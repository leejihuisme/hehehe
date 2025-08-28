import streamlit as st

# 간단한 단어 사전 예시 (실제로는 더 큰 리스트 필요)
word_list = ["사과", "과자", "자동차", "학교", "고양이", "이발소", "소방서", "서울", "운동", "공원"]

# 세션 상태 초기화
if "used_words" not in st.session_state:
    st.session_state.used_words = []
if "last_char" not in st.session_state:
    st.session_state.last_char = None

st.title("🔗 끝말잇기 게임")
st.write("단어를 입력해서 끝말잇기를 해보세요!")

# 사용자 입력
user_word = st.text_input("단어 입력")

if st.button("제출"):
    if user_word not in word_list:
        st.error("사전에 없는 단어입니다!")
    elif user_word in st.session_state.used_words:
        st.error("이미 사용한 단어입니다!")
    else:
        # 첫 단어이거나, 규칙 확인
        if st.session_state.last_char is None or user_word[0] == st.session_state.last_char:
            st.session_state.used_words.append(user_word)
            st.session_state.last_char = user_word[-1]
            st.success(f"✅ '{user_word}' 입력 성공! 다음 단어는 '{st.session_state.last_char}'로 시작해야 합니다.")
        else:
            st.error(f"❌ 규칙 위반! '{st.session_state.last_char}'(으)로 시작해야 해요.")

# 지금까지 사용한 단어 출력
if st.session_state.used_words:
    st.subheader("📜 지금까지 나온 단어")
    st.write(" → ".join(st.session_state.used_words))
