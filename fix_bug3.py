#!/usr/bin/env python3
"""
Fix for Bug 3: Missing Import and Undefined Variable in Phase2 Notebook

Problem: The notebook tries to import from a non-existent module and uses an undefined variable 'df'.

Fix: Remove the problematic import and fix the undefined variable reference.
"""

import re

def fix_phase2_notebook():
    """Fix the missing import and undefined variable in phase2 notebook"""
    
    # Read the original file
    with open('Sample_testing_models_phase2.ipynb', 'r') as f:
        content = f.read()
    
    # Fix 1: Remove the problematic import line
    # Remove: from ipynb.fs.full.PCA_analysis import *
    content = re.sub(
        r'#!pip install ipynb\nfrom ipynb\.fs\.full\.PCA_analysis import \*',
        '# PCA analysis functions will be defined inline or imported from local files',
        content
    )
    
    # Fix 2: Fix the undefined variable 'df' to 'processeddata'
    # Change: zero_cols = [ col for col, is_zero in ((df == 0).sum() == df.shape[0]).items() if is_zero ]
    # To: zero_cols = [ col for col, is_zero in ((processeddata == 0).sum() == processeddata.shape[0]).items() if is_zero ]
    content = re.sub(
        r'zero_cols = \[ col for col, is_zero in \(\(df == 0\)\.sum\(\) == df\.shape\[0\]\)\.items\(\) if is_zero \]',
        'zero_cols = [ col for col, is_zero in ((processeddata == 0).sum() == processeddata.shape[0]).items() if is_zero ]',
        content
    )
    
    # Write the fixed content back
    with open('Sample_testing_models_phase2_fixed.ipynb', 'w') as f:
        f.write(content)
    
    print("Bug 3 fixed: Missing import removed and undefined variable fixed in phase2 notebook")
    print("Original file preserved, fixed version saved as 'Sample_testing_models_phase2_fixed.ipynb'")

if __name__ == "__main__":
    fix_phase2_notebook()