import sys
import os

# Ensure the project root is on the path so webapp.* imports resolve.
_ROOT = os.path.dirname(os.path.abspath(__file__))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

# Also ensure webapp/ is importable directly (for `from weekly_report_view import ...`)
_WEBAPP = os.path.join(_ROOT, "webapp")
if _WEBAPP not in sys.path:
    sys.path.insert(0, _WEBAPP)

# Streamlit runs this file via exec(), so __name__ != "__main__".
# We must NOT guard the import behind `if __name__ == "__main__"`.
# Instead, execute the app module directly.
from webapp.streamlit_app import *  # noqa: F401, F403, E402
