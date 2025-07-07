
#!/usr/bin/env python3
"""
Simple wrapper to run git summary agent
Usage: python gitsummary.py
"""
import subprocess
import sys
import os

def main():
    script_path = "ai-assistants/git-summary-agent/git_summary_agent.py"
    
    if not os.path.exists(script_path):
        print(f"Error: {script_path} not found!")
        sys.exit(1)
    
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running git summary agent: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
