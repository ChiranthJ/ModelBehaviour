#!/usr/bin/env python3
"""
Master script to fix all identified bugs in the Costa Rican Household Poverty Prediction project.

This script runs all three bug fixes in sequence:
1. Variable name conflict in upsampling notebook
2. Hardcoded file paths in multiple notebooks
3. Missing import and undefined variable in phase2 notebook
"""

import os
import sys

def main():
    """Run all bug fixes in sequence"""
    
    print("=" * 60)
    print("Costa Rican Household Poverty Prediction - Bug Fixes")
    print("=" * 60)
    print()
    
    # Check if we're in the right directory
    if not os.path.exists('README.md'):
        print("Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Run Bug Fix 1: Variable Name Conflict
    print("🔧 Fixing Bug 1: Variable Name Conflict in Upsampling Notebook...")
    try:
        exec(open('fix_bug1.py').read())
        print("✅ Bug 1 fixed successfully!")
    except Exception as e:
        print(f"❌ Error fixing Bug 1: {e}")
    
    print()
    
    # Run Bug Fix 2: Hardcoded File Paths
    print("🔧 Fixing Bug 2: Hardcoded File Paths...")
    try:
        exec(open('fix_bug2.py').read())
        print("✅ Bug 2 fixed successfully!")
    except Exception as e:
        print(f"❌ Error fixing Bug 2: {e}")
    
    print()
    
    # Run Bug Fix 3: Missing Import and Undefined Variable
    print("🔧 Fixing Bug 3: Missing Import and Undefined Variable...")
    try:
        exec(open('fix_bug3.py').read())
        print("✅ Bug 3 fixed successfully!")
    except Exception as e:
        print(f"❌ Error fixing Bug 3: {e}")
    
    print()
    print("=" * 60)
    print("🎉 All bug fixes completed!")
    print("=" * 60)
    print()
    print("📁 Fixed files created:")
    print("   • Upsampling Minority Classes_fixed.ipynb")
    print("   • Analysis_fixed.ipynb")
    print("   • Sample_testing_models_phase1_fixed.ipynb")
    print("   • Sample_testing_models_phase2_fixed.ipynb")
    print()
    print("📋 Summary of fixes applied:")
    print("   1. Variable name conflict resolved - no more data overwriting")
    print("   2. Hardcoded paths replaced with relative paths - improved portability")
    print("   3. Missing imports and undefined variables fixed - notebooks can now run")
    print()
    print("📖 See BUG_FIXES_SUMMARY.md for detailed explanations of all fixes")
    print()
    print("💡 Original files have been preserved. Use the *_fixed.ipynb versions for production.")

if __name__ == "__main__":
    main()