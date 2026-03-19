#!/bin/bash
# Virtual Environment Setup Script for Windows PowerShell

# Navigate to project directory
cd "c:\Central AI Research\AI-Tech-Exploration-Sandbox\hacknpulse"

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Green
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Green
. .\venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Green
python -m pip install --upgrade pip

# Install requirements
Write-Host "Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

# Verify installation
Write-Host "`nVerifying installation..." -ForegroundColor Green
python -c "import autogen; import openai; import fastapi; print('✅ All dependencies installed successfully!')"

Write-Host "`n✅ Virtual environment setup complete!" -ForegroundColor Green
Write-Host "Activated virtual environment at: $(Get-Location)\venv" -ForegroundColor Cyan
