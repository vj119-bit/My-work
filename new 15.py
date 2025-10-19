import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cybersecurity Demo — Harmless", page_icon="🔒", layout="centered")
st.title("🔒 Security Demo — Harmless & With Consent")
st.write("Don’t worry, this is a simple, harmless file that won’t cause any issues")

# ---- harmless payload ----
payload = """This is a harmless demo file.
Proof token: DEMO-PROOF-2025-XYZ
Created by: Vj.
"""

# Big banner
st.markdown(
    """<div style="padding:16px;border-radius:12px;background:#ffe4e6;color:#991b1b;
    font-weight:700;">You have been hacked.</div>""",
    unsafe_allow_html=True
)

# URL param to force the attempt (optional): ?dl=1
force_dl = st.query_params.get("dl", ["0"])
force_dl = (force_dl[0] if isinstance(force_dl, list) else force_dl) in ("1", "true", "yes")

# Only try once per session to avoid repeated auto-download attempts on reruns
if "dl_fired" not in st.session_state:
    st.session_state.dl_fired = False

should_try_auto = (not st.session_state.dl_fired) or force_dl

if should_try_auto:
    # Mark as fired so refreshes/reruns don't re-trigger
    st.session_state.dl_fired = True

    # Use a tiny HTML+JS component to trigger the download on page load.
    # This may be blocked by browser policies (expected).
    html = f"""
    <div id="auto-dl" style="height:1px; overflow:hidden;"></div>
    <script>
      const payload = {payload!r};
      function triggerDownload(filename, text) {{
        try {{
          const blob = new Blob([text], {{type: 'text/plain'}});
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url; a.download = filename;
          document.body.appendChild(a);
          a.click();
          a.remove();
          setTimeout(()=> URL.revokeObjectURL(url), 3000);
        }} catch (e) {{
          console.error('Download blocked or failed:', e);
        }}
      }}
      // Attempt immediately on load:
      window.addEventListener('load', () => {{
        triggerDownload('demo-proof.txt', payload);
      }});
    </script>
    """
    # Render the component (1px tall, effectively invisible)
    components.html(html, height=1)

st.divider()

# Fallback: guaranteed, user-initiated download button
st.download_button(
    label="⬇️ Download proof file (fallback)",
    data=payload.encode("utf-8"),
    file_name="demo-proof.txt",
    mime="text/plain",
    use_container_width=True
)

with st.expander("Preview file contents"):
    st.code(payload, language="text")

st.caption("Tip: If auto-download didn’t trigger, try clicking the button above or open the link with '?dl=1' appended (e.g., https://my-work-vj.streamlit.app/?dl=1).")


