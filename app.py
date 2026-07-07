import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# ── 기본 페이지 설정 ─────────────────────────────────────────
st.set_page_config(
    page_title="행복MAX 점심시간",
    page_icon="🍚",
    layout="centered",
)

# Streamlit 기본 여백/헤더를 최소화해서 원본 HTML 디자인이
# 화면을 그대로 채우도록 함
st.markdown(
    """
    <style>
        .block-container {padding-top: 0rem; padding-bottom: 0rem;}
        header[data-testid="stHeader"] {background: transparent;}
        iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).parent
HTML_PATH = BASE_DIR / "lunchchooser.html"
LOGO_PATH = BASE_DIR / "cosmaxlogo.png"


@st.cache_data
def load_html() -> str:
    """lunchchooser.html을 읽고, 로고 이미지를 base64 data URI로 치환해서 반환.

    Streamlit Cloud에서는 로컬 상대경로(cosmaxlogo.png)로 이미지를 불러올 수
    없기 때문에, 이미지를 base64로 인코딩해 <img> src에 직접 심어준다.
    """
    html = HTML_PATH.read_text(encoding="utf-8")

    if LOGO_PATH.exists():
        logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
        data_uri = f"data:image/png;base64,{logo_b64}"
        html = html.replace('src="cosmaxlogo.png"', f'src="{data_uri}"')

    return html


html_content = load_html()

# 원본 HTML/CSS/JS를 그대로 iframe에 렌더링
components.html(html_content, height=1400, scrolling=True)
