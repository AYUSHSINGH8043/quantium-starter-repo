#!/usr/bin/env bash

# Exit immediately if a command fails
set -e

# Activate virtual environment
if [ -d "venv" ]; then
  source venv/bin/activate
else
  echo "Virtual environment not found"
  exit 1
fi

# Run test suite
pytest

# If pytest succeeds, exit 0
exit 0
