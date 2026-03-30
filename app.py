import time
import streamlit as st

st.set_page_config(page_title="지수법칙 퀴즈", page_icon="📘", layout="centered")

st.markdown("""
<style>
.block-container {
    max-width: 900px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}
.score-box {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
    padding: 1.2rem 1.5rem;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 1rem;
    box-shadow: 0 10px 24px rgba(0,0,0,0.15);
}
.score-title {
    font-size: 1.1rem;
    font-weight: 700;
    opacity: 0.9;
}
.score-value {
    font-size: 3.2rem;
    font-weight: 900;
    line-height: 1.1;
    margin-top: 0.2rem;
    color: #facc15;
}
.progress-box {
    background: #eff6ff;
    border: 2px solid #bfdbfe;
    padding: 0.8rem 1rem;
    border-radius: 16px;
    font-size: 1.2rem;
    font-weight: 800;
    text-align: center;
    margin-bottom: 1rem;
}
.question-card {
    background: white;
    border: 2px solid #e5e7eb;
    border-radius: 20px;
    padding: 1.2rem 1.2rem 0.8rem 1.2rem;
    margin-bottom: 1rem;
}
.feedback-ok {
    background: #ecfdf5;
    border: 2px solid #86efac;
    color: #166534;
    padding: 1rem;
    border-radius: 16px;
    font-size: 1.2rem;
    font-weight: 800;
    text-align: center;
    margin-top: 1rem;
}
.feedback-no {
    background: #fef2f2;
    border: 2px solid #fca5a5;
    color: #b91c1c;
    padding: 1rem;
    border-radius: 16px;
    font-size: 1.2rem;
    font-weight: 800;
    text-align: center;
    margin-top: 1rem;
}
.small-guide {
    color: #64748b;
    font-size: 0.95rem;
    margin-bottom: 0.8rem;
}
div.stButton > button {
    width: 100%;
    min-height: 56px;
    font-size: 1.15rem;
    font-weight: 800;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

questions = [
    {
        "text": "2^3 × 2^4 을 간단히 하면?",
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
        "text": "y^{10} \div y^2 을 간단히 하면?",
        "latex": r"y^{10} \div y^2",
        "options": [r"y^{12}", r"y^5", r"y^8", r"y^{20}"],
        "answer": r"y^8",
        "explanation": "밑이 같을 때 나눗셈은 지수를 뺍니다. 10-2=8"
    },
    {
        "text": "(ab)^4 를 간단히 하면?",
        "latex": r"(ab)^4",
        "options": [r"ab^4", r"a^4b", r"a^4b^4", r"4ab"],
        "answer": r"a^4b^4",
        "explanation": "괄호 안의 각 문자에 지수 4를 곱해 줍니다."
    },
    {
        "text": "\left(\frac{x}{y}\right)^3 을 간단히 하면?",
        "latex": r"\left(\frac{x}{y}\right)^3",
        "options": [r"\frac{x}{y^3}", r"\frac{x^3}{y}", r"\frac{x^3}{y^3}", r"xy^3"],
        "answer": r"\frac{x^3}{y^3}",
        "explanation": "분자와 분모 각각에 3제곱을 적용합니다."
    },
]

if "score" not in st.session_state:
    st.session_state.score = 0
if "index" not in st.session_state:
    st.session_state.index = 0
if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = set()
if "finished" not in st.session_state:
    st.session_state.finished = False

def reset_quiz():
    st.session_state.score = 0
    st.session_state.index = 0
    st.session_state.wrong_questions = set()
    st.session_state.finished = False
    st.rerun()

def check_answer(selected_option: str):
    q = questions[st.session_state.index]
    idx = st.session_state.index

    if selected_option == q["answer"]:
        gain = 0 if idx in st.session_state.wrong_questions else 5
        st.session_state.score += gain

        if gain == 5:
            msg = "정답입니다! +5점"
        else:
            msg = "정답입니다! 이 문제는 이미 틀려서 점수는 추가되지 않습니다."

        st.markdown(f'<div class="feedback-ok">{msg}</div>', unsafe_allow_html=True)
        st.caption(f"해설: {q['explanation']}")
        time.sleep(1.0)

        if st.session_state.index < len(questions) - 1:
            st.session_state.index += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()
    else:
        st.session_state.score -= 5
        st.session_state.wrong_questions.add(idx)
        st.markdown('<div class="feedback-no">다시 풀어봅시다. -5점</div>', unsafe_allow_html=True)
        st.caption(f"힌트: {q['explanation']}")
        time.sleep(2.0)
        st.rerun()

if st.session_state.finished:
    st.markdown(
        f'<div class="score-box"><div class="score-title">최종 점수</div><div class="score-value">{st.session_state.score}</div></div>',
        unsafe_allow_html=True
    )
    st.success("퀴즈를 모두 마쳤습니다!")
    if st.session_state.score >= 20:
        st.balloons()
        st.write("아주 잘했어요! 지수법칙을 자신 있게 풀고 있네요.")
    elif st.session_state.score >= 5:
        st.write("좋아요! 조금만 더 연습하면 더 빨라질 거예요.")
    else:
        st.write("괜찮아요. 다시 풀면서 규칙을 익히면 금방 좋아집니다.")
    if st.button("처음부터 다시 시작", use_container_width=True):
        reset_quiz()
    st.stop()

q = questions[st.session_state.index]

st.markdown(
    f'<div class="score-box"><div class="score-title">현재 점수</div><div class="score-value">{st.session_state.score}</div></div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="progress-box">문제 {st.session_state.index + 1} / {len(questions)}</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="question-card">', unsafe_allow_html=True)
st.markdown("### 문제")
st.write(q["text"])
st.latex(q["latex"])
st.markdown('<div class="small-guide">번호를 누르면 바로 채점됩니다.</div>', unsafe_allow_html=True)
st.markdown("### 보기")

for i, opt in enumerate(q["options"], start=1):
    c1, c2 = st.columns([1.1, 8.9], gap="small")
    with c1:
        pressed = st.button(str(i), key=f"opt_{st.session_state.index}_{i}", use_container_width=True)
    with c2:
        st.latex(opt)
    if pressed:
        check_answer(opt)

st.markdown('</div>', unsafe_allow_html=True)
