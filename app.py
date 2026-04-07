import sys
import os

_ROOT = os.path.dirname(os.path.abspath(__file__))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
_WEBAPP = os.path.join(_ROOT, "webapp")
if _WEBAPP not in sys.path:
    sys.path.insert(0, _WEBAPP)

try:
    from webapp.streamlit_app import main
    import streamlit as st
    st.write("✅ Import OK")
    st.write(f"Python: {sys.version}")
    import pandas as pd
    st.write(f"Pandas: {pd.__version__}")
    import altair as alt
    st.write(f"Altair: {alt.__version__}")
    st.write("Calling main()...")
    main()
except Exception as e:
    import traceback
    import streamlit as st
    st.error(f"ERROR: {e}")
    st.code(traceback.format_exc())
