import streamlit as st

st.set_page_config(page_title="지수법칙 퀴즈", page_icon="📘", layout="centered")

QUESTIONS = [
    {
        "q_latex": r"2^3 \times 2^4",
        "q_text": "2^3 × 2^4 을 간단히 하면?",
        "options": [
            {"latex": r"2^{12}", "text": "2^12"},
            {"latex": r"2^7", "text": "2^7"},
            {"latex": r"2^1", "text": "2^1"},
            {"latex": r"4^7", "text": "4^7"},
        ],
        "answer": "2^7",
        "explanation": "밑이 같을 때 곱셈은 지수를 더합니다. 3+4=7"
    },
    {
        "q_latex": r"(x^2)^3",
        "q_text": "(x^2)^3 을 간단히 하면?",
        "options": [
            {"latex": r"x^5", "text": "x^5"},
            {"latex": r"x^6", "text": "x^6"},
            {"latex": r"x^8", "text": "x^8"},
            {"latex": r"x^9", "text": "x^9"},
        ],
        "answer": "x^6",
        "explanation": "거듭제곱의 거듭제곱은 지수를 곱합니다. 2×3=6"
    },
    {
        "q_latex": r"y^{10} \div y^2",
        "q_text": "y^10 ÷ y^2 을 간단히 하면?",
        "options": [
            {"latex": r"y^{12}", "text": "y^12"},
            {"latex": r"y^5", "text": "y^5"},
            {"latex": r"y^8", "text": "y^8"},
            {"latex": r"y^{20}", "text": "y^20"},
        ],
        "answer": "y^8",
        "explanation": "밑이 같을 때 나눗셈은 지수를 뺍니다. 10-2=8"
    },
    {
        "q_latex": r"(ab)^4",
        "q_text": "(ab)^4 를 간단히 하면?",
        "options": [
            {"latex": r"ab^4", "text": "ab^4"},
            {"latex": r"a^4b", "text": "a^4b"},
            {"latex": r"a^4b^4", "text": "a^4b^4"},
            {"latex": r"4ab", "text": "4ab"},
        ],
        "answer": "a^4b^4",
        "explanation": "괄호 안의 각 문자에 지수를 똑같이 적용합니다."
    },
    {
        "q_latex": r"(-2a)^3",
        "q_text": "(-2a)^3 을 간단히 하면?",
        "options": [
            {"latex": r"-6a^3", "text": "-6a^3"},
            {"latex": r"-8a^3", "text": "-8a^3"},
            {"latex": r"8a^3", "text": "8a^3"},
            {"latex": r"-2a^3", "text": "-2a^3"},
        ],
        "answer": "-8a^3",
        "explanation": "(-2)^3=-8 이고, a도 세 번 곱해져 a^3이 됩니다."
    },
]

if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected" not in st.session_state:
    st.session_state.selected = None
if "show_result" not in st.session_state:
    st.session_state.show_result = False

def reset_for_next():
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.show_result = False

def choose(option_text: str):
    if st.session_state.answered:
        return
    st.session_state.selected = option_text
    st.session_state.answered = True
    st.session_state.show_result = True
    if option_text == QUESTIONS[st.session_state.index]["answer"]:
        st.session_state.score += 5

def next_question():
    if st.session_state.index < len(QUESTIONS) - 1:
        st.session_state.index += 1
        reset_for_next()
    else:
        st.session_state.index += 1

st.title("📘 지수법칙 퀴즈")
st.caption("수식이 깨지지 않도록 문제와 보기를 LaTeX 형식으로 표시한 버전입니다.")

if st.session_state.index >= len(QUESTIONS):
    st.success("퀴즈 완료!")
    st.subheader(f"최종 점수: {st.session_state.score}점")
    if st.button("처음부터 다시 하기", use_container_width=True):
        st.session_state.index = 0
        st.session_state.score = 0
        reset_for_next()
        st.rerun()
    st.stop()

q = QUESTIONS[st.session_state.index]

st.markdown(f"### 문제 {st.session_state.index + 1} / {len(QUESTIONS)}")
st.write(q["q_text"])
st.latex(q["q_latex"])

st.markdown("#### 보기를 누르세요")

for i, option in enumerate(q["options"]):
    label = ["A", "B", "C", "D"][i]
    cols = st.columns([1, 6])
    with cols[0]:
        st.button(
            label,
            key=f"btn_{st.session_state.index}_{i}",
            on_click=choose,
            args=(option["text"],),
            use_container_width=True,
            disabled=st.session_state.answered,
        )
    with cols[1]:
        st.latex(option["latex"])

if st.session_state.show_result:
    if st.session_state.selected == q["answer"]:
        st.success("정답입니다! +5점")
    else:
        st.error("오답입니다.")
        st.write(f"선택한 답: {st.session_state.selected}")
        st.write(f"정답: {q['answer']}")
        st.info(q["explanation"])

    st.write(f"현재 점수: {st.session_state.score}점")

    if st.button("다음 문제", use_container_width=True):
        next_question()
        st.rerun()
