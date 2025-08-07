#!/usr/bin/env python3
"""
Pre-commit hook script for Studio Bar Django project.
This script runs flake8 checks before allowing commits.
"""
import shutil
import subprocess  # nosec B404 - legitimate use for code quality checks
import sys


def run_flake8():
    """Run flake8 checks and return the result."""
    # Find full path to flake8 for security
    flake8_path = shutil.which('flake8')
    if not flake8_path:
        print("Error: flake8 not found. Please install it with: pip install flake8")
        return 1, "", "flake8 not found"
    
    try:
        # Use full path and explicit arguments for security
        result = subprocess.run([flake8_path], capture_output=True, text=True, shell=False, check=False)  # nosec B603 - secure subprocess call with full path
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        print(f"Error running flake8: {e}")
        return 1, "", str(e)


def main():
    """Main function to run pre-commit checks."""
    print("Running pre-commit checks...")

    # Run flake8
    print("Checking code style with flake8...")
    returncode, stdout, stderr = run_flake8()

    if returncode != 0:
        print("❌ Code style issues found:")
        print(stdout)
        if stderr:
            print("Errors:")
            print(stderr)
        print("\n💡 Fix issues by running: make lint-fix")
        print("Then run: git add . && git commit")
        sys.exit(1)

    print("✅ All pre-commit checks passed!")
    sys.exit(0)


if __name__ == "__main__":
    main()
