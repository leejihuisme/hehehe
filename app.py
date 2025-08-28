import streamlit as st
import matplotlib.pyplot as plt

# --- 페이지 설정 ---
st.title("🏡 2D 가구 배치 시뮬레이터")
st.info("방 크기를 설정하고, 가구의 위치와 크기를 입력해 보세요.")

# --- 방 크기 입력 ---
st.subheader("1. 방 크기 설정")
room_width = st.slider("방의 가로 길이 (m)", 1.0, 20.0, 5.0)
room_height = st.slider("방의 세로 길이 (m)", 1.0, 20.0, 4.0)

# --- 가구 입력 ---
st.subheader("2. 가구 정보 입력")
num_furniture = st.number_input("추가할 가구의 개수", min_value=0, max_value=5, value=1)

furniture_list = []
for i in range(int(num_furniture)):
    st.write(f"**가구 #{i+1}**")
    name = st.text_input(f"가구 이름 (예: 침대)", key=f"name_{i}")
    x_pos = st.slider(f"X축 위치 (좌측 하단 기준)", 0.0, room_width, float(room_width/2), key=f"x_{i}")
    y_pos = st.slider(f"Y축 위치 (좌측 하단 기준)", 0.0, room_height, float(room_height/2), key=f"y_{i}")
    width = st.slider(f"가구 가로 길이", 0.1, room_width, 1.0, key=f"w_{i}")
    height = st.slider(f"가구 세로 길이", 0.1, room_height, 2.0, key=f"h_{i}")

    furniture_list.append({
        'name': name,
        'x': x_pos,
        'y': y_pos,
        'width': width,
        'height': height
    })

# --- 시각화 ---
st.subheader("3. 배치 시뮬레이션")

fig, ax = plt.subplots(figsize=(10, 8))

# 방 그리기
room_rect = plt.Rectangle((0, 0), room_width, room_height, fc='lightgray', ec='black')
ax.add_patch(room_rect)

# 가구 그리기
total_furniture_area = 0
for furniture in furniture_list:
    name = furniture['name']
    x = furniture['x']
    y = furniture['y']
    width = furniture['width']
    height = furniture['height']

    # 가구 영역 표시
    furniture_rect = plt.Rectangle((x - width/2, y - height/2), width, height, fc='lightblue', ec='darkblue', alpha=0.7)
    ax.add_patch(furniture_rect)

    # 가구 이름 표시
    ax.text(x, y, name, ha='center', va='center', fontsize=12, color='black', weight='bold')

    # 가구 넓이 계산
    total_furniture_area += width * height

ax.set_xlim(0, room_width)
ax.set_ylim(0, room_height)
ax.set_aspect('equal', adjustable='box')
ax.set_title("가구 배치도")
ax.set_xlabel("가로 (m)")
ax.set_ylabel("세로 (m)")
ax.grid(True)
st.pyplot(fig)

# --- 결과 분석 ---
st.subheader("4. 분석 결과")
room_area = room_width * room_height
empty_area = room_area - total_furniture_area

st.metric("총 방 넓이", f"{room_area:.2f} m²")
st.metric("가구들이 차지하는 넓이", f"{total_furniture_area:.2f} m²")
st.metric("남은 여유 공간", f"{empty_area:.2f} m²")
