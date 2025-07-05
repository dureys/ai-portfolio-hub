# 🤖 AI COLLABORATION PROTOCOL

## SHARED WORKSPACE: GitHub Repository
**Repository**: https://github.com/dureys/ai-portfolio-hub
**Access**: Public (for AI reading) + Private sessions (for context)

## COLLABORATION WORKFLOW

### 1. Local Development (You)
- Work in VS Code with local AI models
- Make changes and commit frequently
- Push to GitHub immediately after major progress

### 2. Claude Assistance (AI Review & Guidance)
- **READ**: Repository state via GitHub URL
- **PROVIDE**: Architecture guidance, code review, problem-solving
- **CONTEXT**: Always check latest commit and AI_CONTEXT.md
- **NO DIRECT COMMITS**: Claude provides guidance, you implement

### 3. Replit Development (Live Testing)
- **IMPORT**: GitHub repository into Replit
- **SYNC**: Pull latest changes before starting work
- **TEST**: Live demos and deployment
- **PUSH**: Changes back to GitHub

## SESSION HANDOFF PROTOCOL

### Starting New Session with Claude
1. **Share Repository URL**: https://github.com/dureys/ai-portfolio-hub
2. **Reference Context**: "Please read AI_CONTEXT.md and current-state.md"
3. **Current Task**: Always specified in current-state.md
4. **Last Commit**: Check latest commit message for progress

### Working with Replit
1. **Import from GitHub**: Use repository URL
2. **Create new branch**: For experimental features
3. **Merge via GitHub**: Review changes before merging to main

## FILE PRIORITIES FOR AI READING
1. **AI_CONTEXT.md** - Current project status
2. **.ai-sessions/current-state.md** - Exact task state
3. **README.md** - Overall project overview
4. **Latest commit messages** - Recent progress
5. **Specific project folders** - Current work area

## COMMIT MESSAGE PROTOCOL
- **Progress**: "🔄 WIP: Building AutoGen CRM agents"
- **Completion**: "✅ COMPLETE: AutoGen CRM demo working"  
- **Ready for AI**: "🤖 READY: Need Claude review of architecture"
- **Blocked**: "⚠️ BLOCKED: Need help with Streamlit deployment"

## REPLIT COLLABORATION SETUP
- **Main Repository**: Keep in sync with GitHub
- **Live Development**: Test and iterate quickly
- **Demo Deployment**: Share live links for feedback
- **Branch Strategy**: Use branches for experimental features
