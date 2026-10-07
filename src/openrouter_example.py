#!/usr/bin/env python3
"""
OpenRouter Example: Analyze Biophysics Papers with Gemma Model

This script demonstrates how to use the OpenRouter API (via OpenAI library)
to analyze research papers using Google's Gemma model - a cost-effective alternative.

The script uses the OpenAI Python library but points to OpenRouter's API endpoint.

Requirements:
- OPENROUTER_API_KEY environment variable set
- Run: python openrouter_example.py

Author: Biophysics Tutorial
"""

import os
import time
import openai  # Using the openai package for compatibility with OpenRouter

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
        print("Make sure you're running this script from the project root directory.")
        exit(1)


def load_prompt(filepath):
    """Load the analysis prompt from a file."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}")
        exit(1)


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


def main():
    """Main function - runs the analysis pipeline."""
    
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "BIOPHYSICS PAPER ANALYSIS - OPENROUTER" + " "*14 + "║")
    print("║" + " "*18 + "Using Google's Gemma-2 Model" + " "*21 + "║")
    print("╚" + "="*68 + "╝")
    
    # Get API key from environment
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("\n❌ ERROR: OPENROUTER_API_KEY environment variable not set!")
        print("\nTo fix this:")
        print("  1. Go to https://openrouter.ai/keys and get your API key")
        print("  2. Copy .env.template to .env")
        print("  3. Add your OpenRouter API key to .env")
        print("  4. Run: source .env")
        print("  5. Try again: python openrouter_example.py")
        exit(1)
    
    # Load paper and prompt
    print("\n📖 Loading paper and prompt...")
    paper = load_paper(os.path.join(PROJECT_ROOT, "examples/papers/paper2.txt"))  # Using paper2 for variety
    prompt = load_prompt(os.path.join(PROJECT_ROOT, "examples/prompts/analysis_prompt.txt"))
    
    # Analyze the paper
    print(f"\n📄 Paper loaded ({len(paper)} characters)")
    print(f"📝 Analysis prompt loaded ({len(prompt)} characters)")
    
    # Run the analysis
    analysis = analyze_paper_with_openrouter(paper, prompt, api_key)
    
    # Display results
    print("\n📊 ANALYSIS RESULTS:")
    print("-"*70)
    print(analysis)
    print("-"*70)
    
    # Optional: Save results to file
    output_file = os.path.join(PROJECT_ROOT, "results/openrouter_analysis.txt")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        with open(output_file, 'w') as f:
            f.write("OPENROUTER PAPER ANALYSIS\n")
            f.write("="*70 + "\n")
            f.write(f"Model: Gemma-2-9b-it via OpenRouter\n")
            f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*70 + "\n\n")
            f.write(analysis)
        print(f"\n✓ Results saved to {output_file}")
    except Exception as e:
        print(f"\n⚠️  Could not save results: {e}")
    
    print("\n✅ Analysis complete!")
    print("\n💡 Tip: Compare results between OpenAI and OpenRouter models!")
    print("        Try running: python openai_example.py")


if __name__ == "__main__":
    main()
