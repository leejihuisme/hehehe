import streamlit as st
import numpy as np

# 타이틀 설정
st.title("2D 도형 계산기 📐")

# 사이드바에서 도형 선택
shape_option = st.sidebar.selectbox(
    "보고 싶은 도형을 선택하세요:",
    ("원", "직사각형", "정사각형")
)

# --- 원 계산 ---
if shape_option == "원":
    st.header("원")
    radius = st.slider("반지름을 조절하세요:", 1, 10, 3)

    # 넓이와 둘레 계산
    area = np.pi * radius**2
    circumference = 2 * np.pi * radius

    st.subheader("계산 결과:")
    st.write(f"**원의 반지름:** {radius}")
    st.write(f"**원의 넓이:** {area:.2f}")
    st.write(f"**원의 둘레:** {circumference:.2f}")

    st.info("이 프로그램은 계산만 수행하며, 도형을 시각적으로 보여주지는 않습니다.")


# --- 직사각형 계산 ---
elif shape_option == "직사각형":
    st.header("직사각형")
    width = st.slider("가로 길이를 조절하세요:", 1, 10, 5)
    height = st.slider("세로 길이를 조절하세요:", 1, 10, 3)

    # 넓이와 둘레 계산
    area = width * height
    perimeter = 2 * (width + height)

    st.subheader("계산 결과:")
    st.write(f"**직사각형의 가로:** {width}")
    st.write(f"**직사각형의 세로:** {height}")
    st.write(f"**직사각형의 넓이:** {area}")
    st.write(f"**직사각형의 둘레:** {perimeter}")

    st.info("이 프로그램은 계산만 수행하며, 도형을 시각적으로 보여주지는 않습니다.")


# --- 정사각형 계산 ---
elif shape_option == "정사각형":
    st.header("정사각형")
    side = st.slider("한 변의 길이를 조절하세요:", 1, 10, 4)

    # 넓이와 둘레 계산
    area = side**2
    perimeter = 4 * side

    st.subheader("계산 결과:")
    st.write(f"**정사각형의 한 변 길이:** {side}")
    st.write(f"**정사각형의 넓이:** {area}")
    st.write(f"**정사각형의 둘레:** {perimeter}")

    st.info("이 프로그램은 계산만 수행하며, 도형을 시각적으로 보여주지는 않습니다.")
