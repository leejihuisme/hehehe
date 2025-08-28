import streamlit as st
import random

st.title("⚽️ 축구 선수 능력치 생성기")
st.markdown("---")

# 사용자에게 선수 이름 입력받기
player_name = st.text_input("좋아하는 축구 선수의 이름을 입력하세요:", "손흥민")

# 능력치 생성 버튼
if st.button("능력치 생성"):
    if player_name:
        # 이름 길이를 기준으로 능력치 계산 (랜덤성 부여)
        name_length = len(player_name)
        
        # '공격', '속도', '수비', '패스' 능력치 계산
        attack_stat = min(100, (name_length * 8) + random.randint(1, 20))
        speed_stat = min(100, (name_length * 7) + random.randint(1, 25))
        defense_stat = min(100, (name_length * 5) + random.randint(1, 30))
        pass_stat = min(100, (name_length * 6) + random.randint(1, 22))

        # 총 능력치 계산
        total_stat = attack_stat + speed_stat + defense_stat + pass_stat
        
        st.header(f"⭐ {player_name} 선수의 능력치")
        st.write(f"총점: **{total_stat}** (400점 만점)")
        
        st.markdown("---")
        
        # 능력치 시각화
        st.subheader("📊 스탯 분포")
        st.progress(attack_stat / 100, text=f"공격: {attack_stat}")
        st.progress(speed_stat / 100, text=f"속도: {speed_stat}")
        st.progress(defense_stat / 100, text=f"수비: {defense_stat}")
        st.progress(pass_stat / 100, text=f"패스: {pass_stat}")

        st.info("이 능력치는 재미를 위해 생성된 것으로, 실제 데이터와 무관합니다.")
    else:
        st.warning("선수 이름을 입력해주세요.")
