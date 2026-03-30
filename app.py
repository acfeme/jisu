import time
import streamlit as st

st.set_page_config(page_title="지수법칙 퀴즈", page_icon="🎮", layout="centered")

st.markdown("""
<style>
.block-container {
    max-width: 780px;
    padding-top: 0.18rem;
    padding-bottom: 0.3rem;
}
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #fffef7 0%, #f8fbff 45%, #fdf2ff 100%);
}
.maker-badge {
    text-align: center;
    font-weight: 900;
    color: #7c3aed;
    background: linear-gradient(90deg, #f5f3ff, #eff6ff);
    border: 1.5px solid #c4b5fd;
    border-radius: 999px;
    padding: 0.18rem 0.55rem;
    margin-bottom: 0.2rem;
    font-size: 0.95rem;
}
.score-box {
    background: linear-gradient(135deg, #ec4899, #8b5cf6, #3b82f6);
    color: white;
    padding: 0.35rem 0.6rem;
    border-radius: 14px;
    text-align: center;
    margin-bottom: 0.22rem;
    border: 2px solid #ede9fe;
}
.score-title {
    font-size: 0.95rem;
    font-weight: 900;
}
.score-value {
    font-size: 2.3rem;
    font-weight: 900;
    line-height: 1.0;
    margin-top: 0.02rem;
    color: #fef08a;
}
.progress-box {
    background: linear-gradient(90deg, #fde68a, #fca5a5);
    border: 1.5px solid #fb7185;
    color: #7c2d12;
    padding: 0.22rem 0.55rem;
    border-radius: 11px;
    font-size: 1rem;
    font-weight: 900;
    text-align: center;
    margin-bottom: 0.22rem;
}
.question-card {
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    border: 2px solid #c4b5fd;
    border-radius: 16px;
    padding: 0.38rem 0.55rem 0.28rem 0.55rem;
    margin-bottom: 0.2rem;
}
.shake {
    animation: shake 0.35s ease-in-out 2;
    border-color: #f87171 !important;
}
@keyframes shake {
    0% { transform: translateX(0); }
    20% { transform: translateX(-6px); }
    40% { transform: translateX(6px); }
    60% { transform: translateX(-4px); }
    80% { transform: translateX(4px); }
    100% { transform: translateX(0); }
}
.section-title {
    font-size: 1.5rem;
    font-weight: 900;
    color: #1e293b;
    margin-bottom: 0.02rem;
}
.guide-box {
    color: #334155;
    font-size: 0.92rem;
    font-weight: 800;
    margin-top: 0.08rem;
    margin-bottom: 0.18rem;
    background: linear-gradient(90deg, #ecfeff, #eff6ff);
    border: 1.5px solid #93c5fd;
    border-radius: 10px;
    padding: 0.22rem 0.45rem;
}
.feedback-ok {
    background: linear-gradient(90deg, #dcfce7, #bbf7d0);
    border: 1.5px solid #22c55e;
    color: #166534;
    padding: 0.38rem;
    border-radius: 10px;
    font-size: 1.02rem;
    font-weight: 900;
    text-align: center;
    margin-top: 0.2rem;
}
.feedback-no {
    background: linear-gradient(90deg, #fee2e2, #fecaca);
    border: 1.5px solid #ef4444;
    color: #991b1b;
    padding: 0.38rem;
    border-radius: 10px;
    font-size: 1.02rem;
    font-weight: 900;
    text-align: center;
    margin-top: 0.2rem;
}
.explain-box {
    background: linear-gradient(90deg, #eff6ff, #eef2ff);
    border: 1.5px solid #93c5fd;
    color: #1e3a8a;
    padding: 0.28rem 0.45rem;
    border-radius: 9px;
    margin-top: 0.15rem;
    font-size: 0.95rem;
    font-weight: 700;
}
.final-box {
    background: linear-gradient(135deg, #f43f5e, #8b5cf6, #0ea5e9);
    color: white;
    padding: 0.5rem;
    border-radius: 16px;
    text-align: center;
    border: 2px solid #ddd6fe;
    margin-bottom: 0.25rem;
}
.final-title {
    font-size: 1rem;
    font-weight: 900;
}
.final-score {
    font-size: 3rem;
    font-weight: 900;
    color: #fef08a;
    line-height: 1.0;
    margin-top: 0.04rem;
}
.option-row {
    background: linear-gradient(90deg, #ffffff, #faf5ff);
    border: 1.5px solid #e9d5ff;
    border-radius: 11px;
    padding: 0.04rem 0.24rem;
    margin-bottom: 0.14rem;
}
div.stButton > button {
    width: 100%;
    min-height: 34px;
    font-size: 0.95rem;
    font-weight: 900;
    border-radius: 9px;
    border: 1.5px solid #cbd5e1;
    background: linear-gradient(180deg, #ffffff, #f8fafc);
    padding: 0rem 0.1rem;
}
div.stButton > button:hover {
    border: 1.5px solid #a855f7;
    color: #7c3aed;
    background: linear-gradient(180deg, #fdf4ff, #f5f3ff);
}
div[data-testid="stLatex"] {
    margin-top: -0.2rem;
    margin-bottom: -0.2rem;
}
p {
    margin-bottom: 0.08rem;
}
</style>
""", unsafe_allow_html=True)

