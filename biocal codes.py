
import streamlit as st
import math

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Biocal",
    page_icon="🧪",
    layout="centered"
)

# =====================================================
# SESSION STATE
# =====================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_home():
    st.session_state.page = "home"

def go_calc(name):
    st.session_state.page = name

# =====================================================
# MOBILE SAFE CSS
# =====================================================
st.markdown("""
<style>
.stButton > button {
    width: 100%;
    background-color: #1565C0;
    color: white;
    font-size: 16px;
    border-radius: 14px;
    padding: 12px;
}
.stSelectbox, .stNumberInput {
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.title("🧪 Biocal")
st.caption("Daily use laboratory calculations")

# =====================================================
# HOME
# =====================================================
if st.session_state.page == "home":
    tools = [
        "Mass", "Volume", "Temperature", "Density",
        "C1V1 Dilution",
        "Molarity (from moles)", "Molarity (from grams)", "Molarity by dilution",
        "Normality", "Normality by dilution", "Molarity → Normality",
        "Molality",
        "Percentage Solution",
        "Moles Calculator",
        "DNA Concentration", "RNA Concentration", "DNA Purity",
        "Osmotic Pressure",
        "pH",
        "Hardy–Weinberg"
    ]

    choice = st.selectbox("Select Calculator", tools)

    if st.button("➡️ Open"):
        go_calc(choice)

# =====================================================
# BACK BUTTON
# =====================================================
if st.session_state.page != "home":
    if st.button("⬅️ Back"):
        go_home()
    st.divider()

# =====================================================
# MASS
# =====================================================
if st.session_state.page == "Mass":
    value = st.number_input("Value")
    f = st.selectbox("From", ["kg","g","mg"])
    t = st.selectbox("To", ["kg","g","mg"])
    factors = {"kg":1000,"g":1,"mg":0.001}
    if st.button("Calculate"):
        st.success((value*factors[f])/factors[t])

# =====================================================
# VOLUME
# =====================================================
elif st.session_state.page == "Volume":
    value = st.number_input("Value")
    f = st.selectbox("From", ["L","mL","µL"])
    t = st.selectbox("To", ["L","mL","µL"])
    factors = {"L":1,"mL":0.001,"µL":0.000001}
    if st.button("Calculate"):
        st.success((value*factors[f])/factors[t])

# =====================================================
# TEMPERATURE
# =====================================================
elif st.session_state.page == "Temperature":
    temp = st.number_input("Temperature")
    mode = st.selectbox("Conversion", ["C→K","K→C","C→F","F→C"])
    if st.button("Convert"):
        if mode=="C→K": st.success(temp+273.15)
        elif mode=="K→C": st.success(temp-273.15)
        elif mode=="C→F": st.success(temp*9/5+32)
        elif mode=="F→C": st.success((temp-32)*5/9)

# =====================================================
# DENSITY
# =====================================================
elif st.session_state.page == "Density":
    m = st.number_input("Mass (g)")
    v = st.number_input("Volume (mL)")
    if st.button("Calculate"):
        st.success(m/v)

# =====================================================
# C1V1
# =====================================================
elif st.session_state.page == "C1V1 Dilution":
    C1=st.number_input("C₁",0.0)
    V1=st.number_input("V₁",0.0)
    C2=st.number_input("C₂",0.0)
    V2=st.number_input("V₂",0.0)
    if st.button("Calculate"):
        if C1==0: st.success((C2*V2)/V1)
        elif V1==0: st.success((C2*V2)/C1)
        elif C2==0: st.success((C1*V1)/V2)
        elif V2==0: st.success((C1*V1)/C2)

# =====================================================
# MOLARITY
# =====================================================
elif st.session_state.page == "Molarity (from moles)":
    n=st.number_input("Moles")
    V=st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.success(n/V)

elif st.session_state.page == "Molarity (from grams)":
    g=st.number_input("molarity")
    mm=st.number_input("Molecular weight ")
    V=st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.success((g/mm)/V)

elif st.session_state.page == "Molarity by dilution":
    M1=st.number_input("M₁",0.0)
    V1=st.number_input("V₁",0.0)
    M2=st.number_input("M₂",0.0)
    V2=st.number_input("V₂",0.0)
    if st.button("Calculate"):
        if M1==0: st.success((M2*V2)/V1)
        elif V1==0: st.success((M2*V2)/M1)
        elif M2==0: st.success((M1*V1)/V2)
        elif V2==0: st.success((M1*V1)/M2)

# =====================================================
# NORMALITY
# =====================================================
elif st.session_state.page == "Normality":
    ge=st.number_input("Gram equivalents")
    V=st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.success(ge/V)

elif st.session_state.page == "Normality by dilution":
    N1=st.number_input("N₁",0.0)
    V1=st.number_input("V₁",0.0)
    N2=st.number_input("N₂",0.0)
    V2=st.number_input("V₂",0.0)
    if st.button("Calculate"):
        if N1==0: st.success((N2*V2)/V1)
        elif V1==0: st.success((N2*V2)/N1)
        elif N2==0: st.success((N1*V1)/V2)
        elif V2==0: st.success((N1*V1)/N2)

elif st.session_state.page == "Molarity → Normality":
    M=st.number_input("Molarity")
    n=st.number_input("n-factor")
    if st.button("Calculate"):
        st.success(M*n)

# =====================================================
# MOLALITY
# =====================================================
elif st.session_state.page == "Molality if solvent is in kg":
    n=st.number_input("Moles")
    kg=st.number_input("Solvent mass (kg)")
    if st.button("Calculate"):
        st.success(n/kg)

# =====================================================
# PERCENTAGE
# =====================================================
    st.subheader("Percentage Solutions")

    option = st.selectbox(
        "Select type",
        ["%(w/v)", "%(v/v)", "%(m/v)"]
    )

    if option == "%(w/v)":
        grams = st.number_input("Grams of solute (g)", min_value=0.0)
        volume = st.number_input("Volume of solution (mL)", min_value=0.0)

        if st.button("Calculate"):
            if volume > 0:
                percent = (grams / volume) * 100
                st.success(f"%(w/v) = {percent:.2f} %")

    elif option == "%(v/v)":
        vol_solute = st.number_input("Volume of solute (mL)", min_value=0.0)
        vol_solution = st.number_input("Volume of solution (mL)", min_value=0.0)

        if st.button("Calculate"):
            if vol_solution > 0:
                percent = (vol_solute / vol_solution) * 100
                st.success(f"%(v/v) = {percent:.2f} %")

    elif option == "%(m/v)":
        mass = st.number_input("Mass of solute (g)", min_value=0.0)
        volume = st.number_input("Volume of solution (mL)", min_value=0.0)

        if st.button("Calculate"):
            if volume > 0:
                percent = (mass / volume) * 100
                st.success(f"%(m/v) = {percent:.2f} %")


# =====================================================
# MOLES
# =====================================================
elif st.session_state.page == "Moles Calculator":
    g=st.number_input("Mass (g)")
    mm=st.number_input("Molar mass")
    if st.button("Calculate"):
        st.success(g/mm)

# =====================================================
# DNA RNA
# =====================================================
elif st.session_state.page == "DNA Concentration":
    A=st.number_input("A260")
    d=st.number_input("Dilution",1.0)
    if st.button("Calculate"):
        st.success(A*50*d)

elif st.session_state.page == "RNA Concentration":
    A=st.number_input("A260")
    d=st.number_input("Dilution",1.0)
    if st.button("Calculate"):
        st.success(A*40*d)

elif st.session_state.page == "DNA Purity":
    a260=st.number_input("A260")
    a280=st.number_input("A280")
    if st.button("Calculate"):
        st.success(a260/a280)

# =====================================================
# OSMOTIC
# =====================================================
elif st.session_state.page == "Osmotic Pressure":
    i=st.number_input("i")
    M=st.number_input("M")
    T=st.number_input("T (K)")
    if st.button("Calculate"):
        st.success(i*M*0.0821*T)

# =====================================================
# pH
# =====================================================
elif st.session_state.page == "pH":
    h=st.number_input("[H⁺]")
    if st.button("Calculate"):
        st.success(-math.log10(h))

# =====================================================
# HARDY
# =====================================================
elif st.session_state.page == "Hardy–Weinberg":
    p=st.slider("p",0.0,1.0,0.5)
    q=1-p
    if st.button("Calculate"):
        st.success({"p²":p*p,"2pq":2*p*q,"q²":q*q})


