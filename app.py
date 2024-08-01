# -*- coding: utf-8 -*-
import streamlit as st

# Add this at the beginning of your app
st.write("Debug: Application started")

def calculate_sliv(L, S):
    if L - 1 < 7:
        SLIV = 14 * (L - 1) + S
    else:
        SLIV = 14 * (14 - L + 1) + (14 - 1 - S)
    return SLIV

def reverse_sliv(SLIV):
    for L in range(1, 15):
        for S in range(0, 14):
            if calculate_sliv(L, S) == SLIV:
                return L, S
    return None, None

# Streamlit interface
st.title("SLIV 计算器")
st.write("Debug: Title displayed")

# Input L and S to calculate SLIV
st.header("计算 SLIV")
L = st.number_input("输入 L (1-14)", min_value=1, max_value=14, step=1)
S = st.number_input("输入 S (0-12)", min_value=0, max_value=12, step=1)
st.write(f"Debug: L = {L}, S = {S}")

if L + S <= 14:
    SLIV = calculate_sliv(L, S)
    st.write(f"计算得到的 SLIV 值: {SLIV}")
    st.write(f"Debug: SLIV calculated = {SLIV}")
else:
    st.write("L 和 S 的总和不能超过 14")
    st.write("Debug: Invalid L and S combination")

# Input SLIV to calculate L and S
st.header("反向计算 L 和 S")
input_SLIV = st.number_input("输入 SLIV 值", min_value=0)
st.write(f"Debug: Input SLIV = {input_SLIV}")

if input_SLIV:
    L, S = reverse_sliv(input_SLIV)
    if L is not None and S is not None:
        st.write(f"反向计算得到的 S: {S}, L: {L}")
        st.write(f"Debug: Reverse calculation successful, S = {S}, L = {L}")
    else:
        st.write("未找到有效的 L 和 S")
        st.write("Debug: Reverse calculation failed")

# Add this at the end of your app
st.write("Debug: Application finished")