questions = [
    {"latex": r"2^3 \times 2^4", "options": [r"2^{12}", r"2^7", r"2^1", r"4^7"], "answer": r"2^7", "explanation": "밑이 같을 때는 지수를 더합니다. 3+4=7"},
    {"latex": r"(x^2)^3", "options": [r"x^5", r"x^6", r"x^8", r"x^9"], "answer": r"x^6", "explanation": "거듭제곱의 거듭제곱은 지수를 곱합니다. 2×3=6"},
    {"latex": r"y^{10} \div y^2", "options": [r"y^{12}", r"y^5", r"y^8", r"y^{20}"], "answer": r"y^8", "explanation": "밑이 같을 때 나눗셈은 지수를 뺍니다. 10-2=8"},
    {"latex": r"(ab)^4", "options": [r"ab^4", r"a^4b", r"a^4b^4", r"4ab"], "answer": r"a^4b^4", "explanation": "괄호 안의 각 문자에 지수 4를 곱해 줍니다."},
    {"latex": r"\left(\frac{x}{y}\right)^3", "options": [r"\frac{x}{y^3}", r"\frac{x^3}{y}", r"\frac{x^3}{y^3}", r"xy^3"], "answer": r"\frac{x^3}{y^3}", "explanation": "분자와 분모 각각에 3제곱을 적용합니다."},
    {"latex": r"a^5 \times a", "options": [r"a^5", r"a^4", r"a^6", r"2a^5"], "answer": r"a^6", "explanation": "a는 a^1과 같으므로 5+1=6입니다."},
    {"latex": r"a^3 \div a^3", "options": [r"0", r"1", r"a", r"a^6"], "answer": r"1", "explanation": "같은 수를 나누면 1입니다."},
    {"latex": r"x^2 \div x^5", "options": [r"x^3", r"\frac{1}{x^7}", r"\frac{1}{x^3}", r"1"], "answer": r"\frac{1}{x^3}", "explanation": "뒤의 지수가 더 크면 분모로 보내서 5-2=3입니다."},
    {"latex": r"(-2a)^3", "options": [r"-6a^3", r"-8a^3", r"8a^3", r"-2a^3"], "answer": r"-8a^3", "explanation": "(-2)^3=-8 이고 a도 세 번 곱합니다."},
    {"latex": r"(3x^2)^2", "options": [r"6x^4", r"9x^2", r"9x^4", r"3x^4"], "answer": r"9x^4", "explanation": "3도 제곱하고 x^2도 제곱해서 9x^4입니다."},
    {"latex": r"a^2 \times a^x = a^{10}", "options": [r"5", r"8", r"12", r"20"], "answer": r"8", "explanation": "지수를 더하므로 2+x=10 입니다."},
    {"latex": r"(b^x)^3 = b^{15}", "options": [r"5", r"12", r"18", r"45"], "answer": r"5", "explanation": "지수를 곱하므로 3x=15 입니다."},
    {"latex": r"2^3 \times 5^3", "options": [r"7^3", r"10^3", r"10^6", r"10^9"], "answer": r"10^3", "explanation": "지수가 같으면 밑끼리 곱해서 (2×5)^3 입니다."},
    {"latex": r"x^8 \div (x^2)^3", "options": [r"x^3", r"x^2", r"x^6", r"x^{12}"], "answer": r"x^2", "explanation": "(x^2)^3=x^6 이고 x^8÷x^6=x^2 입니다."},
    {"latex": r"2^{10} \div 2^2 \div 2^3", "options": [r"2^{15}", r"2^5", r"2^8", r"2^0"], "answer": r"2^5", "explanation": "차례대로 지수를 빼면 10-2-3=5 입니다."},
    {"latex": r"(a^3b^2)^4", "options": [r"a^7b^6", r"a^{12}b^8", r"a^{12}b^2", r"a^3b^8"], "answer": r"a^{12}b^8", "explanation": "각 지수에 4를 곱합니다."},
    {"latex": r"\left(\frac{2}{x^3}\right)^3", "options": [r"\frac{6}{x^6}", r"\frac{8}{x^6}", r"\frac{8}{x^9}", r"\frac{2}{x^9}"], "answer": r"\frac{8}{x^9}", "explanation": "2^3=8 이고 (x^3)^3=x^9 입니다."},
    {"latex": r"(-x^2y^3)^2", "options": [r"-x^4y^6", r"x^4y^6", r"x^4y^5", r"x^2y^6"], "answer": r"x^4y^6", "explanation": "음수의 짝수 제곱은 양수입니다."},
    {"latex": r"3^4 + 3^4 + 3^4", "options": [r"3^{12}", r"9^4", r"3^5", r"3^7"], "answer": r"3^5", "explanation": "3^4가 3개이므로 3×3^4=3^5 입니다."},
    {"latex": r"4^3", "options": [r"2^5", r"2^6", r"2^8", r"2^{12}"], "answer": r"2^6", "explanation": "4=2^2 이므로 (2^2)^3=2^6 입니다."},
    {"latex": r"8^2 \times 4^3", "options": [r"2^{10}", r"2^{11}", r"2^{12}", r"2^{13}"], "answer": r"2^{12}", "explanation": "8=(2^3), 4=(2^2) 이므로 2^6×2^6=2^{12} 입니다."},
    {"latex": r"x^a \times x^2 = x^8", "options": [r"4", r"6", r"10", r"16"], "answer": r"6", "explanation": "a+2=8 이므로 a=6 입니다."},
    {"latex": r"(a^2)^b = a^{10}", "options": [r"5", r"8", r"12", r"20"], "answer": r"5", "explanation": "2b=10 이므로 b=5 입니다."},
    {"latex": r"\left(\frac{x^a}{y^2}\right)^3 = \frac{x^{12}}{y^6}", "options": [r"3", r"4", r"9", r"12"], "answer": r"4", "explanation": "3a=12 이므로 a=4 입니다."},
    {"latex": r"2^a \times 3^b = 72", "options": [r"4", r"5", r"6", r"7"], "answer": r"5", "explanation": "72=2^3×3^2 이므로 a+b=5 입니다."},
    {"latex": r"10^5 \div 10^2", "options": [r"10^7\text{ 배}", r"10^3\text{ 배}", r"3\text{ 배}", r"100\text{ 배}"], "answer": r"10^3\text{ 배}", "explanation": "같은 밑의 나눗셈이므로 10^(5-2)=10^3 입니다."},
    {"latex": r"(3 \times 10^5) \times 10^2", "options": [r"3 \times 10^3", r"3 \times 10^7", r"3 \times 10^{10}", r"300"], "answer": r"3 \times 10^7", "explanation": "10의 지수는 더해서 10^7 이 됩니다."},
    {"latex": r"2^{x+1}=8", "options": [r"1", r"2", r"3", r"4"], "answer": r"2", "explanation": "8=2^3 이므로 x+1=3 입니다."},
    {"latex": r"3^2 \times 9 = 3^n", "options": [r"2", r"3", r"4", r"5"], "answer": r"4", "explanation": "9=3^2 이므로 3^2×3^2=3^4 입니다."},
    {"latex": r"(x^2y^a)^3 = x^6y^{12}", "options": [r"3", r"4", r"9", r"36"], "answer": r"4", "explanation": "3a=12 이므로 a=4 입니다."}
]

