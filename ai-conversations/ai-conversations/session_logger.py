import datetime
import json
import os

class AISessionLogger:
    def __init__(self):
        self.session_file = "ai-conversations/session_log.json"
        self.ensure_file_exists()
        
    def ensure_file_exists(self):
        if not os.path.exists(self.session_file):
            with open(self.session_file, 'w') as f:
                json.dump([], f)
    
    def log_interaction(self, ai_name, task, outcome, files_modified=None):
        """Log every AI interaction for future reference"""
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "ai_assistant": ai_name,
            "task_description": task,
            "outcome": outcome,
            "files_modified": files_modified or [],
            "session_context": "ai-portfolio-hub development"
        }
        
        # Read existing logs
        with open(self.session_file, 'r') as f:
            logs = json.load(f)
        
        # Add new entry
        logs.append(entry)
        
        # Save updated logs
        with open(self.session_file, 'w') as f:
            json.dump(logs, f, indent=2)
    
    def get_recent_context(self, hours=24):
        """Get recent AI interactions for context"""
        with open(self.session_file, 'r') as f:
            logs = json.load(f)
        
        cutoff = datetime.datetime.now() - datetime.timedelta(hours=hours)
        recent = [log for log in logs 
                 if datetime.datetime.fromisoformat(log['timestamp']) > cutoff]
        return recent

# Usage example
logger = AISessionLogger()
logger.log_interaction(
    "Claude", 
    "Complete persistent AI environment setup", 
    "In progress - setting up model hierarchy and AI collaboration system"
)