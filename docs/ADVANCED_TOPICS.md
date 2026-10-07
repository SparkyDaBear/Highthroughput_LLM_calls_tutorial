# Advanced Topics: Extending Your LLM Analysis

This guide covers advanced techniques and best practices for integrating LLM-based paper analysis into your research workflow.

## Table of Contents
1. Comparing Model Outputs
2. Batch Processing Multiple Papers
3. Creating Custom Analysis Prompts
4. Error Handling and Robustness
5. Analyzing Your Own Papers
6. Cost Optimization
7. Integrating into Research Workflows

---

## 1. Comparing Model Outputs

### Why Compare Models?

Different models have different strengths:
- **OpenAI GPT-4 mini:** More nuanced, better at complex reasoning, higher cost
- **OpenRouter Gemma:** Faster, cheaper, good for quick analysis
- **Strategy:** Use Gemma for initial screening, GPT-4 for detailed analysis

### How to Compare Effectively

Create a comparison script (add to your project):

```python
import os
import json
from openai import OpenAI

# This is pseudocode - see below for full implementation

def analyze_with_both_models(paper_text, prompt):
    """Analyze same paper with both models and compare."""
    
    # OpenAI analysis
    openai_result = analyze_with_openai(paper_text, prompt)
    
    # OpenRouter analysis
    openrouter_result = analyze_with_openrouter(paper_text, prompt)
    
    # Save both for comparison
    comparison = {
        "paper": paper_text[:100],  # Paper identifier
        "openai": openai_result,
        "openrouter": openrouter_result,
        "timestamp": datetime.now().isoformat()
    }
    
    with open("comparison_results.json", "a") as f:
        json.dump(comparison, f)
    
    return comparison

def print_side_by_side(openai_result, openrouter_result):
    """Display results for easy comparison."""
    print("\n" + "="*80)
    print("OPENAI (GPT-4 mini)" + " "*40 + "OPENROUTER (Gemma)")
    print("="*80)
    
    openai_lines = openai_result.split('\n')
    openrouter_lines = openrouter_result.split('\n')
    
    max_lines = max(len(openai_lines), len(openrouter_lines))
    
    for i in range(max_lines):
        oai = openai_lines[i] if i < len(openai_lines) else ""
        ortr = openrouter_lines[i] if i < len(openrouter_lines) else ""
        print(f"{oai:<40} | {ortr:<40}")
```

### What to Look For

1. **Tone and Style**
   - GPT-4 tends to be more academic
   - Gemma may be more direct/conversational

2. **Completeness**
   - Does one model miss sections the other includes?
   - Do quantitative details appear in both?

3. **Accuracy**
   - Check results against original paper
   - Note any hallucinations or made-up details

4. **Length and Conciseness**
   - Faster doesn't always mean worse
   - Longer isn't always more comprehensive

### When to Use Which Model

**Use OpenAI GPT-4 mini for:**
- Complex papers with subtle interpretations needed
- First detailed analysis of critical papers
- When accuracy is more important than cost
- Papers from unfamiliar domains

**Use OpenRouter Gemma for:**
- Initial screening of many papers
- Well-structured papers with clear methodology
- When speed and cost matter more than nuance
- Repeated analyses on similar topics

---

## 2. Batch Processing Multiple Papers

### Simple Batch Analysis

Modify the example scripts to process multiple papers:

```python
import os
import glob
from pathlib import Path

def batch_analyze(paper_directory, use_openai=True):
    """Analyze all papers in a directory."""
    
    paper_files = glob.glob(os.path.join(paper_directory, "*.txt"))
    results = []
    
    print(f"Found {len(paper_files)} papers to analyze...")
    
    for i, paper_file in enumerate(paper_files, 1):
        print(f"\n[{i}/{len(paper_files)}] Analyzing {os.path.basename(paper_file)}...")
        
        with open(paper_file, 'r') as f:
            paper_text = f.read()
        
        if use_openai:
            analysis = analyze_with_openai(paper_text)
        else:
            analysis = analyze_with_openrouter(paper_text)
        
        results.append({
            "filename": os.path.basename(paper_file),
            "analysis": analysis
        })
        
        # Save incrementally (in case of errors mid-batch)
        save_results(results, f"batch_results_{i}.json")
    
    return results

# Usage:
# batch_analyze("examples/papers/")
```

### Handling Rate Limits

APIs have rate limits. Add delays between requests:

```python
import time

def batch_analyze_with_rate_limiting(paper_directory, delay_seconds=2):
    """Analyze papers with delays to respect rate limits."""
    
    paper_files = glob.glob(os.path.join(paper_directory, "*.txt"))
    
    for paper_file in paper_files:
        # Analyze
        with open(paper_file, 'r') as f:
            analysis = analyze_paper(f.read())
        
        # Save results
        save_result(analysis)
        
        # Wait before next request
        print(f"Waiting {delay_seconds} seconds before next request...")
        time.sleep(delay_seconds)
    
    print("Batch analysis complete!")
```

### Organize Results

Save results in structured formats:

```python
import json
import csv
from datetime import datetime

def save_results_structured(analyses, output_format="json"):
    """Save results in multiple formats for flexibility."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        # Good for: Detailed analysis, easy to parse
        with open(f"results_{timestamp}.json", "w") as f:
            json.dump(analyses, f, indent=2)
    
    elif output_format == "csv":
        # Good for: Quick scanning, comparison across papers
        with open(f"results_{timestamp}.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=analyses[0].keys())
            writer.writeheader()
            writer.writerows(analyses)
    
    elif output_format == "markdown":
        # Good for: Reading in notebooks, sharing with others
        with open(f"results_{timestamp}.md", "w") as f:
            for analysis in analyses:
                f.write(f"# {analysis['filename']}\n\n")
                f.write(analysis['analysis'])
                f.write("\n\n---\n\n")
```

---

## 3. Creating Custom Analysis Prompts

### Adapting for Different Domains

The base prompt focuses on Motivation/Hypothesis/Experiments/Results. Adapt it for other fields:

**For Machine Learning Papers:**
```
Extract:
- Problem Statement
- Proposed Method/Architecture  
- Datasets and Baselines
- Performance Metrics and Comparison
- Limitations and Future Work
```

**For Review Articles:**
```
Extract:
- Main Topic and Scope
- Current Understanding
- Key Open Questions
- Recent Breakthroughs
- Future Directions
```

**For Clinical Studies:**
```
Extract:
- Clinical Question
- Patient Population and Design
- Intervention Description
- Primary Outcomes
- Clinical Significance
```

### Template for Custom Prompts

Use this structure when creating your own:

```
## YOUR CUSTOM ANALYSIS PROMPT

### ROLE
You are [EXPERT TYPE] with expertise in [DOMAIN].

### TASK
Extract these components from the paper:
1. [COMPONENT 1] - Definition of what to extract
2. [COMPONENT 2] - Definition of what to extract
3. [COMPONENT 3] - Definition of what to extract

### INSTRUCTIONS FOR EACH SECTION
[For each component, provide 2-3 sentences about:
- What counts as this component
- What detail level to include
- How to format the response]

### OUTPUT FORMAT
Use this exact structure:
---
## COMPONENT 1
[Your analysis here]

## COMPONENT 2
[Your analysis here]
---

### QUALITY CRITERIA
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

### DO NOT
- [Common mistake to avoid]
- [Another mistake to avoid]
```

---

## 4. Error Handling and Robustness

### Common Errors and Solutions

```python
from openai import APIError, RateLimitError, APIConnectionError
import time

def analyze_with_retry(paper_text, prompt, max_retries=3):
    """Analyze with automatic retry logic."""
    
    for attempt in range(max_retries):
        try:
            # Attempt analysis
            result = analyze_paper(paper_text, prompt)
            return result
            
        except RateLimitError:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries exceeded due to rate limiting.")
                raise
        
        except APIConnectionError:
            if attempt < max_retries - 1:
                print("Connection error. Retrying...")
                time.sleep(1)
            else:
                print("Could not connect to API after retries.")
                raise
        
        except APIError as e:
            print(f"API Error: {e}")
            raise
    
    return None

def validate_paper_text(text):
    """Validate that paper text is suitable for analysis."""
    
    # Check minimum length
    if len(text) < 500:
        raise ValueError("Paper text too short (< 500 characters)")
    
    # Check that it contains key sections
    required_sections = ["abstract", "introduction", "method", "result"]
    text_lower = text.lower()
    
    found_sections = sum(1 for section in required_sections 
                        if section in text_lower)
    
    if found_sections < 2:
        print(f"Warning: Found only {found_sections} expected sections")
    
    return True
```

### Logging and Debugging

```python
import logging

def setup_logging(log_file="llm_analysis.log"):
    """Set up logging for debugging."""
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

# Usage:
logger = setup_logging()

logger.info(f"Starting analysis of paper: {paper_id}")
logger.info(f"Using model: {model_name}")
logger.info(f"Analysis complete. Tokens used: {token_count}")
```

---

## 5. Analyzing Your Own Papers

### Step-by-Step Guide

**Step 1: Prepare your paper**
```bash
# Extract text from PDF (if needed)
# Save as .txt file in examples/papers/
cp ~/my_paper.pdf examples/papers/
# Convert PDF to text (many free tools available)
```

**Step 2: Create a custom prompt (optional)**
```bash
cp examples/prompts/analysis_prompt.txt examples/prompts/my_custom_prompt.txt
# Edit my_custom_prompt.txt to match your needs
```

**Step 3: Modify the Python script**
```python
# In your script, change:
paper_text = load_paper("examples/papers/my_paper.txt")
prompt_text = load_prompt("examples/prompts/my_custom_prompt.txt")
```

**Step 4: Run analysis**
```bash
python openai_example.py
```

### Tips for Best Results

1. **Clean the text**
   - Remove headers/footers (page numbers, dates)
   - Fix encoding issues
   - Remove tables (they confuse LLMs; describe instead)