if "score" not in st.session_state:
    st.session_state.score = 0
if "index" not in st.session_state:
    st.session_state.index = 0
if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = set()
if "finished" not in st.session_state:
    st.session_state.finished = False
if "shake" not in st.session_state:
    st.session_state.shake = False

def reset_quiz():
    st.session_state.score = 0
    st.session_state.index = 0
    st.session_state.wrong_questions = set()
    st.session_state.finished = False
    st.session_state.shake = False
    st.rerun()

def check_answer(selected_option: str):
    q = questions[st.session_state.index]
    idx = st.session_state.index
    if selected_option == q["answer"]:
        st.session_state.shake = False
        gain = 0 if idx in st.session_state.wrong_questions else 5
        st.session_state.score += gain
        msg = "🎉 정답입니다! +5점" if gain == 5 else "😊 정답입니다! 하지만 이 문제는 이미 틀려서 점수는 추가되지 않습니다."
        st.markdown(f'<div class="feedback-ok">{msg}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="explain-box">해설: {q["explanation"]}</div>', unsafe_allow_html=True)
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
        st.session_state.shake = True
        st.rerun()

if st.session_state.finished:
    st.markdown('<div class="maker-badge">이송원 선생님 제작</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="final-box"><div class="final-title">🏆 최종 점수</div><div class="final-score">{st.session_state.score}</div></div>', unsafe_allow_html=True)
    st.success("퀴즈를 모두 마쳤습니다!")
    if st.button("처음부터 다시 시작", use_container_width=True):
        reset_quiz()
    st.stop()

