#!/usr/bin/env python3
"""
Pre-commit hook script for Studio Bar Django project.
This script runs flake8 checks before allowing commits.
"""
import subprocess
import sys


def run_flake8():
    """Run flake8 checks and return the result."""
    try:
        result = subprocess.run(['flake8'], capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        print("Error: flake8 not found. Please install it with: pip install flake8")
        return 1, "", "flake8 not found"


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
