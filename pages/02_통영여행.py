import streamlit as st

# 페이지 설정
st.set_page_config(page_title="통영 2박 3일 여행 코스 🧳", page_icon="🌊")

# 타이틀 및 소개
st.title("🌅 통영 2박 3일 여행 ✨완.벽.가.이.드✨")
st.markdown("""
여유로운 바다, 감성 가득한 벽화마을, 그리고 맛있는 꿀빵까지!  
**지금 떠나는 통영 2박 3일 여행** 🚗🎒  
👇 아래 코스를 참고해서 힐링을 준비해보세요!
""")

# 이미지 추가 (스트림릿은 URL 또는 로컬 경로 사용 가능)
st.image("https://cdn.visitkorea.or.kr/img/call?cmd=VIEW&id=b43b94c8-660f-4c6a-a0a8-4ae6e9c69a68", caption="동피랑 마을 전경 🎨", use_column_width=True)

# DAY 1
st.header("📍 Day 1 - 통영 도착 & 감성 코스")
st.markdown("""
- 🛥️ **도착 후 중앙시장 탐방**  
  👉 싱싱한 회와 통영 꿀빵 맛보기!

- 🎨 **동피랑 벽화마을 산책**  
  골목골목마다 감성 뿜뿜~ 사진 필수! 📸

- 🚡 **미륵산 케이블카**  
  통영 바다가 한눈에! 일몰 시간 추천 🌅

- 🍽️ **숙소 체크인 & 저녁 식사**  
  바닷가 근처 펜션 추천 🛌
""")

st.image("https://tong.visitkorea.or.kr/static/images/miruksan.jpg", caption="미륵산 케이블카에서 바라본 석양 🌇", use_column_width=True)

# DAY 2
st.header("📍 Day 2 - 바다와 섬의 하루")
st.markdown("""
- 🚤 **한산도 or 비진도 유람선 타기**  
  이순신 장군의 흔적과 바다 풍경을 만나는 시간!

- 🌿 **이순신공원 산책**  
  통영의 푸른 바다와 동상, 벤치에서 힐링 🌊

- 🍲 **해물 식당에서 점심 한 끼**  
  멍게비빔밥, 물메기탕... 진짜 맛집이 여기에!

- ☕ **카페 투어**  
  바다가 보이는 루프탑 카페에서 여유로운 오후 💙
""")

st.image("https://www.koreatodo.com/images/korea/south-korea-tongyeong-hansando-island-5.jpg", caption="한산도에서 보는 바다와 배 🌴", use_column_width=True)

# DAY 3
st.header("📍 Day 3 - 가볍게 마무리 🌤️")
st.markdown("""
- 🍜 **간단한 아침 & 체크아웃**

- 🧵 **통영 전통공예관 or 서피랑 책방 거리**  
  기념품 구경도 잊지 마세요!

- 📦 **통영 중앙시장 재방문 (선물 구입)**  
  꿀빵 포장하고 집으로~ 🎁

- 🚗 **귀가길에도 감성 한 스푼**  
  바다를 마음에 담아 가세요 🌊💙
""")

st.image("https://cdn.visitkorea.or.kr/img/call?cmd=VIEW&id=4ee3bcf3-207e-4c2a-a72f-3f01a7f8357f", caption="서피랑의 조용한 거리 🌳", use_column_width=True)

# 마무리 멘트
st.markdown("""
---

### 🎉 지금 당장 떠나고 싶어지지 않나요?

💌 잊지 마세요: 여행은 **당신에게 주는 최고의 선물**이에요.  
가볍게 짐을 싸고, 푸른 통영 바다로 힐링하러 떠나보세요! 🌊  
""")

# 🎈 효과 (선택사항)
st.balloons()
