import sys
import os
import traceback

_ROOT = os.path.dirname(os.path.abspath(__file__))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
_WEBAPP = os.path.join(_ROOT, "webapp")
if _WEBAPP not in sys.path:
    sys.path.insert(0, _WEBAPP)

try:
    from webapp.streamlit_app import main
    main()
except Exception as _e:
    # Surface the real error instead of showing a blank "oh no" screen
    try:
        import streamlit as st
        st.error(f"**App startup error:**\n\n```\n{traceback.format_exc()}\n```")
    except Exception:
        pass
    raise
