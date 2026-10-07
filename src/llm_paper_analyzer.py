#!/usr/bin/env python3
"""
Biophysics Paper Analysis with LLM APIs

This script demonstrates how to analyze research papers using either:
- OpenAI's GPT-4 mini model
- OpenRouter's Gemma-2 model (via google/gemma-2-9b-it)

The only difference between providers is the API endpoint and model used.
All other logic remains the same.

Requirements:
- Environment variables: OPENAI_API_KEY and/or OPENROUTER_API_KEY
- Run with: python llm_paper_analyzer.py --provider openai
            python llm_paper_analyzer.py --provider openrouter

Author: Biophysics Tutorial
"""

import os
import sys
import time
import argparse
from openai import OpenAI
import openai

# Get the project root directory (parent of src/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)


def load_paper(filepath):
    """Load paper text from a file."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}")
        exit(1)


def load_prompt(filepath):
    """Load the analysis prompt from a file."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}")
        exit(1)


def analyze_paper_with_openai(paper_text, prompt_template, api_key):
    """
    Use OpenAI's GPT-4 mini model to analyze a paper.
    
    Args:
        paper_text: The text of the research paper
        prompt_template: The analysis prompt
        api_key: OpenAI API key
    
    Returns:
        The model's response text
    """
    
    # Create the OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Combine the prompt template with the paper text
    user_message = f"{prompt_template}\n\n[PAPER TEXT]\n{paper_text}"
    
    print("\n" + "="*70)
    print("🔄 Sending request to OpenAI (GPT-4 mini)...")
    print("="*70)
    
    # Make the API call
    start_time = time.time()
    
    response = client.chat.completions.create(
        model="gpt-4-mini",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.7,  # Slightly creative but factual (0=deterministic, 1=creative)
        max_tokens=1500,   # Limit response length
    )
    
    elapsed_time = time.time() - start_time
    
    # Extract the response
    analysis = response.choices[0].message.content
    
    # Print timing and token info
    print(f"✓ Response received in {elapsed_time:.2f} seconds")
    print(f"  Tokens used: {response.usage.total_tokens}")
    print("="*70 + "\n")
    
    return analysis


def analyze_paper_with_openrouter(paper_text, prompt_template, api_key):
    """
    Use OpenRouter's API with Google Gemma model to analyze a paper.
    
    OpenRouter is a gateway to many models and is often cheaper than direct APIs.
    
    Args:
        paper_text: The text of the research paper
        prompt_template: The analysis prompt
        api_key: OpenRouter API key
    
    Returns:
        The model's response text
    """
    
    # Configure OpenAI library to use OpenRouter's API endpoint
    openai.api_key = api_key
    openai.api_base = "https://openrouter.ai/api/v1"
    
    # Combine the prompt template with the paper text
    user_message = f"{prompt_template}\n\n[PAPER TEXT]\n{paper_text}"
    
    print("\n" + "="*70)
    print("🔄 Sending request to OpenRouter (Gemma-2-9b-it)...")
    print("="*70)
    
    # Make the API call
    start_time = time.time()
    
    try:
        response = openai.ChatCompletion.create(
            model="google/gemma-2-9b-it",  # Latest Gemma 2 9B instruction-tuned model
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.7,  # Slightly creative but factual
            max_tokens=1500,   # Limit response length
        )
    except Exception as e:
        print(f"\n❌ API Error: {e}")
        print("\nThis might be because:")
        print("  - Your OpenRouter API key is invalid")
        print("  - You've exceeded your API quota")
        print("  - OpenRouter service is temporarily unavailable")
        raise
    
    elapsed_time = time.time() - start_time
    
    # Extract the response
    analysis = response.choices[0].message["content"]
    
    # Print timing and token info
    print(f"✓ Response received in {elapsed_time:.2f} seconds")
    print(f"  Model: google/gemma-2-9b-it")
    print("="*70 + "\n")
    
    return analysis


def main(provider="openai"):
    """Main function - runs the analysis pipeline."""
    
    # Validate provider
    if provider not in ["openai", "openrouter"]:
        print(f"❌ ERROR: Invalid provider '{provider}'")
        print("   Must be either 'openai' or 'openrouter'")
        sys.exit(1)
    
    # Display header
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "BIOPHYSICS PAPER ANALYSIS" + " "*28 + "║")
    
    if provider == "openai":
        print("║" + " "*17 + "Using OpenAI's GPT-4 mini Model" + " "*21 + "║")
        env_key = "OPENAI_API_KEY"
        paper_path = os.path.join(PROJECT_ROOT, "examples/papers/paper1.txt")
    else:
        print("║" + " "*17 + "Using OpenRouter's Gemma Model" + " "*21 + "║")
        env_key = "OPENROUTER_API_KEY"
        paper_path = os.path.join(PROJECT_ROOT, "examples/papers/paper2.txt")
    
    print("╚" + "="*68 + "╝")
    
    # Get API key from environment
    api_key = os.environ.get(env_key)
    if not api_key:
        print(f"\n❌ ERROR: {env_key} environment variable not set!")
        print("\nTo fix this:")
        print("  1. Copy .env.template to .env")
        print(f"  2. Add your {provider.upper()} API key to .env")
        print("  3. Run: source .env")
        print(f"  4. Try again: python llm_paper_analyzer.py --provider {provider}")
        exit(1)
    
    # Load paper and prompt
    print("\n📖 Loading paper and prompt...")
    paper = load_paper(paper_path)
    prompt = load_prompt(os.path.join(PROJECT_ROOT, "examples/prompts/analysis_prompt.txt"))
    
    # Analyze the paper
    print(f"\n📄 Paper loaded ({len(paper)} characters)")
    print(f"📝 Analysis prompt loaded ({len(prompt)} characters)")
    
    # Run the analysis
    if provider == "openai":
        analysis = analyze_paper_with_openai(paper, prompt, api_key)
    else:
        analysis = analyze_paper_with_openrouter(paper, prompt, api_key)
    
    # Display results
    print("\n📊 ANALYSIS RESULTS:")
    print("-"*70)
    print(analysis)
    print("-"*70)
    
    # Save results to file
    output_file = os.path.join(PROJECT_ROOT, f"results/{provider}_analysis.txt")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        with open(output_file, 'w') as f:
            f.write(f"{provider.upper()} PAPER ANALYSIS\n")
            f.write("="*70 + "\n")
            if provider == "openai":
                f.write("Model: GPT-4 mini\n")
            else:
                f.write("Model: Gemma-2-9b-it via OpenRouter\n")
            f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*70 + "\n\n")
            f.write(analysis)
        print(f"\n✓ Results saved to {output_file}")
    except Exception as e:
        print(f"\n⚠️  Could not save results: {e}")
    
    print("\n✅ Analysis complete!")
    print("\n💡 Tip: Try comparing outputs from both providers:")
    print("        python llm_paper_analyzer.py --provider openai")
    print("        python llm_paper_analyzer.py --provider openrouter")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze biophysics papers with LLM APIs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python llm_paper_analyzer.py --provider openai
  python llm_paper_analyzer.py --provider openrouter
  python llm_paper_analyzer.py -p openai

Default provider: openai
        """
    )
    
    parser.add_argument(
        "--provider",
        "-p",
        choices=["openai", "openrouter"],
        default="openai",
        help="Which LLM provider to use (default: openai)"
    )
    
    args = parser.parse_args()
    main(provider=args.provider)
