import streamlit as st

st.set_page_config(page_title="지수법칙 퀴즈", page_icon="📘", layout="centered")

st.markdown("""
<style>
.block-container {max-width: 820px; padding-top: 2rem; padding-bottom: 2rem;}
.option-btn button {
    width: 100%;
    height: 54px;
    font-size: 1.1rem;
    font-weight: 700;
    border-radius: 12px;
}
.option-row {
    padding: 10px 0 14px 0;
    border-bottom: 1px solid #eee;
}
.score-box {
    padding: 14px 18px;
    border-radius: 14px;
    background: #f6f7fb;
    border: 1px solid #e6e8ef;
    margin-bottom: 18px;
}
</style>
""", unsafe_allow_html=True)

questions = [
    {
        "text": "2^3 \\times 2^4 을 간단히 하면?",
        "latex": r"2^3 \times 2^4",
        "options": [r"2^{12}", r"2^7", r"2^1", r"4^7"],
        "answer": r"2^7",
        "explanation": "밑이 같을 때는 지수를 더합니다. 3+4=7"
    },
    {
        "text": "(x^2)^3 을 간단히 하면?",
        "latex": r"(x^2)^3",
        "options": [r"x^5", r"x^6", r"x^8", r"x^9"],
        "answer": r"x^6",
        "explanation": "거듭제곱의 거듭제곱은 지수를 곱합니다. 2×3=6"
    },
    {
        "text": "y^{10} \\div y^2 을 간단히 하면?",
        "latex": r"y^{10} \div y^2",
        "options": [r"y^{12}", r"y^5", r"y^8", r"y^{20}"],
        "answer": r"y^8",
        "explanation": "나눗셈은 지수를 뺍니다. 10-2=8"
    },
    {
        "text": "(ab)^4 를 간단히 하면?",
        "latex": r"(ab)^4",
        "options": [r"ab^4", r"a^4b", r"a^4b^4", r"4ab"],
        "answer": r"a^4b^4",
        "explanation": "괄호 안의 각 항에 4제곱을 적용합니다."
    },
    {
        "text": "\\left(\\frac{x}{y}\\right)^3 을 간단히 하면?",
        "latex": r"\left(\frac{x}{y}\right)^3",
        "options": [r"\frac{x}{y^3}", r"\frac{x^3}{y}", r"\frac{x^3}{y^3}", r"xy^3"],
        "answer": r"\frac{x^3}{y^3}",
        "explanation": "분자와 분모 각각에 3제곱을 적용합니다."
    },
]

if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "selected" not in st.session_state:
    st.session_state.selected = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False

def choose(option):
    st.session_state.selected = option

def next_question():
    if st.session_state.index < len(questions) - 1:
        st.session_state.index += 1
        st.session_state.selected = None
        st.session_state.submitted = False
    else:
        st.session_state.index = len(questions)

if st.session_state.index >= len(questions):
    st.title("🎉 퀴즈 완료")
    st.markdown(f"<div class='score-box'><h3>최종 점수: {st.session_state.score}점</h3></div>", unsafe_allow_html=True)
    if st.button("다시 시작하기"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.selected = None
        st.session_state.submitted = False
        st.rerun()
    st.stop()

q = questions[st.session_state.index]

st.markdown(f"<div class='score-box'><b>문제 {st.session_state.index + 1} / {len(questions)}</b> &nbsp;&nbsp; 현재 점수: <b>{st.session_state.score}</b></div>", unsafe_allow_html=True)

st.subheader("문제를 보고 알맞은 답을 고르세요.")
st.latex(q["latex"])

st.markdown("### 보기")

labels = ["A", "B", "C", "D"]
for i, opt in enumerate(q["options"]):
    c1, c2 = st.columns([1, 6], vertical_alignment="center")
    with c1:
        st.markdown("<div class='option-btn'>", unsafe_allow_html=True)
        st.button(labels[i], key=f"btn_{i}", on_click=choose, args=(opt,))
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        prefix = "✅ " if st.session_state.selected == opt else ""
        st.markdown(f"<div class='option-row'>{prefix}</div>", unsafe_allow_html=True)
        st.latex(opt)

if st.session_state.selected is not None:
    st.info(f"선택한 답: {st.session_state.selected}")

if st.button("제출하기", type="primary", use_container_width=True):
    if st.session_state.selected is None:
        st.warning("먼저 보기를 선택하세요.")
    else:
        st.session_state.submitted = True
        if st.session_state.selected == q["answer"]:
            st.session_state.score += 5
            st.success("정답입니다! +5점")
        else:
            st.error(f"오답입니다. 정답은 {q['answer']} 입니다. -0점")
        st.write("해설:", q["explanation"])

        if st.button("다음 문제", use_container_width=True):
            next_question()
            st.rerun()

if st.session_state.submitted:
    if st.button("다음 문제로 이동", use_container_width=True):
        next_question()
        st.rerun()

