# Code Quality with flake8

This project uses flake8 for automated Python code quality checks.

## Quick Start

### Run Code Quality Checks

```bash
# Check all code
make lint

# Auto-fix common issues
make lint-fix

# Run all checks (lint + tests)
make check-all
```

## Setup Details

### Installed Tools

- **flake8**: Main linting tool for Python code quality
- **flake8-django**: Django-specific linting rules
- **autopep8**: Automatic code formatting to fix common issues

### Configuration

- **`.flake8`**: Main configuration file with project-specific rules
- **`.vscode/settings.json`**: VS Code integration for real-time linting
- **`.github/workflows/ci.yml`**: Automated checks on GitHub

### Current Rules

- **Max line length**: 88 characters (Black-compatible)
- **Excluded directories**: migrations, staticfiles, .venv, **pycache**
- **Ignored errors**:
  - E203: whitespace before ':' (conflicts with black)
  - W503: line break before binary operator (old PEP 8 style)

## VS Code Integration

The project is configured to:

- Show flake8 errors/warnings in real-time
- Auto-format Python files on save using autopep8
- Organize imports automatically

## Manual Commands

### Basic Usage

```bash
# Run flake8 on entire project
flake8

# Check specific file
flake8 myapp/views.py

# Show statistics
flake8 --statistics

# Count errors by type
flake8 --count --statistics
```

### Auto-fixing

```bash
# Fix formatting issues automatically
autopep8 --in-place --recursive --aggressive --aggressive --max-line-length=88 .

# Fix specific file
autopep8 --in-place --aggressive --aggressive --max-line-length=88 myfile.py
```

## Current Status

✅ **Resolved Issues:**

- Removed unused imports
- Fixed whitespace and blank line issues
- Added proper spacing around operators
- Fixed function/class definition spacing

⚠️ **Remaining Issues:**

- Some long lines in forms.py and views.py (design decision for readability)
- These are acceptable and documented in the configuration

## Integration with Git

### Pre-commit Checks

A pre-commit script is available at `scripts/pre-commit-check.py`:

```bash
# Run pre-commit checks manually
python scripts/pre-commit-check.py
```

### GitHub Actions

Automated checks run on:

- Push to main/develop branches
- Pull requests to main branch

## Best Practices

1. **Run checks before committing:**

   ```bash
   make check-all
   ```

2. **Fix issues automatically when possible:**

   ```bash
   make lint-fix
   ```

3. **Use VS Code for real-time feedback** - errors will appear as you type

4. **Long lines**: Break at logical points:

   ```python
   # Bad
   very_long_function_call_with_many_parameters(param1, param2, param3, param4, param5)

   # Good
   very_long_function_call_with_many_parameters(
       param1, param2, param3,
       param4, param5
   )
   ```

## Customization

To modify rules, edit `.flake8`:

```ini
[flake8]
max-line-length = 88
ignore = E203,W503
exclude = migrations,staticfiles
```

## Troubleshooting

### Common Issues

1. **"flake8: command not found"**

   ```bash
   pip install flake8 flake8-django
   ```

2. **VS Code not showing errors**

   - Check that Python extension is installed
   - Verify Python interpreter is set correctly
   - Restart VS Code

3. **Too many line length errors**
   - Run `make lint-fix` to auto-fix what's possible
   - Manually break long lines at logical points

### Getting Help

- Check flake8 documentation: https://flake8.pycqa.org/
- Django-specific rules: https://github.com/rocioar/flake8-django
