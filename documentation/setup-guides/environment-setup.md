# Complete Development Environment Setup

## Overview
This guide reproduces the complete AI development environment for the portfolio project.

## Required Tools
1. **Git & GitHub CLI**: Version control and repository management
2. **VS Code**: Primary development environment
3. **Python 3.11+**: Core programming language
4. **Ollama**: Local AI model serving
5. **AutoGen**: Multi-agent framework

## Installation Order

### 1. Core Tools
\\\powershell
# Install package manager
choco install chocolatey

# Install development tools
choco install git vscode nodejs python ollama github-cli -y
\\\

### 2. Python Packages
\\\powershell
pip install -r requirements.txt
\\\

### 3. AI Models
\\\powershell
ollama pull deepseek-coder:1.3b
ollama pull deepseek-coder:6.7b
ollama pull deepseek-coder:33b
\\\

### 4. VS Code Extensions
\\\powershell
code --install-extension Continue.continue
code --install-extension ms-python.python
code --install-extension GitHub.copilot
\\\

## Verification
\\\powershell
# Test AI models
ollama run deepseek-coder:6.7b "print('Environment ready!')"

# Test AutoGen
python -c "import autogen; print('AutoGen working!')"

# Test Streamlit
streamlit hello
\\\

## Performance Optimization
- Ensure GPU acceleration is enabled
- Use appropriate model sizes for tasks
- Configure Continue extension for model hierarchy
