# 🤖 CLAUDE COLLABORATION MARKERS

## Current Status Tags
- **🔄 IN_PROGRESS**: Currently working on task
- **🤖 NEED_CLAUDE**: Ready for Claude's architectural guidance  
- **✅ READY_REVIEW**: Code complete, need Claude review
- **⚠️ BLOCKED**: Stuck, need Claude's problem-solving help
- **🚀 DEPLOY_READY**: Ready for Replit deployment testing

## How to Use
1. **Update current-state.md** with appropriate tag
2. **Commit with tag in message**
3. **Claude reads repository** and provides targeted assistance
4. **Continue development** with Claude's guidance

## Example Workflow
# Tool: PowerShell
# Location: C:\Projects\ai-portfolio-hub\
# What: Create tags for Claude to understand project state
# Why: Clear signals for AI assistance needs

@"
# 🤖 CLAUDE COLLABORATION MARKERS

## Current Status Tags
- **🔄 IN_PROGRESS**: Currently working on task
- **🤖 NEED_CLAUDE**: Ready for Claude's architectural guidance  
- **✅ READY_REVIEW**: Code complete, need Claude review
- **⚠️ BLOCKED**: Stuck, need Claude's problem-solving help
- **🚀 DEPLOY_READY**: Ready for Replit deployment testing

## How to Use
1. **Update current-state.md** with appropriate tag
2. **Commit with tag in message**
3. **Claude reads repository** and provides targeted assistance
4. **Continue development** with Claude's guidance

## Example Workflow  You: Work on AutoGen agents locally
You: Commit with "🤖 NEED_CLAUDE: Review multi-agent architecture"
Claude: Reads repo, provides architecture feedback
You: Implement suggestions, commit with "🔄 IN_PROGRESS: Implementing Claude's suggestions"
You: Complete feature, commit with "✅ READY_REVIEW: AutoGen CRM demo complete"
Claude: Reviews final implementation, suggests improvements
You: Deploy to Replit for live testing ## Repository Reading Instructions for Claude
**Repository URL**: https://github.com/dureys/ai-portfolio-hub
**Context Files**: 
- AI_CONTEXT.md (public project status)
- .ai-sessions/current-state.md (detailed task state)
- Latest commit messages (recent progress)
