# File Structure & Quick Reference

This is a complete map of all files in the tutorial package and what each one does.

## 📁 Complete Directory Structure

```
Highthroughput_LLM_calls_tutorial/
│
├── 📄 README.md                          ⭐ Main documentation hub
│   └── Start here for project overview
│
├── 📄 QUICKSTART.md                      ⚡ 5-minute quick start
│   └── For "just show me how it works" learners
│
├── 📄 PROJECT_OVERVIEW.md                🗺️  This file - complete guide
│   └── Explains every component and learning paths
│
├── 📄 setup_instructions.md              🔧 Detailed step-by-step setup
│   └── Platform-specific guides (macOS/Linux/Windows)
│
├── 📄 PROMPT_ENGINEERING_GUIDE.md        🧠 How to write effective prompts
│   └── Deep dive into prompting techniques
│
├── 📄 ADVANCED_TOPICS.md                 🚀 Scaling and integration
│   └── Batch processing, custom workflows, optimization
│
├── 🐍 src/                           💻 Python scripts
│   ├── llm_paper_analyzer.py        Unified analyzer (supports both APIs)
│   └── requirements.txt             Python dependencies
│
├── 📋 requirements.txt                   📦 Python dependencies
│   ├── openai>=1.3.0
│   └── python-dotenv>=1.0.0
│
├── 🔐 .env.template                      🔑 Environment variables template
│   ├── DO NOT EDIT - template only
│   └── Copy to .env and add your real keys
│
├── 🚫 .gitignore                         🛡️  Prevents committing secrets
│   ├── Protects: .env, API keys, cache
│   └── Allows: code and documentation
│
├── 📁 examples/                          📚 Sample data and prompts
│   │
│   ├── 📁 papers/                        🧬 Biophysics research papers
│   │   ├── paper1.txt                  (protein folding)
│   │   ├── paper2.txt                  (cell mechanics)
│   │   └── paper3.txt                  (ion channels)
│   │
│   └── 📁 prompts/                       💭 Analysis prompts
│       └── analysis_prompt.txt         (main analysis framework)
│
├── 📁 results/                           📊 Output directory
│   ├── openai_analysis.txt             (created on first run)
│   └── openrouter_analysis.txt         (created on first run)
│
└── 📁 .git/                              📝 Version control
    └── (repository history)
```

## 📚 File-by-File Guide

### Core Learning Files

| File | Purpose | Reading Time | When to Use |
|------|---------|--------------|------------|
| **README.md** | Project overview, concepts, model comparison | 10-15 min | First! Overview of everything |
| **QUICKSTART.md** | 5-minute setup and first run | 5 min | Want quick results immediately |
| **PROJECT_OVERVIEW.md** | (This file) Complete map and learning paths | 10 min | Understand the whole package |
| **setup_instructions.md** | Step-by-step setup guide for each OS | 15-20 min | Actually setting up (first time) |
| **PROMPT_ENGINEERING_GUIDE.md** | Deep dive into prompting techniques | 45 min | Want to understand prompt engineering |
| **ADVANCED_TOPICS.md** | Batch processing, workflows, optimization | 1 hour | Ready to scale up your usage |

### Executable Scripts

| File | Purpose | How to Use |
|------|---------|----------|
| **src/llm_paper_analyzer.py** | Unified analyzer for both APIs | `python src/llm_paper_analyzer.py --provider openai` or `--provider openrouter` |

### Configuration Files

| File | Purpose | Do I Edit It? | Notes |
|------|---------|--------------|-------|
| **.env.template** | Template showing what variables needed | ❌ No | Copy to `.env`, edit the copy |
| **.env** | Your actual API keys | ✅ Yes | Created from .env.template, never commit to Git |
| **requirements.txt** | Python package list | ❌ Usually not | Only if adding new dependencies |
| **.gitignore** | Prevents committing secrets | ❌ No | Already configured correctly |

### Example Data

| File | Type | Content | Use For |
|------|------|---------|---------|
| **paper1.txt** | Research paper | Protein folding (ubiquitin) | OpenAI example script |
| **paper2.txt** | Research paper | Cell mechanics (AFM) | OpenRouter example script |
| **paper3.txt** | Research paper | Ion channels (cryo-EM) | Testing/comparison |
| **analysis_prompt.txt** | Prompt template | Structured analysis framework | Shows prompt engineering principles |

### Output Files (Created After Running)