2. **Provide context**
   - If paper is highly specialized, add domain background to prompt
   - Consider providing a brief abstract

3. **Iterate on prompts**
   - Run once and check results
   - Refine prompt if results miss details you need
   - Test refined prompt on a few papers before batch processing

4. **Validate results**
   - Always spot-check LLM outputs
   - Cross-reference with original paper
   - Watch for hallucinations (claims not in paper)

---

## 6. Cost Optimization

### Estimating Costs

```python
def estimate_cost(paper_length_chars, num_papers, model="gpt-4-mini"):
    """Estimate analysis costs."""
    
    # Rough token count (1 token ≈ 4 characters)
    tokens_per_paper = paper_length_chars / 4
    
    # Prompt overhead
    prompt_tokens = 200  # Prompt size
    total_tokens = (tokens_per_paper + prompt_tokens) * num_papers
    
    # Pricing (per 1M tokens)
    prices = {
        "gpt-4-mini": 0.15,      # Input tokens
        "gemma": 0.10,           # Via OpenRouter
    }
    
    cost = (total_tokens / 1_000_000) * prices.get(model, 0.15)
    return cost

# Example:
print(estimate_cost(50000, 100, "gpt-4-mini"))  # Cost to analyze 100 papers
```

### Cost-Saving Strategies

1. **Use Gemma for bulk work**
   - 33% cheaper than GPT-4 mini
   - Good enough for screening and categorization

2. **Batch requests**
   - Fewer API calls = fewer rate limit delays
   - Process multiple papers in one session

3. **Cache prompts**
   - Use the same prompt template across papers
   - Some APIs offer prompt caching discounts

4. **Limit output length**
   - Smaller responses cost less
   - Set `max_tokens` appropriately

5. **Monitor usage**
   - Check API dashboards regularly
   - Set spending alerts/limits

---

## 7. Integrating into Research Workflows

### Workflow Integration Example

```python
"""
Complete workflow: Collect papers → Analyze → Compare → Identify patterns
"""

def research_workflow(paper_directory):
    """Complete analysis pipeline."""
    
    # Step 1: Collect and validate papers
    logger.info("Step 1: Collecting papers...")
    papers = load_and_validate_papers(paper_directory)
    logger.info(f"Found {len(papers)} valid papers")
    
    # Step 2: Quick screening with Gemma
    logger.info("Step 2: Quick screening with Gemma...")
    gemma_results = batch_analyze_gemma(papers)
    
    # Step 3: Deep analysis of promising papers with GPT-4
    logger.info("Step 3: Deep analysis of top papers...")
    promising_indices = filter_by_relevance(gemma_results, threshold=0.7)
    gpt_results = [analyze_with_gpt4(papers[i]) for i in promising_indices]
    
    # Step 4: Compare results and identify patterns
    logger.info("Step 4: Comparing results and identifying patterns...")
    comparison = compare_analyses(gemma_results, gpt_results)
    patterns = identify_research_trends(comparison)
    
    # Step 5: Generate summary report
    logger.info("Step 5: Generating report...")
    report = generate_report(papers, gemma_results, gpt_results, patterns)
    
    return report

def generate_report(papers, gemma_results, gpt_results, patterns):
    """Create a comprehensive analysis report."""
    
    report = {
        "metadata": {
            "num_papers": len(papers),
            "analysis_date": datetime.now().isoformat(),
            "models_used": ["gemma", "gpt-4-mini"]
        },
        "individual_analyses": gpt_results,
        "identified_patterns": patterns,
        "recommendations": generate_recommendations(patterns)
    }
    
    # Save as both JSON and markdown
    save_report_json(report)
    save_report_markdown(report)
    
    return report
```

### Common Integration Scenarios

**Scenario 1: Literature Review**
```
1. Batch analyze all papers in your reading list
2. Extract key findings automatically
3. Identify gaps and future directions
4. Organize results by theme
```

**Scenario 2: Grant Writing**
```
1. Extract "Significance" sections from related papers
2. Synthesize to demonstrate research importance
3. Identify collaborative opportunities
4. Generate preliminary background section
```

**Scenario 3: Seminar Presentations**
```
1. Analyze papers before presenting
2. Extract key takeaways for slides
3. Identify questions to address
4. Generate discussion talking points
```

**Scenario 4: Collaborator Communication**
```
1. Analyze papers from collaborators' domain
2. Extract key concepts in accessible language
3. Identify common ground between fields
4. Generate discussion points for meetings
```

---

## Putting It All Together

Start simple:
1. Run the example scripts
2. Understand how they work
3. Modify for your needs
4. Batch process multiple papers
5. Compare results between models
6. Build custom prompts
7. Integrate into your workflow

---

## Further Reading

- **Prompt Optimization:** See `PROMPT_ENGINEERING_GUIDE.md`
- **Setup Help:** See `setup_instructions.md`
- **Quick Start:** See `QUICKSTART.md`

---

Remember: These tools are most powerful when combined with critical human judgment. Always verify LLM outputs against original sources before using them in research!
