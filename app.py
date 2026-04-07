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

# Streamlit runs this file via exec() on every interaction rerun.
# Calling main() directly (instead of `import *`) ensures all st.* render
# calls execute every rerun — otherwise Python's module cache skips them
# and the page goes blank after the first interaction.
from webapp.streamlit_app import main  # noqa: E402
main()
