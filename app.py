import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="행복MAX 점심시간",
    page_icon="🍚",
    layout="centered",
)

LOGO_PATH = Path(__file__).parent / "cosmaxlogo.png"
LOGO_B64 = base64.b64encode(LOGO_PATH.read_bytes()).decode() if LOGO_PATH.exists() else ""

AVATAR_EMOJIS = ["🧑", "👩", "🧑‍💻", "👨‍🍳", "🙋‍♀️", "🧑‍🎨"]
AVATAR_COLORS = ["#FFE1B8", "#FFD1C7", "#D9F2E6", "#E4E1FF", "#FFF1B8", "#D8ECFF"]

st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

        .stApp, [data-testid="stAppViewContainer"] {{
            background-color: #FFF3E4;
            background-image:
                linear-gradient(180deg, rgba(255,246,235,0.93), rgba(255,238,219,0.93)),
                url("data:image/png;base64,{LOGO_B64}");
            background-repeat: no-repeat;
            background-position: center top, center 10%;
            background-size: cover, 1100px;
            background-attachment: fixed, fixed;
        }}
        .block-container {{padding-top: 1rem; padding-bottom: 2rem;}}
        .stamp {{
            display: inline-block;
            padding: 6px 18px;
            border-radius: 999px;
            background: #FF7A59;
            color: white;
            font-weight: 700;
            font-size: 13px;
            box-shadow: 0 6px 14px rgba(233,87,63,0.35);
            margin-bottom: 14px;
        }}
        .hero {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .hero img {{
            display: block;
            margin: 0 auto;
        }}
        .hero h1 {{
            font-family: 'Jua', sans-serif;
            font-size: 34px;
            color: #3B2A1F;
        }}
        .hero-caption {{
            color: rgba(59, 42, 31, 0.6);
            font-size: 0.9rem;
            line-height: 1.5;
        }}
        .section-label {{
            font-weight: 700;
            font-size: 16px;
            color: #8B2E2E;
            margin: 20px 0 10px 0;
        }}
        .member-avatar-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
        }}
        .member-avatar {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 16px;
            flex-shrink: 0;
        }}
        .member-avatar-label {{
            font-weight: 700;
            font-size: 14px;
            color: #3B2A1F;
        }}
        div[class*="st-key-member_card_"] {{
            background: #FFFFFF;
            border-radius: 20px !important;
            border-color: rgba(139, 118, 99, 0.15) !important;
            box-shadow: 0 8px 20px rgba(139, 45, 45, 0.08);
            padding: 8px 4px;
        }}
        div[class*="st-key-member_tags_"] button {{
            border-radius: 999px !important;
            font-weight: 700 !important;
            font-size: 12px !important;
        }}
        div[class*="st-key-member_tags_"] button[aria-pressed="true"],
        div[class*="st-key-member_tags_"] button[aria-checked="true"] {{
            background-color: #2FAE96 !important;
            border-color: #2FAE96 !important;
            color: white !important;
        }}
        .st-key-add_member_btn button {{
            background: transparent !important;
            border: 2px dashed rgba(255, 122, 89, 0.5) !important;
            color: #FF7A59 !important;
            font-weight: 700 !important;
            border-radius: 14px !important;
        }}
        .st-key-recommend_btn button {{
            background: linear-gradient(135deg, #FF7A59, #E9573F) !important;
            border: none !important;
            border-radius: 999px !important;
            font-weight: 800 !important;
            font-size: 17px !important;
            padding: 14px 0 !important;
            box-shadow: 0 10px 24px rgba(233, 87, 63, 0.35);
            position: relative;
        }}
        .st-key-recommend_btn button::before,
        .st-key-recommend_btn button::after {{
            content: "";
            position: absolute;
            top: 50%;
            width: 18px;
            height: 18px;
            background: #FFF3E4;
            border-radius: 50%;
            transform: translateY(-50%);
        }}
        .st-key-recommend_btn button::before {{ left: -9px; }}
        .st-key-recommend_btn button::after {{ right: -9px; }}
        .st-key-result_card {{
            text-align: center;
            border-radius: 20px !important;
            box-shadow: 0 8px 20px rgba(139, 45, 45, 0.08);
        }}
        .result-badge {{
            color: #2FAE96;
            font-weight: 700;
            font-size: 12px;
        }}
        .result-title {{
            font-family: 'Jua', sans-serif;
            font-size: 22px;
            color: #3B2A1F;
            margin-top: 6px;
        }}
        .result-stars {{
            margin-top: 6px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

TAG_OPTIONS = ["한식", "중식", "일식", "양식", "분식", "아시안", "맵게"]
RESTAURANTS = [
    {"name": "역전할머니맥주 분당판교역점", "menu": "치즈라볶이", "tags": ["분식", "맵게"], "address": "경기 성남시 분당구 판교역로192번길 14-2", "distanceM": 450, "walkMin": 6, "rating": 3.9, "catchtable": False},
    {"name": "마라공방 판교점", "menu": "마라탕", "tags": ["중식", "맵게"], "address": "경기 성남시 분당구 판교역로192번길 12 2층", "distanceM": 430, "walkMin": 6, "rating": 4.3, "catchtable": False},
    {"name": "르메콩", "menu": "소고기쌀국수", "tags": ["아시안"], "address": "경기 성남시 분당구 대왕판교로 670 유스페이스2(B동) 2층 218호", "distanceM": 900, "walkMin": 12, "rating": 4.6, "catchtable": False},
    {"name": "여의나룻", "menu": "한우탕", "tags": ["한식"], "address": "경기 성남시 분당구 분당내곡로 131 판교테크원 2층", "distanceM": 1100, "walkMin": 14, "rating": 4.4, "catchtable": False},
    {"name": "해미옥", "menu": "해물칼국수", "tags": ["한식"], "address": "경기 성남시 분당구 대왕판교로606번길 41 지하1층 B01호", "distanceM": 650, "walkMin": 9, "rating": 4.2, "catchtable": False},
    {"name": "카츠쇼쿠도우", "menu": "로스카츠 정식", "tags": ["일식"], "address": "경기 성남시 분당구 판교역로 152 알파돔타워3 지하1층 9호", "distanceM": 480, "walkMin": 6, "rating": 4.5, "catchtable": False},
    {"name": "신승반점 현대백화점판교점", "menu": "유니짜장", "tags": ["중식"], "address": "경기 성남시 분당구 판교역로146번길 20 현대백화점 판교점 지하1층", "distanceM": 500, "walkMin": 7, "rating": 4.6, "catchtable": True},
    {"name": "매드포갈릭 판교라스트리트점", "menu": "로제파스타", "tags": ["양식"], "address": "경기 성남시 분당구 대왕판교로606번길 10 알파리움타워 1동 2층", "distanceM": 600, "walkMin": 8, "rating": 4.2, "catchtable": True},
    {"name": "청년다방 판교테크노밸리점", "menu": "불향차돌떡볶이", "tags": ["분식", "맵게"], "address": "경기 성남시 분당구 대왕판교로 660 유스페이스1 A동 206호", "distanceM": 900, "walkMin": 12, "rating": 4.3, "catchtable": False},
    {"name": "영심이떡볶이&김밥 판교2호점", "menu": "떡볶이", "tags": ["분식"], "address": "경기 성남시 분당구 대왕판교로606번길 45 판교역 푸르지오시티", "distanceM": 550, "walkMin": 7, "rating": 4.0, "catchtable": False},
]


def render_stars(rating: float) -> str:
    full = round(rating)
    return "⭐" * full + "☆" * (5 - full) + f" {rating:.1f}"


def map_search_url(restaurant: dict) -> str:
    return f"https://map.kakao.com/?q={restaurant['name']} {restaurant['address']}"


def reservation_info(restaurant: dict) -> tuple[str, str]:
    query = restaurant["name"]
    if restaurant["catchtable"]:
        return (
            f"https://app.catchtable.co.kr/ct/map/COMMON?showTabs=true&serviceType=INTEGRATION&keyword={query}&keywordSearch={query}&bottomSheetHeightType=HALF",
            "캐치테이블에서 예약하기",
        )
    return (f"https://map.naver.com/p/search/{query}", "네이버 플레이스에서 보기")


def initialize_members() -> None:
    if "members" not in st.session_state:
        st.session_state.members = [
            {"name": "", "yesterday": "", "tags": []},
            {"name": "", "yesterday": "", "tags": []},
        ]
    if "recommendation" not in st.session_state:
        st.session_state.recommendation = None


initialize_members()

logo_html = f'<img src="data:image/png;base64,{LOGO_B64}" width="220" />' if LOGO_B64 else ""

st.markdown(
    f"""
    <div class="hero">
        {logo_html}
        <div class="stamp">센스MAX 신입사원 인증</div>
        <h1>행복<span style='color:#FF8166'>MAX</span> 점심시간</h1>
        <p class="hero-caption">전날 먹은 메뉴와 취향을 입력하면, 판교 근처에서 팀원 모두가 만족할 메뉴를 찾아드려요.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='section-label'>🍚 팀원별 정보 입력</div>", unsafe_allow_html=True)

for idx, member in enumerate(st.session_state.members):
    with st.container(border=True, key=f"member_card_{idx}"):
        col1, col2 = st.columns([6, 1])
        with col1:
            avatar_emoji = AVATAR_EMOJIS[idx % len(AVATAR_EMOJIS)]
            avatar_color = AVATAR_COLORS[idx % len(AVATAR_COLORS)]
            st.markdown(
                f"""
                <div class="member-avatar-row">
                    <span class="member-avatar" style="background:{avatar_color};">{avatar_emoji}</span>
                    <span class="member-avatar-label">팀원 {idx + 1} 이름 (선택)</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            member_name = st.text_input(
                f"팀원 {idx + 1} 이름",
                value=member.get("name", ""),
                key=f"member_name_{idx}",
                label_visibility="collapsed",
                placeholder="이름을 입력해주세요",
            )
        with col2:
            if st.button("✕", key=f"remove_member_{idx}", use_container_width=True):
                st.session_state.members.pop(idx)
                st.rerun()

        member_yesterday = st.text_input(
            "전날 먹은 메뉴",
            value=member.get("yesterday", ""),
            key=f"member_yesterday_{idx}",
            placeholder="예: 삼겹살, 김치찌개",
        )
        member_tags = st.pills(
            "취향 태그",
            TAG_OPTIONS,
            selection_mode="multi",
            default=member.get("tags", []),
            key=f"member_tags_{idx}",
        )

        st.session_state.members[idx]["name"] = member_name
        st.session_state.members[idx]["yesterday"] = member_yesterday
        st.session_state.members[idx]["tags"] = member_tags

if st.button("＋ 팀원 추가하기", use_container_width=True, key="add_member_btn"):
    st.session_state.members.append({"name": "", "yesterday": "", "tags": []})
    st.rerun()

if st.button("오늘의 메뉴 추천받기", type="primary", use_container_width=True, key="recommend_btn"):
    yesterday_menus = [m.get("yesterday", "").strip() for m in st.session_state.members if m.get("yesterday", "").strip()]
    tag_count = {}
    for member in st.session_state.members:
        for tag in member.get("tags", []):
            tag_count[tag] = tag_count.get(tag, 0) + 1

    candidates = [r for r in RESTAURANTS if not any(y in r["menu"] or r["menu"] in y for y in yesterday_menus)]
    pool = candidates if candidates else RESTAURANTS

    best = pool[0]
    best_score = -1
    for restaurant in pool:
        score = sum(tag_count.get(tag, 0) for tag in restaurant["tags"])
        if score > best_score:
            best_score = score
            best = restaurant

    st.session_state.recommendation = {
        "restaurant": best,
        "best_score": best_score,
        "yesterday_menus": yesterday_menus,
    }

if st.session_state.recommendation:
    recommendation = st.session_state.recommendation
    restaurant = recommendation["restaurant"]
    with st.container(border=True, key="result_card"):
        st.markdown("<div class='result-badge'>오늘의 추천 도착!</div>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='result-title'>{restaurant['name']} · {restaurant['menu']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(f"<div class='result-stars'>{render_stars(restaurant['rating'])}</div>", unsafe_allow_html=True)
        if recommendation["best_score"] > 0:
            st.caption(f"팀원 취향 태그와 {recommendation['best_score']}건 일치했어요")
        else:
            st.caption("전날 메뉴를 제외하고 골라봤어요")
        st.link_button("📍 주소 보기", map_search_url(restaurant), use_container_width=True)
        st.caption(f"🚶 코스맥스 본사에서 도보 약 {restaurant['walkMin']}분 ({restaurant['distanceM']}m)")
        reserve_url, reserve_label = reservation_info(restaurant)
        st.link_button(reserve_label, reserve_url, use_container_width=True)

st.markdown("<div style='text-align:center; margin-top:36px; color:#8B7663; font-size:11px;'>코맥인들의 슬기로운 점심시간을 위하여</div>", unsafe_allow_html=True)
