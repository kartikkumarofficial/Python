@echo off
REM === Force Anaconda Python ===
set ANACONDA_PY=C:\ProgramData\anaconda3\python.exe

REM === Your notebook directory ===
set NOTEBOOK_DIR=C:\files\programming\Python\2025\jupyter

REM === Change to notebook directory ===
cd /d "%NOTEBOOK_DIR%"

REM === Launch Jupyter Notebook using Anaconda ===
"%ANACONDA_PY%" -m notebook

pause
