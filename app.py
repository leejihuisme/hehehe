import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 타이틀 설정
st.title("2D 도형 시각화 프로그램 📐")

# 사이드바에서 도형 선택
shape_option = st.sidebar.selectbox(
    "보고 싶은 도형을 선택하세요:",
    ("원", "직사각형", "정사각형")
)

# --- 원 그리기 ---
if shape_option == "원":
    st.header("원 시각화")
    radius = st.slider("반지름을 조절하세요:", 1, 10, 3)

    # 원의 방정식
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Matplotlib으로 원 그리기
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_aspect('equal', adjustable='box') # x, y 축 비율을 같게 설정
    ax.set_title(f'반지름이 {radius}인 원')
    ax.grid()

    st.pyplot(fig)

    # 넓이와 둘레 계산
    area = np.pi * radius**2
    circumference = 2 * np.pi * radius

    st.subheader("계산 결과:")
    st.write(f"**원의 넓이:** {area:.2f}")
    st.write(f"**원의 둘레:** {circumference:.2f}")


# --- 직사각형 그리기 ---
elif shape_option == "직사각형":
    st.header("직사각형 시각화")
    width = st.slider("가로 길이를 조절하세요:", 1, 10, 5)
    height = st.slider("세로 길이를 조절하세요:", 1, 10, 3)

    # 직사각형 꼭짓점 좌표
    x_coords = [0, width, width, 0, 0]
    y_coords = [0, 0, height, height, 0]

    # Matplotlib으로 직사각형 그리기
    fig, ax = plt.subplots()
    ax.plot(x_coords, y_coords)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f'가로 {width}, 세로 {height}인 직사각형')
    ax.set_xlim(-1, 11) # 그래프 범위 설정
    ax.set_ylim(-1, 11)
    ax.grid()

    st.pyplot(fig)

    # 넓이와 둘레 계산
    area = width * height
    perimeter = 2 * (width + height)

    st.subheader("계산 결과:")
    st.write(f"**직사각형의 넓이:** {area}")
    st.write(f"**직사각형의 둘레:** {perimeter}")


# --- 정사각형 그리기 ---
elif shape_option == "정사각형":
    st.header("정사각형 시각화")
    side = st.slider("한 변의 길이를 조절하세요:", 1, 10, 4)

    # 정사각형 꼭짓점 좌표
    x_coords = [0, side, side, 0, 0]
    y_coords = [0, 0, side, side, 0]

    # Matplotlib으로 정사각형 그리기
    fig, ax = plt.subplots()
    ax.plot(x_coords, y_coords)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f'한 변의 길이가 {side}인 정사각형')
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.grid()

    st.pyplot(fig)

    # 넓이와 둘레 계산
    area = side**2
    perimeter = 4 * side

    st.subheader("계산 결과:")
    st.write(f"**정사각형의 넓이:** {area}")
    st.write(f"**정사각형의 둘레:** {perimeter}")
