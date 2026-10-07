#!/usr/bin/env python3
"""
OpenAI Example: Analyze Biophysics Papers with GPT-4 mini

This script demonstrates how to use the OpenAI API to analyze research papers
and extract key information: motivation, hypothesis, experiments, and results.

Requirements:
- OPENAI_API_KEY environment variable set
- Run: python openai_example.py

Author: Biophysics Tutorial
"""

import os
import time
from openai import OpenAI

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


def main():
    """Main function - runs the analysis pipeline."""
    
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "BIOPHYSICS PAPER ANALYSIS - OPENAI" + " "*19 + "║")
    print("║" + " "*17 + "Using OpenAI's GPT-4 mini Model" + " "*21 + "║")
    print("╚" + "="*68 + "╝")
    
    # Get API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("\n❌ ERROR: OPENAI_API_KEY environment variable not set!")
        print("\nTo fix this:")
        print("  1. Copy .env.template to .env")
        print("  2. Add your OpenAI API key to .env")
        print("  3. Run: source .env")
        print("  4. Try again: python openai_example.py")
        exit(1)
    
    # Load paper and prompt
    print("\n📖 Loading paper and prompt...")
    paper = load_paper(os.path.join(PROJECT_ROOT, "examples/papers/paper1.txt"))
    prompt = load_prompt(os.path.join(PROJECT_ROOT, "examples/prompts/analysis_prompt.txt"))
    
    # Analyze the paper
    print(f"\n📄 Paper loaded ({len(paper)} characters)")
    print(f"📝 Analysis prompt loaded ({len(prompt)} characters)")
    
    # Run the analysis
    analysis = analyze_paper_with_openai(paper, prompt, api_key)
    
    # Display results
    print("\n📊 ANALYSIS RESULTS:")
    print("-"*70)
    print(analysis)
    print("-"*70)
    
    # Optional: Save results to file
    output_file = os.path.join(PROJECT_ROOT, "results/openai_analysis.txt")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        with open(output_file, 'w') as f:
            f.write("OPENAI PAPER ANALYSIS\n")
            f.write("="*70 + "\n")
            f.write(f"Model: GPT-4 mini\n")
            f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*70 + "\n\n")
            f.write(analysis)
        print(f"\n✓ Results saved to {output_file}")
    except Exception as e:
        print(f"\n⚠️  Could not save results: {e}")
    
    print("\n✅ Analysis complete!")
    print("\n💡 Tip: Try modifying the prompt in examples/prompts/analysis_prompt.txt")
    print("        and see how it changes the analysis!")


if __name__ == "__main__":
    main()
