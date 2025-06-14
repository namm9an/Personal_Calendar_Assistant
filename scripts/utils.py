import os
import sys
from pathlib import Path

def setup_python_path():
    """Add project root to Python path."""
    project_root = str(Path(__file__).parent.parent)
    if project_root not in sys.path:
        sys.path.insert(0, project_root) 