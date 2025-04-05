from math import floor
from time import time
import streamlit as st


def rotl(x, k):
    return (x << k) | (x >> (64 - k))

def get():
    def _splitmix(x):
        x = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
        x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
        x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
        return x ^ (x >> 31)

    def _rotl(x, k):
        return ((x << k) | (x >> (64 - k))) & 0xFFFFFFFFFFFFFFFF

    s0 = _splitmix(floor(time()))
    s1 = _splitmix(s0)
    s1 ^= s0
    s0 = _rotl(s0, 24) ^ s1 ^ ((s1 << 16) & 0xFFFFFFFFFFFFFFFF)
    s1 = _rotl(s1, 37)
    return (s0 + s1) & 0xFFFFFFFFFFFFFFFF

def check():
    if st.session_state.get("answer") is None:
        st.error("정답을 먼저 생성해주세요.")
    elif int(t) == st.session_state.get("answer"):
        st.success("정답입니다!\nFlag는 `flag{}`입니다.".format(st.secrets["flag"]))
    else:
        st.error("틀렸습니다.\n정답은 `{}`였으나 다시 바뀝니다.".format(st.session_state.get("answer")))
        st.session_state.update({"answer": get()})

st.set_page_config(page_title="Streamlit으로 만든 간단한 퀴즈입니다!", layout="wide")

st.title("Streamlit으로 만든 간단한 퀴즈입니다!")
st.button("정답 생성", on_click=lambda: st.session_state.update({"answer": get()}))
c1, c2 = st.columns(2)
t = st.text_input("정답을 입력하세요", type="password")
st.button("제출", on_click=check)