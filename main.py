import streamlit as st

# 🎬 MBTI에 따른 영화 추천 데이터
mbti_movies = {
    "INTJ": ["🧠 『굿 윌 헌팅』", "🚀 『인터스텔라』"],
    "INTP": ["🧪 『프루프』", "🧬 『컨택트』"],
    "ENTJ": ["🎯 『뷰티풀 마인드』", "🌌 『2001: 스페이스 오디세이』"],
    "ENTP": ["🔭 『디스커버리』", "💥 『아이언맨』"],
    "INFJ": ["🔬 『히든 피겨스』", "🌠 『콘택트』"],
    "INFP": ["📚 『빅 히어로』", "🧬 『루시』"],
    "ENFJ": ["💡 『소셜 네트워크』", "🚀 『마션』"],
    "ENFP": ["🔋 『백 투 더 퓨처』", "🌀 『테넷』"],
    "ISTJ": ["💻 『이미테이션 게임』", "📐 『피그말리온』"],
    "ISFJ": ["🧬 『가타카』", "🧠 『왓슨을 찾아서』"],
    "ESTJ": ["🛰️ 『그래비티』", "🕹️ 『트론』"],
    "ESFJ": ["📡 『인셉션』", "🧲 『업사이드 다운』"],
    "ISTP": ["⚙️ 『엑스 마키나』", "🧪 『테슬라』"],
    "ISFP": ["🌌 『어라이벌』", "🔋 『트랜센던스』"],
    "ESTP": ["🚗 『레디 플레이어 원』", "🔬 『아이로봇』"],
    "ESFP": ["🎉 『월-E』", "🤖 『로봇 앤 프랭크』"]
}

# 🌟 타이틀 & 설명
st.set_page_config(page_title="MBTI 영화 추천기 🎥", page_icon="🎞️")
st.title("📽️ 당신의 MBTI로 추천받는 수학·과학 명작 🎬")
st.markdown("MBTI 유형을 선택하면, 당신에게 딱 어울리는 🎓 **명작 영화**를 추천해드려요! 💫")

# 🎯 MBTI 선택
mbti_options = list(mbti_movies.keys())
selected_mbti = st.selectbox("👇 MBTI를 선택해주세요!", mbti_options)

# 💌 추천 결과
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형에게 추천하는 영화는?")
    for movie in mbti_movies[selected_mbti]:
        st.markdown(f"- {movie}")
    
    st.balloons()  # 🎈 풍선 효과!
    st.success("팡팡! 영화가 도착했어요 🎁")
