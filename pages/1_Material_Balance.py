import streamlit as st

st.title("Material Balance: Binary Separator")
st.caption("Overall: F = D + B   |   Component: F·xF = D·xD + B·xB")

c1, c2 = st.columns(2)
F = c1.number_input("Feed rate F (kg/h)", min_value=0.0, value=100.0)
xF = c1.number_input("Feed fraction xF", 0.0, 1.0, 0.50)
xD = c2.number_input("Top product fraction xD", 0.0, 1.0, 0.95)
xB = c2.number_input("Bottom product fraction xB", 0.0, 1.0, 0.05)

if st.button("Calculate"):
    if not (xB < xF < xD):
        st.error("Requires xB < xF < xD.")
    else:
        D = F * (xF - xB) / (xD - xB)
        B = F - D
        a, b = st.columns(2)
        a.metric("Top product D (kg/h)", f"{D:.2f}")
        b.metric("Bottom product B (kg/h)", f"{B:.2f}")
        err = F * xF - (D * xD + B * xB)
        st.write(f"Component balance closure error: {err:.2e}")
