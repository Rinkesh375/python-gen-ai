# ==========================================
# pip install vs python -m pip install
# ==========================================

# 1. pip install <package>
#
# Example:
# pip install arrow
#
# - Runs the 'pip' executable found in your system PATH.
# - The operating system decides which pip to execute.
# - If multiple Python versions are installed, it may use the wrong pip.
# - Good to use when a virtual environment (venv) is activated.
#
# Flow:
# Terminal
#    ↓
# pip
#    ↓
# OS searches PATH
#    ↓
# First pip found
#    ↓
# Package installed


# 2. python -m pip install <package>
#
# Example:
# python -m pip install arrow
#
# - Runs the current Python interpreter first.
# - '-m' means "run a Python module".
# - Python executes its own pip module.
# - Guarantees the package is installed for the same Python
#   interpreter that is running your code.
# - Recommended and considered best practice.
#
# Flow:
# Terminal
#    ↓
# python
#    ↓
# Run pip module (-m pip)
#    ↓
# Package installed into THIS Python


# ==========================================
# Which one should I use?
# ==========================================
#
# pip install arrow
# ✔ Simpler
# ✔ Works well inside an activated virtual environment
# ✖ Can install into the wrong Python if multiple versions exist
#
# python -m pip install arrow
# ✔ Best Practice
# ✔ Uses the current Python interpreter
# ✔ Avoids version mismatches
# ✔ Recommended by most Python developers


# ==========================================
# JavaScript Analogy
# ==========================================
#
# npm install axios
#      ≈
# pip install arrow      (uses the available package manager)
#
# Activated venv
#      ≈
# Project's local node_modules
#
# python -m pip install arrow
#      ≈
# "Use the npm that belongs to THIS Node installation."
# (Not an exact Node.js command, but the same idea.)
#
# ==========================================
# Rule of Thumb
# ==========================================
#
# Inside an activated virtual environment:
#     pip install package
#     ✔ Safe
#
# When unsure which Python you're using:
#     python -m pip install package
#     ✔ Best Practice
#
# Remember:
# Trust the Python interpreter, not the pip command.