q = questions[st.session_state.index]

st.markdown('<div class="maker-badge">이송원 선생님 제작</div>', unsafe_allow_html=True)
st.markdown(f'<div class="score-box"><div class="score-title">🌟 현재 점수</div><div class="score-value">{st.session_state.score}</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="progress-box">🎯 문제 {st.session_state.index + 1} / {len(questions)}</div>', unsafe_allow_html=True)

shake_class = "shake" if st.session_state.shake else ""
st.markdown(f'<div class="question-card {shake_class}">', unsafe_allow_html=True)
st.markdown('<div class="section-title">문제</div>', unsafe_allow_html=True)
st.latex(q["latex"])

if st.session_state.shake:
    st.markdown('<div class="feedback-no">💡 다시 풀어봅시다. -5점</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="explain-box">힌트: {q["explanation"]}</div>', unsafe_allow_html=True)
    time.sleep(2.0)
    st.session_state.shake = False
    st.rerun()

st.markdown('<div class="guide-box">번호를 누르면 바로 채점됩니다.</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title" style="font-size:1.35rem; margin-top:0.02rem;">보기</div>', unsafe_allow_html=True)

for i, opt in enumerate(q["options"], start=1):
    st.markdown('<div class="option-row">', unsafe_allow_html=True)
    c1, c2 = st.columns([1.0, 5.0], gap="small")
    with c1:
        pressed = st.button(str(i), key=f"opt_{st.session_state.index}_{i}", use_container_width=True)
    with c2:
        st.latex(opt)
    st.markdown('</div>', unsafe_allow_html=True)
    if pressed:
        check_answer(opt)

st.markdown('</div>', unsafe_allow_html=True)
