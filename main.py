import streamlit as st

# MBTI별 취미 추천 데이터 🎨
mbti_hobbies = {
    "INTJ": ["📖 독서", "🎯 퍼즐 맞추기", "🧘 혼자 명상"],
    "INTP": ["🧪 실험적인 요리", "💡 아이디어 노트 쓰기", "🎮 전략 게임"],
    "ENTJ": ["📈 자기계발 강의 듣기", "🗂️ 블로그 운영", "🎯 다트 던지기"],
    "ENTP": ["🎙️ 팟캐스트 듣기", "🃏 카드 마술", "🗣️ 토론 모임"],
    "INFJ": ["🕯️ 향초 켜고 일기 쓰기", "🎨 그림 그리기", "🌌 별 보기"],
    "INFP": ["✍️ 감성 글쓰기", "📷 사진 찍기", "🎧 인디 음악 감상"],
    "ENFJ": ["📚 독서 모임 참여", "🧁 간단 베이킹", "🎬 영화 정리 노트"],
    "ENFP": ["🎨 컬러링북 색칠", "🎲 보드게임", "🎈 무작정 산책"],
    "ISTJ": ["📋 할 일 정리", "🧩 조립 키트", "🧼 집 정리"],
    "ISFJ": ["🍲 요리 연습", "🧵 손뜨개", "🌿 반려식물 돌보기"],
    "ESTJ": ["📊 가계부 정리", "🎯 다트 연습", "📆 일정 플래너 꾸미기"],
    "ESFJ": ["🍪 디저트 만들기", "📸 추억 정리 앨범 만들기", "🎶 플레이리스트 정리"],
    "ISTP": ["🔧 공구 만지작거리기", "🎮 혼자 게임", "📷 액션캠 브이로그"],
    "ISFP": ["🎧 음악 들으며 그림 그리기", "📓 무지 노트 꾸미기", "🪴 식물 인테리어"],
    "ESTP": ["🚴 자전거 타기", "🎲 실내 스포츠", "📺 유튜브 짧은 영상 만들기"],
    "ESFP": ["💃 홈 파티 준비", "🎤 노래방 앱", "📱 틱톡 댄스 따라하기"]
}

# 🌟 페이지 설정
st.set_page_config(page_title="MBTI 취미 추천기 🎨", page_icon="🌈")
st.title("🌟 MBTI로 알아보는 퇴근 후 취미 🎯")
st.markdown("당신의 MBTI를 선택하면, 오늘 하루를 마무리할 ✨편안한 취미✨를 추천해드려요! 😌")

# MBTI 선택 드롭다운
mbti_list = sorted(mbti_hobbies.keys())
selected_mbti = st.selectbox("👇 당신의 MBTI를 골라주세요!", mbti_list)

# 추천 취미 보여주기
if selected_mbti:
    st.markdown(f"## 🎁 {selected_mbti} 유형에게 추천하는 퇴근 후 취미는?")
    for hobby in mbti_hobbies[selected_mbti]:
        st.markdown(f"- {hobby}")

    st.balloons()  # 🎈
