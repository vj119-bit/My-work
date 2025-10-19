import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Security Demo — Harmless", page_icon="🔒")
st.title("🔒 Security Demo — Harmless & With Consent")
st.write("This is a **safe** interview demo. Click the link below (consent required) to download a benign proof file.")

payload = """This is a harmless demo file.
Proof token: DEMO-PROOF-2025-XYZ
Created by: [Your Name] — for interview demo only.
"""

# Show a big banner (demo)
st.markdown(
    """<div style="padding:16px;border-radius:12px;background:#ffe4e6;color:#991b1b;
    font-weight:700;">You have been hacked. (Demo)</div>""",
    unsafe_allow_html=True
)

st.write("**Click this link to start the download immediately:**")

# The HTML below creates a clickable link that builds a Blob and triggers a download.
# This runs inside an iframe (component) and uses a user click to allow the browser to download.
html = f"""
<div>
  <a id="downloadLink" href="#" style="font-weight:700; text-decoration:none; color:#1f6feb; cursor:pointer;">🔗 Click here to download proof file</a>
</div>
<script>
  const payload = {payload!r}; // safe JS string literal
  function triggerDownload(filename, text) {{
    const blob = new Blob([text], {{type: 'text/plain'}});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(()=> URL.revokeObjectURL(url), 3000);
  }}
  const link = document.getElementById('downloadLink');
  link.addEventListener('click', function(e) {{
    e.preventDefault();
    triggerDownload('demo-proof.txt', payload);
  }});
</script>
"""

# Render the HTML. The component runs the script in an iframe with script permission.
components.html(html, height=60)
st.caption("If the link doesn't work in a particular browser, use the Download button below as a fallback.")

# Fallback: Streamlit-native download (guaranteed)
st.download_button(
    label="⬇️ Fallback: Download proof file",
    data=payload.encode("utf-8"),
    file_name="demo-proof.txt",
    mime="text/plain",
    use_container_width=True
)

with st.expander("Preview file contents"):
    st.code(payload, language="text")
