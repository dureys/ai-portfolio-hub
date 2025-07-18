# GPU Acceleration Setup Guide

## Prerequisites
- NVIDIA GPU with CUDA support
- Windows 11 with WSL2 (optional)
- At least 16GB RAM (32GB recommended)

## Installation Steps

### 1. Install NVIDIA Drivers
- Download latest drivers from nvidia.com
- Ensure CUDA 12.x compatibility

### 2. Install Ollama with GPU Support
\\\powershell
winget install Ollama.Ollama
\\\

### 3. Configure GPU Acceleration
\\\powershell
$env:CUDA_VISIBLE_DEVICES = "0"
ollama serve
\\\

### 4. Verify GPU Usage
\\\powershell
nvidia-smi
ollama run deepseek-coder:6.7b "test gpu acceleration"
\\\

## Performance Benchmarks
- 1.3B model: < 5 seconds
- 6.7B model: 10-30 seconds  
- 33B model: 30-60 seconds

## Troubleshooting
- If GPU not detected: Restart Ollama service
- If slow responses: Check nvidia-smi for utilization
- If CUDA errors: Verify driver compatibility
