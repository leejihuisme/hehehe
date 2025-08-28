import streamlit as st

# 축구장 배경을 위한 스타일 설정
st.markdown("""
    <style>
    .soccer-field {
        background-color: #2e8b57;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid white;
    }
    .player {
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 15px;
        color: white;
    }
    .label {
        font-size: 0.9em;
        text-align: center;
        color: white;
        margin-top: -15px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚽️ 축구 포메이션 전략판")
st.markdown("---")

# 기본 포메이션 데이터 정의
formations = {
    "4-4-2": [4, 4, 2],
    "4-3-3": [4, 3, 3],
    "3-5-2": [3, 5, 2],
    "4-2-3-1": [4, 2, 3, 1]
}

# 사용자에게 포메이션 선택을 요청
selected_formation_name = st.selectbox(
    "원하는 포메이션을 선택하세요:",
    list(formations.keys())
)

st.write("")

# 선택된 포메이션에 따라 선수 수 설정
try:
    defense, midfield, attack = formations[selected_formation_name]
except ValueError:
    defense, holding_mid, attacking_mid, attack = formations[selected_formation_name]
    midfield = holding_mid + attacking_mid

# 축구장 컨테이너 시작
with st.container():
    st.markdown("<div class='soccer-field'>", unsafe_allow_html=True)
    
    # -------------------
    # 골키퍼 (GK)
    # -------------------
    gk_col = st.columns(1)[0]
    with gk_col:
        st.write("") # 공간 확보
        st.markdown("<div class='player'>🏃‍♂️</div>", unsafe_allow_html=True)
        st.markdown("<div class='label'>GK</div>", unsafe_allow_html=True)
        
    # -------------------
    # 공격수 (Attackers)
    # -------------------
    st.markdown("")
    attack_cols = st.columns(attack)
    for i in range(attack):
        with attack_cols[i]:
            st.markdown("<div class='player'>🏃‍♂️</div>", unsafe_allow_html=True)
            st.markdown("<div class='label'>FW</div>", unsafe_allow_html=True)
            
    # -------------------
    # 미드필더 (Midfielders)
    # -------------------
    mid_cols = st.columns(midfield)
    for i in range(midfield):
        with mid_cols[i]:
            st.markdown("<div class='player'>🏃‍♂️</div>", unsafe_allow_html=True)
            st.markdown("<div class='label'>MF</div>", unsafe_allow_html=True)

    # -------------------
    # 수비수 (Defenders)
    # -------------------
    def_cols = st.columns(defense)
    for i in range(defense):
        with def_cols[i]:
            st.markdown("<div class='player'>🏃‍♂️</div>", unsafe_allow_html=True)
            st.markdown("<div class='label'>DF</div>", unsafe_allow_html=True)
            
    st.markdown("</div>", unsafe_allow_html=True)
