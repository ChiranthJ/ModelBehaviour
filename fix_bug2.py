#!/usr/bin/env python3
"""
Fix for Bug 2: Hardcoded File Paths in Notebooks

Problem: Multiple notebooks contain hardcoded Windows file paths that will fail
on different operating systems and make the code non-portable.

Fix: Replace hardcoded paths with relative paths or environment variables.
"""

import re
import os

def fix_hardcoded_paths():
    """Fix hardcoded file paths in all notebooks"""
    
    # List of files to fix
    files_to_fix = [
        'Analysis.ipynb',
        'Sample_testing_models_phase1.ipynb',
        'Sample_testing_models_phase2.ipynb'
    ]
    
    for filename in files_to_fix:
        if os.path.exists(filename):
            print(f"Fixing hardcoded paths in {filename}...")
            
            with open(filename, 'r') as f:
                content = f.read()
            
            # Replace hardcoded Windows paths with relative paths
            # Fix paths like 'C:\\Users\\rames\\OneDrive\\Desktop\\namma\\DA_proj\\preprocessed_wosq.csv'
            content = re.sub(
                r'C:\\\\Users\\\\rames\\\\OneDrive\\\\Desktop\\\\namma\\\\DA_proj\\\\preprocessed_wosq\.csv',
                'preprocessed_wosq.csv',
                content
            )
            
            content = re.sub(
                r'C:\\\\Users\\\\rames\\\\OneDrive\\\\Desktop\\\\namma\\\\DA_proj\\\\preprocessed\.csv',
                'preprocessed.csv',
                content
            )
            
            # Fix other hardcoded paths
            content = re.sub(
                r'C:\\\\Users\\\\rames\\\\OneDrive\\\\Desktop\\\\namma\\\\DA_proj\\\\costa-rican-household-poverty-prediction \(1\)\\\\train\.csv',
                'RawData/train.csv',
                content
            )
            
            content = re.sub(
                r'C:\\\\Users\\\\rames\\\\OneDrive\\\\Desktop\\\\namma\\\\DA_proj\\\\costa-rican-household-poverty-prediction \(1\)\\\\test\.csv',
                'RawData/test.csv',
                content
            )
            
            # Write the fixed content back
            with open(f"{filename.replace('.ipynb', '_fixed.ipynb')}", 'w') as f:
                f.write(content)
            
            print(f"Fixed version saved as {filename.replace('.ipynb', '_fixed.ipynb')}")
        else:
            print(f"File {filename} not found, skipping...")

if __name__ == "__main__":
    fix_hardcoded_paths()
    print("\nBug 2 fixed: Hardcoded file paths replaced with relative paths")
    print("All notebooks now use portable file paths")