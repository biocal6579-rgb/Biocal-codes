
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
        "Molarity (from moles)", "Molarity (from grams)", "Molarity (if solvent in Kg)","Molarity(if solvent in Liters)","Molarity by dilution",
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
    st.subheader("Mass Converter")

    value = st.number_input("Value", min_value=0.0)
    f = st.selectbox("From", ["kg", "g", "mg"])
    t = st.selectbox("To", ["kg", "g", "mg"])

    factors = {
        "kg": 1000,
        "g": 1,
        "mg": 0.001
    }

    if st.button("Calculate"):
        result = (value * factors[f]) / factors[t]
        st.success(f"Result = {result:.4f} {t}")




# =====================================================
# VOLUME
# =====================================================
elif st.session_state.page == "Volume":

    value = st.number_input("Value", min_value=0.0)

    f = st.selectbox("From", ["L", "mL", "µL"])

    t = st.selectbox("To", ["L", "mL", "µL"])

    factors = {
        "L": 1,
        "mL": 0.001,
        "µL": 0.000001
    }

    if st.button("Calculate"):
        result = (value * factors[f]) / factors[t]
        st.success(f"Result={result:.6f} {t}")



# =====================================================
# TEMPERATURE
# =====================================================
elif st.session_state.page == "Temperature":
    st.subheader("Temperature Converter")

    temp = st.number_input(
        "Temperature value",
        key="temp_value"
    )

    mode = st.selectbox(
        "Conversion",
        ["C → K", "K → C", "C → F", "F → C"],
        key="temp_mode"
    )

    if st.button("Convert", key="temp_btn"):
        if mode == "C → K":
            st.success(f"result={temp + 273.15:.2f} K")

        elif mode == "K → C":
            st.success(f"result={temp - 273.15:.2f} °C")

        elif mode == "C → F":
            st.success(f"result={temp * 9/5 + 32:.2f} °F")

        elif mode == "F → C":
            st.success(f"result={((temp - 32) * 5/9):.2f} °C")

# =====================================================
# DENSITY
# =====================================================
elif st.session_state.page == "Density":
    st.subheader(" Density")

    m = st.number_input("Mass (g)", min_value=0.0)
    v = st.number_input("Volume (mL)", min_value=0.0)

    if st.button("Calculate"):
        if v == 0:
            st.error("Volume cannot be zero")
        else:
            density = m / v
            st.success(f"Density = {density:.4f} g/mL")


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
    st.subheader("Molarity (from moles)")
    st.caption("Formula: M = moles / volume (L)")

    n = st.number_input("Moles of solute (mol)", min_value=0.0)
    V = st.number_input("Volume of solution (L)", min_value=0.0)

    if st.button("Calculate"):
        if V == 0:
            st.error("Volume cannot be zero")
        else:
            M = n / V
            st.success(f"Molarity = {M:.4f} mol/L (M)")


elif st.session_state.page == "Molarity (from grams)":
    st.subheader(" Grams of Substance to Add")
    st.caption("Formula: grams = Molarity × Molecular weight × Volume (L)")

    M = st.number_input(
        "Molarity (M)",
        min_value=0.0,
        key="grams_M"
    )

    MW = st.number_input(
        "Molecular weight (g/mol)",
        min_value=0.0,
        key="grams_MW"
    )

    V = st.number_input(
        "Volume of solution (L)",
        min_value=0.0,
        key="grams_V"
    )

    if st.button("Calculate Grams", key="grams_btn"):
        if MW == 0 or V == 0:
            st.error("Molecular weight and volume cannot be zero")
        else:
            grams = M * MW * V
            st.success(f"Grams required = {grams:.4f} g")


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
    st.subheader("Normality")
    st.caption("Formula: N = gram equivalents / volume (L)")

    ge = st.number_input(
        "Gram equivalents",
        min_value=0.0,
        key="normality_ge"
    )

    V = st.number_input(
        "Volume of solution (L)",
        min_value=0.0,
        key="normality_volume"
    )

    if st.button("Calculate Normality", key="normality_btn"):
        if V == 0:
            st.error("Volume cannot be zero")
        else:
            st.success(f"Normality = {ge / V:.4f} N")


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
    st.subheader("🔁 Molarity to Normality")
    st.caption("Formula: N = M × n-factor")

    M = st.number_input("Molarity (M)", min_value=0.0)
    n = st.number_input("n-factor", min_value=0.0)

    if st.button("Calculate"):
        st.success(f"Normality = {M * n:.4f} N")


# =====================================================
# MOLALITY if solvent in kg
# =====================================================
elif st.session_state.page == "Molarity (if solvent in Kg)":
    st.subheader("Molarity (if solvent in Kg)")
    st.caption("Formula: m = moles / mass of solvent (kg)")

    n = st.number_input(
        "Moles of solute (mol)",
        min_value=0.0,
        key="molality_moles"
    )

    kg = st.number_input(
        "Mass of solvent (kg)",
        min_value=0.0,
        key="molality_kg"
    )

    if st.button("Calculate Molality", key="molality_btn"):
        if kg == 0:
            st.error("Solvent mass cannot be zero")
        else:
            st.success(f"Molality = {n / kg:.4f} m")
