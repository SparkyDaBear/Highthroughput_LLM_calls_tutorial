# High-Throughput LLM Calls Tutorial

A beginner-friendly guide to calling Large Language Models (LLMs) via the OpenAI Python module, supporting both **OpenAI** and **OpenRouter** APIs. This tutorial is designed for biophysics students learning to extract scientific insights from research papers using AI-powered analysis.

## 🎯 What You'll Learn

- Set up API keys securely using environment variables
- Call OpenAI's GPT-4 mini model for efficient analysis
- Call OpenRouter's Gemma model as a cost-effective alternative
- Apply prompt engineering best practices for scientific text analysis
- Analyze biophysics papers to extract: motivations, hypotheses, experiments, and results

## 📋 Prerequisites

- Python 3.8 or higher
- API keys from:
  - **OpenAI** (https://platform.openai.com/account/api-keys)
  - **OpenRouter** (https://openrouter.ai/keys)
- Basic familiarity with terminal/command line

## 🚀 Quick Start

### Step 1: Set Up Your Environment

#### On macOS/Linux:

```bash
# Create a copy of the environment template
cp .env.template .env

# Edit the file and add your API keys
nano .env
# or use your preferred editor (vim, code, etc.)

# Source the environment variables
source .env
```

**Add your keys to `.env`:**
```bash
export OPENAI_API_KEY="your-openai-key-here"
export OPENROUTER_API_KEY="your-openrouter-key-here"
```

#### On Windows (PowerShell):

```powershell
# Create environment variables
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-key-here", "User")
[Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", "your-key-here", "User")

# Restart your terminal/IDE for changes to take effect
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Example

#### Test OpenAI (GPT-4 mini):
```bash
python src/llm_paper_analyzer.py --provider openai
```

#### Test OpenRouter (Gemma):
```bash
python src/llm_paper_analyzer.py --provider openrouter
```

#### Or using short flag:
```bash
python src/llm_paper_analyzer.py -p openai
```

## 📁 Project Structure

```
.
├── README.md                          # This file
├── setup_instructions.md              # Detailed setup guide
├── requirements.txt                   # Python dependencies
├── .env.template                      # Environment variable template
├── src/
│   ├── llm_paper_analyzer.py          # Unified analyzer (--provider flag)
│   └── requirements.txt
├── examples/
│   ├── papers/
│   │   ├── paper1.txt                # Example biophysics paper excerpt
│   │   ├── paper2.txt
│   │   └── paper3.txt
│   └── prompts/
│       └── analysis_prompt.txt        # Prompt for paper analysis
└── results/                           # Output directory for analysis results
```

## 📚 About the Example Papers

The tutorial includes excerpts from open-access biophysics research papers covering:
1. **Protein Dynamics & Folding** - Understanding how proteins move and fold
2. **Molecular Simulations** - Computational methods in biophysics
3. **Biomechanics & Cell Mechanics** - How cells and tissues behave mechanically

Each paper excerpt includes abstract, introduction, and key experimental sections—perfect for practicing LLM-based analysis.

## 🧪 How to Run Your Own Analysis

### Using the Unified Script:

The single `src/llm_paper_analyzer.py` script handles both providers via a `--provider` argument:

```bash
# Use OpenAI (default)
python src/llm_paper_analyzer.py

# Use OpenRouter
python src/llm_paper_analyzer.py --provider openrouter
```

Internally, the script has separate `analyze_paper_with_openai()` and `analyze_paper_with_openrouter()` functions, but they share the same data loading, prompting, and result saving logic.

## 💡 Prompt Engineering Tips

The analysis prompt in `examples/prompts/analysis_prompt.txt` demonstrates:

1. **Role Definition** - "You are a expert biophysics researcher..."
2. **Clear Task** - Specific what you want extracted
3. **Structured Output** - Define exactly how results should be formatted
4. **Examples** - Show the model what you expect
5. **Context** - Provide background on the domain

Better prompts → Better results. Experiment and iterate!

## 🔑 Model Comparison

| Aspect | OpenAI (GPT-4 mini) | OpenRouter (Gemma) |
|--------|-----|---------|
| **Cost** | ~$0.15/1M tokens | ~$0.10/1M tokens |
| **Speed** | Very Fast | Very Fast |
| **Quality** | Excellent | Good |
| **Best For** | Complex analysis, nuanced tasks | Quick analysis, cost-sensitive work |

## ⚠️ Important Security Notes

- **Never commit API keys** to version control
- The `.env` file is in `.gitignore` to protect your keys
- Always use environment variables for credentials
- Consider rotating API keys periodically
- Monitor your API usage to avoid unexpected charges

## 🐛 Troubleshooting

### "Authentication failed" error
- Verify your API key is correct (copy directly from provider dashboard)
- Check that environment variables are loaded: `echo $OPENAI_API_KEY`
- Ensure you sourced `.env` on Linux/macOS

### "Rate limit exceeded"
- OpenAI and OpenRouter have usage limits
- Add delays between requests in production code
- Check your account dashboard for current quotas

### "Module not found" error
- Ensure you installed dependencies: `pip install -r requirements.txt`
- Verify you're using the correct Python environment

## 📖 Next Steps

1. **Modify the prompts** - Try different analysis frameworks
2. **Add more papers** - Test on your own research materials
3. **Compare outputs** - See how OpenAI and OpenRouter differ
4. **Build batch processing** - Analyze many papers at once
5. **Integrate into workflows** - Use in your own projects

## 📚 Additional Resources

- [OpenAI Documentation](https://platform.openai.com/docs)
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## 📞 Support

For issues with:
- **API Keys** → Contact OpenAI or OpenRouter support
- **Python code** → Check the setup_instructions.md file
- **Prompts** → Try rephrasing or providing more examples

---

**Happy coding! Remember: the quality of your prompt determines the quality of your results.** 🚀