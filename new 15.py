import streamlit as st
from io import StringIO

st.set_page_config(page_title="Security Demo — Harmless", page_icon="🔒", layout="centered")
st.title("🔒 Security Demo — Harmless & With Consent")
st.write("This is a **safe** interview demo. It shows a banner and lets you download a benign proof file.")

# Big banner
st.markdown(
    """<div style="padding:16px;border-radius:12px;background:#ffe4e6;color:#991b1b;
    font-weight:700;">You have been hacked. (Demo)</div>""",
    unsafe_allow_html=True
)

payload = """This is a harmless demo file.
Proof token: DEMO-PROOF-2025-XYZ
Created by: [Your Name] — for interview demo only.
"""

# Download button (user-initiated; browsers will allow)
st.download_button(
    label="⬇️ Download proof file",
    data=payload.encode("utf-8"),
    file_name="demo-proof.txt",
    mime="text/plain",
    use_container_width=True
)

with st.expander("Preview file contents"):
    st.code(payload, language="text")