# =====================================================
# MOLALITY if solvent in Liters
# =====================================================
elif st.session_state.page == "Molarity(if solvent in Liters)":
    st.caption("Formula: M = moles / volume (L)")

    moles = st.number_input("Moles of solute (mol)", min_value=0.0)
    volume = st.number_input("Volume of solvent (L)", min_value=0.0)

    if st.button("Calculate Molarity"):
        if volume == 0:
            st.error("Volume cannot be zero")
        else:
            M = moles / volume
            st.success(f"Molarity = {M:.3f} M")




# =====================================================
# PERCENTAGE
# =====================================================
elif st.session_state.page == "Percentage Solution":
    st.subheader(" Percentage Solution")

    ptype = st.selectbox(
        "Select Percentage Type",
        ["%(w/v)", "%(v/v)", "%(m/v)"]
    )

    st.markdown("---")

    if ptype == "%(w/v)":
        grams = st.number_input("Grams of solute (g)", min_value=0.0)
        volume = st.number_input("Volume of solution (mL)", min_value=0.0)

        if st.button("Calculate %(w/v)"):
            if volume == 0:
                st.error("Volume cannot be zero")
            else:
                percent = (grams / volume) * 100
                st.success(f"%(w/v) = {percent:.2f} %")

    elif ptype == "%(v/v)":
        vol_solute = st.number_input("Volume of solute (mL)", min_value=0.0)
        vol_solution = st.number_input("Volume of solution (mL)", min_value=0.0)

        if st.button("Calculate %(v/v)"):
            if vol_solution == 0:
                st.error("Solution volume cannot be zero")
            else:
                percent = (vol_solute / vol_solution) * 100
                st.success(f"%(v/v) = {percent:.2f} %")

    elif ptype == "%(m/v)":
        mass = st.number_input("Mass of solute (g)", min_value=0.0)
        volume = st.number_input("Volume of solution (mL)", min_value=0.0)

        if st.button("Calculate %(m/v)"):
            if volume == 0:
                st.error("Volume cannot be zero")
            else:
                percent = (mass / volume) * 100
                st.success(f"%(m/v) = {percent:.2f} %")

# =====================================================
# MOLES
# =====================================================
elif st.session_state.page =="Moles Calculator":

    st.subheader(" Moles Calculator")
    st.caption("Formula: moles (n) = mass (g) / molar mass (g·mol⁻¹)")

    g = st.number_input(
        "Mass of substance (g)",
        min_value=0.0,
        key="moles_mass"
    )

    mm = st.number_input(
        "Molar mass (g/mol)",
        min_value=0.0,
        key="moles_mm"
    )

    if st.button("Calculate Moles", key="moles_btn"):
        if mm == 0:
            st.error("Molar mass cannot be zero")
        else:
            result = g / mm
            st.success(f"Moles = {result:.4f} mol")


# =====================================================
# DNA RNA
# =====================================================
elif st.session_state.page == "DNA Concentration":

    st.subheader("DNA Concentration")
    st.caption("Formula: DNA (µg/mL) = A260 × 50 × Dilution factor")

    A = st.number_input(
        "Absorbance at 260 nm (A260)",
        min_value=0.0,
        key="dna_a260"
    )

    d = st.number_input(
        "Dilution factor",
        min_value=1.0,
        key="dna_dilution"
    )

    if st.button("Calculate DNA Concentration", key="dna_btn"):
        result = A * 50 * d
        st.success(f"DNA Concentration = {result:.2f} µg/mL")


elif st.session_state.page == "RNA Concentration":

    st.subheader("RNA Concentration")
    st.caption("Formula: RNA (µg/mL) = A260 × 40 × Dilution factor")

    A = st.number_input(
        "Absorbance at 260 nm (A260)",
        min_value=0.0,
        key="rna_a260"
    )

    d = st.number_input(
        "Dilution factor",
        min_value=1.0,
        key="rna_dilution"
    )

    if st.button("Calculate RNA Concentration", key="rna_btn"):
        result = A * 40 * d
        st.success(f"RNA Concentration = {result:.2f} µg/mL")


elif st.session_state.page == "DNA Purity":

    st.subheader("🧬 DNA Purity")
    st.caption("Formula: Purity ratio = A260 / A280")

    a260 = st.number_input(
        "Absorbance at 260 nm (A260)",
        min_value=0.0,
        key="purity_a260"
    )

    a280 = st.number_input(
        "Absorbance at 280 nm (A280)",
        min_value=0.0,
        key="purity_a280"
    )

    if st.button("Calculate Purity", key="purity_btn"):
        if a280 == 0:
            st.error("A280 cannot be zero")
        else:
            ratio = a260 / a280
            st.success(f"DNA Purity (A260/A280) = {ratio:.2f} (unitless)")


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
    st.subheader("🧪 pH Calculator")
    st.caption("Formula: pH = −log₁₀[H⁺]")

    h = st.number_input("[H⁺] concentration", min_value=1e-14, key="ph_h")

    if st.button("Calculate pH", key="ph_btn"):
        st.success(f"pH = {-math.log10(h):.4f}")
# =====================================================
# HARDY
# =====================================================
elif st.session_state.page == "Hardy–Weinberg":
    p=st.slider("p",0.0,1.0,0.5)
    q=1-p
    if st.button("Calculate"):
        st.success({"p²":p*p,"2pq":2*p*q,"q²":q*q})


