# Detailed Setup Instructions

This guide walks you through setting up and running the LLM tutorial examples step-by-step.

## Part 1: Get Your API Keys

### Option A: OpenAI (for GPT-4 mini)

1. Go to [OpenAI API Dashboard](https://platform.openai.com/account/api-keys)
2. Log in with your OpenAI account (create one if needed)
3. Click **"Create new secret key"**
4. Copy the key (you'll only see it once!)
5. Save it somewhere safe temporarily

**Important:** OpenAI provides free trial credits (~$5), but charges after that. Monitor your usage!

### Option B: OpenRouter (for Gemma and other models)

1. Go to [OpenRouter Keys Page](https://openrouter.ai/keys)
2. Log in or create an account
3. Click the key icon to generate a new API key
4. Copy the key

**Advantage:** OpenRouter often has cheaper pricing for various models.

## Part 2: Set Up Environment Variables

### On macOS/Linux (Recommended Approach):

**Step 1: Create your environment file**
```bash
cd /path/to/Highthroughput_LLM_calls_tutorial
cp .env.template .env
```

**Step 2: Edit the .env file**

```bash
# Use your preferred editor
nano .env
# or
vim .env
# or open in VS Code: code .env
```

**Step 3: Add your keys**

The file will look like:
```bash
export OPENAI_API_KEY=""
export OPENROUTER_API_KEY=""
```

Replace the empty strings with your actual keys:
```bash
export OPENAI_API_KEY="sk-proj-1234567890abcdefghijklmnopqrst..."
export OPENROUTER_API_KEY="sk-or-1234567890abcdefghijklmnopqrst..."
```

**Step 4: Source the environment (do this every time you open a new terminal)**

```bash
source .env
```

**Step 5: Verify the keys are loaded**

```bash
echo $OPENAI_API_KEY
```

You should see your key printed (the actual value, not empty).

### On Windows (PowerShell - Alternative):

If you prefer not to use .env files, you can set environment variables directly:

```powershell
# Set the environment variables in User scope (persistent)
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-key-here", "User")
[Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", "your-key-here", "User")

# Restart your terminal or IDE for changes to take effect
```

**Verify:**
```powershell
$env:OPENAI_API_KEY
```

### On Windows (Command Prompt):

```cmd
setx OPENAI_API_KEY "your-key-here"
setx OPENROUTER_API_KEY "your-key-here"
```

Then restart Command Prompt.

## Part 3: Install Python Dependencies

```bash
# Make sure you're in the project directory
cd /path/to/Highthroughput_LLM_calls_tutorial

# Install the required packages
pip install -r requirements.txt
```

**What this installs:**
- `openai` - Official OpenAI Python library (works with both OpenAI and OpenRouter)
- `python-dotenv` - Loads variables from .env file

**Verify installation:**
```bash
python -c "import openai; print(openai.__version__)"
```

## Part 4: Run Your First Example

The unified script `src/llm_paper_analyzer.py` supports both APIs via a `--provider` flag.

### Quick Test with OpenAI (GPT-4 mini - default):

```bash
python src/llm_paper_analyzer.py
```

**Expected output:**
- Loading confirmation for paper and prompt
- Structured analysis with Motivation, Hypothesis, Experiments, and Results
- Elapsed time and token usage for the request
- Results saved to `results/openai_analysis.txt`

### Quick Test with OpenRouter (Gemma):

```bash
python src/llm_paper_analyzer.py --provider openrouter
```

Or using the short flag:
```bash
python src/llm_paper_analyzer.py -p openrouter
```

**Expected output:**
- Similar analysis using the Gemma model
- Note: May be slightly different from GPT-4 mini (different model, different style)
- Results saved to `results/openrouter_analysis.txt`

## Part 5: Understanding the Script

The unified script `src/llm_paper_analyzer.py` follows this flow:

1. **Parse command-line arguments**
   ```python
   parser.add_argument("--provider", choices=["openai", "openrouter"], default="openai")
   ```

2. **Load API key from environment**
   ```python
   api_key = os.environ.get("OPENAI_API_KEY")  # or OPENROUTER_API_KEY
   ```

3. **Load paper and prompt files**
   ```python
   paper = load_paper("examples/papers/paper1.txt")
   prompt = load_prompt("examples/prompts/analysis_prompt.txt")
   ```

4. **Call appropriate analyzer function**
   ```python
   if provider == "openai":
       analysis = analyze_paper_with_openai(paper, prompt, api_key)
   else:
       analysis = analyze_paper_with_openrouter(paper, prompt, api_key)
   ```

5. **Display and save results**
   ```python
   print(analysis)
   # Save to results/ directory
   ```

## Part 6: Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'openai'"

**Solution:**
```bash
pip install -r requirements.txt
# or
pip install openai
```

### Problem: "AuthenticationError" or "Invalid API Key"

**Solutions:**
1. Double-check your key is correct (copy from dashboard again)
2. Verify environment variable is loaded: `echo $OPENAI_API_KEY`
3. Make sure you used correct export format: `export OPENAI_API_KEY="..."`
4. Try hardcoding the key in the script (just for testing!):
   ```python
   client = OpenAI(api_key="your-key-here")
   ```

### Problem: "RateLimitError"

**Causes:**
- You've made too many requests too quickly
- You've exceeded your API quota

**Solutions:**
- Wait a few moments before retrying
- Check your API usage dashboard
- For bulk processing, add delays between requests

### Problem: "Connection timeout"

**Causes:**
- Network issues
- API service is down
- Firewall blocking connections

**Solutions:**
- Check your internet connection
- Check API status page (openai.com or openrouter.ai)
- Try adding a longer timeout (see script comments)

### Problem: Environment variables not loading on macOS/Linux

**Solutions:**
1. Check you're in the right directory:
   ```bash
   pwd
   ls -la .env
   ```

2. Source the file explicitly:
   ```bash
   source .env
   ```

3. For permanent setup (optional), add to `~/.bashrc` or `~/.zshrc`:
   ```bash
   # Add this line to ~/.bashrc or ~/.zshrc
   export OPENAI_API_KEY="your-key"
   export OPENROUTER_API_KEY="your-key"
   ```
   Then: `source ~/.bashrc` or `source ~/.zshrc`

## Part 7: Security Best Practices

1. **Never commit .env to Git**
   - The repository has a `.gitignore` that should prevent this
   - Verify: `git status` should not show `.env`

2. **Don't hardcode keys in scripts**
   - Always load from environment variables

3. **Rotate keys periodically**
   - Delete old keys and generate new ones

4. **Monitor usage**
   - Check your OpenAI/OpenRouter dashboard regularly
   - Set spending limits if available

5. **Use separate keys for development and production**
   - Create one key for learning, another for production

## Part 8: Next Steps

After successfully running the examples:

1. **Modify the prompt** in `examples/prompts/analysis_prompt.txt`
2. **Add your own papers** to `examples/papers/`
3. **Experiment with both models** to compare outputs
4. **Try batch processing** multiple papers
5. **Integrate into your research workflow**

## Quick Reference

```bash
# Setup (one-time)
cp .env.template .env
nano .env                         # Add your keys
source .env                       # Load them
pip install -r requirements.txt

# Run unified analyzer with both providers
python src/llm_paper_analyzer.py                 # Default: OpenAI
python src/llm_paper_analyzer.py -p openrouter  # Use OpenRouter
python src/llm_paper_analyzer.py -p openai      # Explicit OpenAI

# Verify keys loaded
echo $OPENAI_API_KEY
echo $OPENROUTER_API_KEY
```

---

**Need help?** Check the main README.md for more resources and support information.
