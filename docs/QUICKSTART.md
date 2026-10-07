# Quick Start: 5 Minutes to Your First LLM Analysis

Get up and running immediately with this no-nonsense guide.

## 5-Minute Setup

### 1. Install Python packages (1 min)
```bash
pip install -r requirements.txt
```

### 2. Get API keys (2 min)
- **OpenAI:** https://platform.openai.com/account/api-keys (sign up if needed)
- **OpenRouter:** https://openrouter.ai/keys (sign up if needed)

### 3. Add keys to environment (2 min)

**macOS/Linux:**
```bash
cp .env.template .env
nano .env
# Paste your API keys in the empty quotes
source .env
```

**Windows PowerShell:**
```powershell
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-key-here", "User")
[Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", "your-key-here", "User")
# Restart terminal
```

## Run Your First Analysis (2 minutes)

### Test OpenAI (default):
```bash
python src/llm_paper_analyzer.py
```

### Test OpenRouter:
```bash
python src/llm_paper_analyzer.py --provider openrouter
```

You should see structured analysis of the research paper printed to console.

## What's in the Box

```
📁 Highthroughput_LLM_calls_tutorial/
├── � src/
│   ├── 📄 llm_paper_analyzer.py     ← Unified analyzer (--provider flag)
│   └── 📄 requirements.txt
├── 📁 examples/
│   ├── 📁 papers/                    ← Example biophysics papers
│   │   ├── paper1.txt                Protein Folding (MD simulations)
│   │   ├── paper2.txt                Cell Mechanics (AFM)
│   │   └── paper3.txt                Ion Channels (Cryo-EM)
│   └── 📁 prompts/
│       └── analysis_prompt.txt       ← The analysis template
├── 📄 README.md                      ← Full documentation
├── 📄 setup_instructions.md          ← Detailed setup guide
├── 📄 PROMPT_ENGINEERING_GUIDE.md    ← Learn prompt optimization
└── 📄 requirements.txt               ← Python dependencies
```

## Next Steps (Pick One)

### 🎓 Learn Prompt Engineering
Read `PROMPT_ENGINEERING_GUIDE.md` to understand how the analysis prompt works and how to create your own.

### 📝 Modify the Analysis
Edit `examples/prompts/analysis_prompt.txt` to ask different questions:
- Instead of Motivation/Hypothesis/Experiments/Results, try asking for:
  - Background/Innovation/Validation/Significance
  - Problem/Solution/Evidence/Implications
  - Challenge/Approach/Discovery/Applications

### 📚 Analyze Your Own Papers
1. Copy your paper text to `examples/papers/paper4.txt`
2. Run: `python openai_example.py` (update the filename inside)
3. Get instant structured analysis

### 🔬 Compare Models
Run with both providers and compare outputs:
```bash
python src/llm_paper_analyzer.py -p openai > results/openai_output.txt
python src/llm_paper_analyzer.py -p openrouter > results/openrouter_output.txt
# Compare with your favorite text editor
```

### 🏭 Batch Process Multiple Papers
Create a simple loop (see main README for example) to analyze all papers at once.

## Troubleshooting: Quick Fixes

| Problem | Solution |
|---------|----------|
| "ModuleNotFoundError" | `pip install -r requirements.txt` |
| "API key not found" | `echo $OPENAI_API_KEY` (should print your key) |
| "Key not loading on macOS" | `source .env` in terminal each time |
| "API quota exceeded" | Check usage dashboard; rate limits reset after 24h |
| "Timeout error" | Network issue; retry in 30 seconds |

## Example Output

Running either script produces formatted output like:

```
======================================================================
🔄 Sending request to OpenAI (GPT-4 mini)...
======================================================================
✓ Response received in 2.34 seconds
  Tokens used: 487

📊 ANALYSIS RESULTS:
----------------------------------------------------------------------

## MOTIVATION
The researchers wanted to understand how proteins fold from unfolded states to 
functional three-dimensional structures...

## HYPOTHESIS
The team hypothesized that proteins follow specific folding pathways guided by 
free energy landscapes containing multiple intermediate states...

## EXPERIMENTS
Molecular dynamics simulations at multiple temperatures using explicit solvent. 
The study examined 50 replicate folding trajectories of ubiquitin protein...

## RESULTS
Analysis revealed that 76% of trajectories successfully folded to native 
structure within the simulation timeframe. The folding proceeded through...

## KEY INSIGHT
Proteins guide their folding through hierarchical assembly of secondary 
structures that subsequently pack into native tertiary structure.
----------------------------------------------------------------------

✓ Results saved to results/openai_analysis.txt
✅ Analysis complete!
```

## Important Notes

⚠️ **Security:**
- Never commit `.env` file to Git
- Regenerate API keys periodically
- Don't hardcode keys in scripts

💰 **Costs:**
- OpenAI: ~$0.15 per 1M tokens (cheap for small usage)
- OpenRouter: ~$0.10 per 1M tokens (slightly cheaper)
- First-time users get free trial credits
- Set spending limits in API dashboards

⏱️ **Rate Limits:**
- OpenAI: 3 requests/min on free tier (plenty for learning)
- OpenRouter: Similar limits
- Add delays between requests for bulk analysis

## Getting Help

1. **API Key issues?** → Contact OpenAI or OpenRouter support
2. **Python errors?** → Check `setup_instructions.md`
3. **Want better results?** → Read `PROMPT_ENGINEERING_GUIDE.md`
4. **Full documentation** → See `README.md`

---

**Ready to start?** Run one of the example scripts right now:

```bash
python openai_example.py
```

Then explore the code to understand what's happening. You've got this! 🚀
