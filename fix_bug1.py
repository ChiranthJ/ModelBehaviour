#!/usr/bin/env python3
"""
Fix for Bug 1: Variable Name Conflict in Upsampling Notebook

Problem: The variable 'upsampled' is used for both the upsampled dataset 
and the fitted LogisticRegression model, causing confusion and potential errors.

Fix: Rename the model variable to 'logistic_model' to avoid confusion.
"""

import re

def fix_upsampling_notebook():
    """Fix the variable name conflict in the upsampling notebook"""
    
    # Read the original file
    with open('Upsampling Minority Classes.ipynb', 'r') as f:
        content = f.read()
    
    # Fix the variable name conflict
    # Replace 'upsampled = LogisticRegression' with 'logistic_model = LogisticRegression'
    content = re.sub(
        r'upsampled = LogisticRegression\(solver=\'liblinear\'\)\.fit\(x_train, y_train\)',
        'logistic_model = LogisticRegression(solver=\'liblinear\').fit(x_train, y_train)',
        content
    )
    
    # Replace 'upsampled_pred = upsampled.predict(x_test)' with 'upsampled_pred = logistic_model.predict(x_test)'
    content = re.sub(
        r'upsampled_pred = upsampled\.predict\(x_test\)',
        'upsampled_pred = logistic_model.predict(x_test)',
        content
    )
    
    # Write the fixed content back
    with open('Upsampling Minority Classes_fixed.ipynb', 'w') as f:
        f.write(content)
    
    print("Bug 1 fixed: Variable name conflict resolved in upsampling notebook")
    print("Original file preserved, fixed version saved as 'Upsampling Minority Classes_fixed.ipynb'")

if __name__ == "__main__":
    fix_upsampling_notebook()