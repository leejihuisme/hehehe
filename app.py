import streamlit as st
import pandas as pd

# 샘플 영화 데이터 생성 (실제로는 CSV 파일 불러오기)
data = {
    "title": ["Inception", "Interstellar", "The Dark Knight", "La La Land", "Parasite"],
    "genre": ["Sci-Fi", "Sci-Fi", "Action", "Romance", "Thriller"],
    "year": [2010, 2014, 2008, 2016, 2019],
    "rating": [8.8, 8.6, 9.0, 8.0, 8.6],
    "poster": [
        "https://m.media-amazon.com/images/I/51zUbui+gbL._AC_.jpg",
        "https://m.media-amazon.com/images/I/71n58BfQ3kL._AC_SL1024_.jpg",
        "https://m.media-amazon.com/images/I/51k0qa6q0-L._AC_.jpg",
        "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_SL1024_.jpg",
        "https://m.media-amazon.com/images/I/91PpQG+9ZtL._AC_SL1500_.jpg",
    ],
    "summary": [
        "A thief who steals corporate secrets through dream-sharing technology is given an inverse task.",
        "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "Batman faces the Joker, a criminal mastermind who plunges Gotham into chaos.",
        "A jazz musician and an aspiring actress fall in love while pursuing their dreams.",
        "Greed and class discrimination threaten the newly formed symbiotic relationship between two families.",
    ]
}

movies = pd.DataFrame(data)

# Streamlit 앱 UI
st.title("🎬 영화 추천 앱")
st.write("장르와 연도를 선택하면 영화 추천을 볼 수 있습니다!")

# 선택 위젯
selected_genre = st.selectbox("장르 선택", options=movies["genre"].unique())
selected_year = st.slider("개봉 연도 선택", int(movies["year"].min()), int(movies["year"].max()))

# 추천 로직
filtered = movies[(movies["genre"] == selected_genre) & (movies["year"] >= selected_year)]

if filtered.empty:
    st.warning("해당 조건에 맞는 영화가 없습니다.")
else:
    for _, row in filtered.iterrows():
        st.subheader(f"{row['title']} ({row['year']}) ⭐{row['rating']}")
        st.image(row['poster'], width=200)
        st.write(row['summary'])
