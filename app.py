import streamlit as st

st.set_page_config(page_title="지수법칙 퀴즈", page_icon="📘", layout="centered")

QUESTIONS = [
    {"q": "2^3 × 2^4 을 간단히 하면?", "a": "2^7", "o": ["2^12", "2^7", "2^1", "4^7"], "ex": "밑이 같을 때 곱셈은 지수를 더합니다. 3+4=7"},
    {"q": "a^5 × a 를 간단히 하면?", "a": "a^6", "o": ["a^5", "a^4", "a^6", "2a^5"], "ex": "a는 a^1과 같으므로 5+1=6입니다."},
    {"q": "(x^2)^3 을 간단히 하면?", "a": "x^6", "o": ["x^5", "x^6", "x^8", "x^9"], "ex": "거듭제곱의 거듭제곱은 지수를 곱합니다. 2×3=6"},
    {"q": "y^10 ÷ y^2 을 간단히 하면?", "a": "y^8", "o": ["y^12", "y^5", "y^8", "y^20"], "ex": "밑이 같을 때 나눗셈은 지수를 뺍니다. 10-2=8"},
    {"q": "a^3 ÷ a^3 의 값은?", "a": "1", "o": ["0", "1", "a", "a^6"], "ex": "같은 수를 나누면 1입니다. (0이 아닌 경우)"},
    {"q": "x^2 ÷ x^5 를 간단히 하면?", "a": "1/x^3", "o": ["x^3", "1/x^7", "1/x^3", "1"], "ex": "뒤의 지수가 더 크면 분모로 내려갑니다. x^(2-5)=x^-3=1/x^3"},
    {"q": "(ab)^4 를 간단히 하면?", "a": "a^4b^4", "o": ["ab^4", "a^4b", "a^4b^4", "4ab"], "ex": "곱의 거듭제곱은 각각에 지수를 적용합니다."},
    {"q": "(x/y)^3 을 간단히 하면?", "a": "x^3/y^3", "o": ["x/y^3", "x^3/y", "x^3/y^3", "xy^3"], "ex": "분자와 분모에 각각 3제곱을 합니다."},
    {"q": "(-2a)^3 을 간단히 하면?", "a": "-8a^3", "o": ["-6a^3", "-8a^3", "8a^3", "-2a^3"], "ex": "(-2)^3=-8 이고 a도 3제곱이 됩니다."},
    {"q": "(3x^2)^2 을 간단히 하면?", "a": "9x^4", "o": ["6x^4", "9x^2", "9x^4", "3x^4"], "ex": "3도 제곱, x^2도 제곱합니다. 3^2=9, (x^2)^2=x^4"},
]


def init_state():
    defaults = {
        "index": 0,
        "score": 0,
        "submitted": False,
        "selected": None,
        "wrong_count": 0,
        "finished": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def reset_quiz():
    for key in ["index", "score", "submitted", "selected", "wrong_count", "finished"]:
        if key in st.session_state:
            del st.session_state[key]
    init_state()


init_state()

st.title("📘 지수법칙 퀴즈")
st.caption("학생들이 웹주소로 접속해 바로 풀 수 있는 스트림릿 앱")

if st.session_state.finished:
    st.success("퀴즈 완료!")
    st.subheader(f"최종 점수: {st.session_state.score}점")
    st.write(f"오답 횟수: {st.session_state.wrong_count}회")
    if st.session_state.score >= 40:
        st.info("아주 잘했어요! 지수법칙을 안정적으로 이해하고 있어요.")
    elif st.session_state.score >= 20:
        st.info("좋아요! 몇 가지 규칙만 더 연습하면 훨씬 탄탄해져요.")
    else:
        st.info("괜찮아요! 해설을 보며 다시 도전하면 금방 늘어요.")

    if st.button("다시 시작하기", use_container_width=True):
        reset_quiz()
        st.rerun()
    st.stop()

q = QUESTIONS[st.session_state.index]

progress = (st.session_state.index + 1) / len(QUESTIONS)
st.progress(progress)
col1, col2, col3 = st.columns(3)
col1.metric("문제", f"{st.session_state.index + 1}/{len(QUESTIONS)}")
col2.metric("점수", st.session_state.score)
col3.metric("오답", st.session_state.wrong_count)

st.markdown("---")
st.subheader(q["q"])

selected = st.radio(
    "정답을 고르세요.",
    q["o"],
    index=None,
    key=f"radio_{st.session_state.index}"
)

if not st.session_state.submitted:
    if st.button("제출하기", type="primary", use_container_width=True):
        if selected is None:
            st.warning("먼저 답을 하나 선택하세요.")
        else:
            st.session_state.selected = selected
            st.session_state.submitted = True
            if selected == q["a"]:
                st.session_state.score += 5
            else:
                st.session_state.score -= 5
                st.session_state.wrong_count += 1
            st.rerun()
else:
    if st.session_state.selected == q["a"]:
        st.success("정답입니다! +5점")
    else:
        st.error("오답입니다. -5점")
        st.write(f"정답: **{q['a']}**")
        st.info(f"해설: {q['ex']}")

    last_question = st.session_state.index == len(QUESTIONS) - 1
    next_label = "결과 보기" if last_question else "다음 문제"
    if st.button(next_label, use_container_width=True):
        st.session_state.submitted = False
        st.session_state.selected = None
        if last_question:
            st.session_state.finished = True
        else:
            st.session_state.index += 1
        st.rerun()

st.markdown("---")
st.write("배포 후 학생들은 링크만 눌러서 바로 사용할 수 있습니다.")