| File | Created By | Purpose |
|------|-----------|---------|
| **results/openai_analysis.txt** | openai_example.py | Paper analysis using GPT-4 mini |
| **results/openrouter_analysis.txt** | openrouter_example.py | Paper analysis using Gemma |
| **results/** | Your scripts | Where all output files go by default |

## 🎯 By Task: What File Do I Need?

### "I just want to run the examples"
```
1. QUICKSTART.md
2. Run: python openai_example.py
3. Run: python openrouter_example.py
```

### "I want to understand what's happening"
```
1. README.md (overview)
2. setup_instructions.md (understand the setup)
3. openai_example.py (read the comments)
4. PROMPT_ENGINEERING_GUIDE.md (learn prompting)
```

### "I want to analyze my own papers"
```
1. setup_instructions.md (if not done)
2. Read PROMPT_ENGINEERING_GUIDE.md
3. Create custom prompt based on analysis_prompt.txt
4. Copy your paper to examples/papers/my_paper.txt
5. Modify openai_example.py to use your files
```

### "I want to process 100s of papers"
```
1. Complete basic setup (QUICKSTART.md)
2. Read ADVANCED_TOPICS.md (Batch Processing section)
3. Build batch processing script based on patterns shown
4. Monitor costs (see ADVANCED_TOPICS.md Cost Optimization)
```

### "I'm stuck and need help"
```
1. Check setup_instructions.md Troubleshooting section
2. Check PROMPT_ENGINEERING_GUIDE.md if about prompts
3. Check ADVANCED_TOPICS.md if about scaling
4. Check official API docs:
   - openai.com/docs
   - openrouter.ai/docs
```

## 💡 File Purposes Summarized

### Documentation (Read these)
- **README.md** → What is this project?
- **QUICKSTART.md** → How do I run it? (fast)
- **PROJECT_OVERVIEW.md** → What's in the box? (comprehensive)
- **setup_instructions.md** → How do I set it up? (detailed)
- **PROMPT_ENGINEERING_GUIDE.md** → How do prompts work?
- **ADVANCED_TOPICS.md** → How do I scale this up?

### Python Code (Run this)
- **src/llm_paper_analyzer.py** → Single unified analyzer with provider flag

### Data (Study these)
- **paper1.txt, paper2.txt, paper3.txt** → Example papers
- **analysis_prompt.txt** → Example prompt

### Configuration (Set up once, then ignore)
- **.env.template** → Template for your .env file
- **.env** → Your actual configuration (NEVER commit)
- **requirements.txt** → What to pip install
- **.gitignore** → What NOT to commit to Git

## 🔄 Typical Usage Flow

### First Time (30 minutes)
```
1. Read QUICKSTART.md
2. Follow setup steps (API keys, .env)
3. Run: python src/llm_paper_analyzer.py
4. Run: python src/llm_paper_analyzer.py --provider openrouter
5. See output printed and saved
```

### Learning Deeply (2-3 hours)
```
1. Read README.md
2. Read PROMPT_ENGINEERING_GUIDE.md
3. Examine analysis_prompt.txt line-by-line
4. Run examples and see exactly what they do
5. Modify prompt slightly and re-run
6. Read comments in openai_example.py
```

### Practical Use (ongoing)
```
1. Add your papers to examples/papers/
2. Create custom prompts for your needs
3. Run analysis scripts
4. Iterate on prompts based on results
5. Save good prompts for reuse
```

### Production Scaling (when needed)
```
1. Read ADVANCED_TOPICS.md
2. Implement batch processing
3. Set up error handling
4. Monitor costs
5. Optimize model selection
```

## 📊 Size Reference

| Component | Size | Time to Read |
|-----------|------|--------------|
| README.md | ~4 KB | 15 min |
| QUICKSTART.md | ~3 KB | 5 min |
| PROJECT_OVERVIEW.md | ~7 KB | 10 min |
| setup_instructions.md | ~8 KB | 20 min |
| PROMPT_ENGINEERING_GUIDE.md | ~12 KB | 45 min |
| ADVANCED_TOPICS.md | ~10 KB | 60 min |
| **Total Documentation** | **~44 KB** | **~2.5 hours** |
| openai_example.py | ~3 KB | 10 min |
| openrouter_example.py | ~3 KB | 10 min |
| **Total Code** | **~6 KB** | **~20 min** |
| paper1.txt | ~5 KB | 10 min |
| paper2.txt | ~4 KB | 10 min |
| paper3.txt | ~4 KB | 10 min |
| analysis_prompt.txt | ~3 KB | 5 min |
| **Total Data** | **~16 KB** | **~35 min** |
| **COMPLETE PACKAGE** | **~66 KB** | **~3 hours** |

## ✅ Checklist: Did I Get Everything?

After cloning/downloading, verify you have:

### Documentation Files
- [ ] README.md
- [ ] QUICKSTART.md
- [ ] PROJECT_OVERVIEW.md (this file)
- [ ] setup_instructions.md
- [ ] PROMPT_ENGINEERING_GUIDE.md
- [ ] ADVANCED_TOPICS.md

### Python Scripts
- [ ] openai_example.py
- [ ] openrouter_example.py

### Configuration
- [ ] requirements.txt
- [ ] .env.template
- [ ] .gitignore

### Data
- [ ] examples/papers/paper1.txt
- [ ] examples/papers/paper2.txt
- [ ] examples/papers/paper3.txt
- [ ] examples/prompts/analysis_prompt.txt

If anything is missing, you might not have the complete package. Check with instructor or re-download.

## 🎓 Recommended Reading Order

**Minimum (to get working):**
1. QUICKSTART.md
2. Run examples

**Standard (to understand thoroughly):**
1. QUICKSTART.md
2. README.md
3. setup_instructions.md (troubleshoot as needed)
4. Run examples
5. PROMPT_ENGINEERING_GUIDE.md

**Complete (to become expert):**
1. All items in "Standard" path
2. ADVANCED_TOPICS.md
3. PROMPT_ENGINEERING_GUIDE.md deep dive
4. Modify and experiment with prompts
5. Build your own analysis scripts

---

## Quick Links

| Need | Go To |
|------|-------|
| Want to run it NOW | [QUICKSTART.md](QUICKSTART.md) |
| Want overview | [README.md](README.md) |
| Having setup issues | [setup_instructions.md](setup_instructions.md#troubleshooting-quick-fixes) |
| Want to learn prompting | [PROMPT_ENGINEERING_GUIDE.md](PROMPT_ENGINEERING_GUIDE.md) |
| Ready to scale | [ADVANCED_TOPICS.md](ADVANCED_TOPICS.md) |
| Understanding structure | [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) (you're reading it!) |

---

**You now have everything you need to analyze research papers with AI!** 🎉

Start with QUICKSTART.md and run the examples. Then decide which learning path fits your goals.

Good luck! 🚀
