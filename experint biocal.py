import streamlit as st
import math

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Biocal - Lab Companion",
    page_icon="🧪",
    layout="centered"
)

# =====================================================
# INITIALIZE STATE & NAVIGATION
# =====================================================
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "Home"
if "selected_calc" not in st.session_state:
    st.session_state.selected_calc = None


def nav_to_tab(tab_name):
    st.session_state.current_tab = tab_name
    st.session_state.selected_calc = None


def open_calculator(calc_name):
    st.session_state.selected_calc = calc_name


def close_calculator():
    st.session_state.selected_calc = None


# =====================================================
# GLOBAL MODERN DARK THEME CSS
# =====================================================
st.markdown("""
<style>
    .stApp, .main, div[data-testid="stAppViewContainer"] {
        background-color: #0B1315 !important;
        color: #E2E8F0;
    }
    .biocal-banner {
        background: linear-gradient(135deg, #38BDF8 0%, #34D399 100%);
        border-radius: 24px;
        padding: 30px;
        color: #0F172A;
        margin-bottom: 25px;
        position: relative;
        box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.15);
    }
    .biocal-banner h1 {
        margin: 0;
        font-size: 32px;
        font-weight: 800;
        color: #0F172A !important;
    }
    .biocal-banner p {
        margin: 5px 0 0 0;
        opacity: 0.9;
        font-size: 15px;
        font-weight: 500;
    }
    div[data-baseweb="input"] {
        background-color: #1E293B !important;
        border-radius: 16px !important;
        border: 1px solid #334155 !important;
    }
    div[data-baseweb="input"] input {
        color: #F8FAFC !important;
    }
    .section-title {
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 1px;
        color: #64748B;
        text-transform: uppercase;
        margin: 25px 0 12px 0;
    }
    .calc-card {
        background-color: #131C2E;
        border: 1px solid #1E293B;
        border-radius: 20px;
        padding: 22px;
        height: 140px;
        transition: all 0.25s ease;
        margin-bottom: 10px;
    }
    .calc-icon {
        font-size: 24px;
        margin-bottom: 8px;
    }
    .calc-name {
        font-size: 15px;
        font-weight: 600;
        color: #F8FAFC;
        margin-bottom: 4px;
    }
    .calc-desc {
        font-size: 12px;
        color: #64748B;
    }
    .convert-section {
        background-color: #131C2E;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #1E293B;
    }
    .convert-header {
        font-size: 16px;
        font-weight: 600;
        color: #F8FAFC;
        margin-bottom: 15px;
    }
    .stButton > button {
        width: 100%;
        background-color: #1E293B;
        color: #E2E8F0;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 10px;
        font-size: 15px;
    }
    .stButton > button:hover {
        border-color: #38BDF8 !important;
        color: #38BDF8 !important;
    }
    .bottom-nav-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #0F172A;
        border-top: 1px solid #1E293B;
        padding: 10px 0;
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

# =====================================================
# GRID CALCULATORS CONFIGURATION DATA
# =====================================================
tools_config = [
    {"name": "Mass", "desc": "kg, g, mg conversions", "icon": "⚖️"},
    {"name": "Volume", "desc": "L, mL, µL conversions", "icon": "🧪"},
    {"name": "Temperature", "desc": "C, K, F parameters", "icon": "🌡️"},
    {"name": "Density", "desc": "Mass per volume scale", "icon": "📊"},
    {"name": "C1V1 Dilution", "desc": "Standard stock titration", "icon": "💧"},
    {"name": "Molarity (from moles)", "desc": "Moles solute per volume", "icon": "🧬"},
    {"name": "Molarity (from grams)", "desc": "Grams solute per volume", "icon": "🔬"},
    {"name": "Molarity by dilution", "desc": "M₁V₁ = M₂V₂ formulas", "icon": "🧪"},
    {"name": "Normality", "desc": "Gram equivalents calculations", "icon": "⚗️"},
    {"name": "Normality by dilution", "desc": "N₁V₁ = N₂V₂ tracking", "icon": "💧"},
    {"name": "Molarity → Normality", "desc": "Using valence n-factors", "icon": "🔄"},
    {"name": "Molality", "desc": "Moles per solvent mass", "icon": "🧪"},
    {"name": "Percentage Solution", "desc": "w/v, v/v ratio outputs", "icon": "📈"},
    {"name": "Moles Calculator", "desc": "Mass divided by molar mass", "icon": "🧮"},
    {"name": "DNA Concentration", "desc": "A260 absorbance factor", "icon": "☀️"},
    {"name": "RNA Concentration", "desc": "A260 factor matrix", "icon": "🧬"},
    {"name": "DNA Purity", "desc": "A260 / A280 pure ratio", "icon": "✨"},
    {"name": "Osmotic Pressure", "desc": "Van 't Hoff equation state", "icon": "💥"},
    {"name": "pH", "desc": "Negative log H+ metric", "icon": "🧪"},
    {"name": "Hardy–Weinberg", "desc": "Population equilibrium mapping", "icon": "🧬"}
]

# =====================================================
# APP CONTROL LOGIC / ROUTING
# =====================================================

if st.session_state.selected_calc:
    # -------------------------------------------------
    # INDIVIDUAL CALCULATOR CALCULATION INTERFACES
    # -------------------------------------------------
    calc_page = st.session_state.selected_calc

    cols = st.columns([1, 5])
    with cols[0]:
        if st.button("⬅️ Back"):
            close_calculator()
            st.rerun()
    with cols[1]:
        st.subheader(f" {calc_page}")
    st.divider()

    # YOUR EXACT UNTOUCHED FORMULAS BELOW:
    if calc_page == "Mass":
        value = st.number_input("Value")
        f = st.selectbox("From", ["kg", "g", "mg"])
        t = st.selectbox("To", ["kg", "g", "mg"])
        factors = {"kg": 1000, "g": 1, "mg": 0.001}
        if st.button("Calculate"):
            st.success((value * factors[f]) / factors[t])

    elif calc_page == "Volume":
        value = st.number_input("Value")
        f = st.selectbox("From", ["L", "mL", "µL"])
        t = st.selectbox("To", ["L", "mL", "µL"])
        factors = {"L": 1, "mL": 0.001, "µL": 0.000001}
        if st.button("Calculate"):
            st.success((value * factors[f]) / factors[t])

    elif calc_page == "Temperature":
        temp = st.number_input("Temperature")
        mode = st.selectbox("Conversion", ["C→K", "K→C", "C→F", "F→C"])
        if st.button("Convert"):
            if mode == "C→K":
                st.success(temp + 273.15)
            elif mode == "K→C":
                st.success(temp - 273.15)
            elif mode == "C→F":
                st.success(temp * 9 / 5 + 32)
            elif mode == "F→C":
                st.success((temp - 32) * 5 / 9)

    elif calc_page == "Density":
        m = st.number_input("Mass (g)")
        v = st.number_input("Volume (mL)")
        if st.button("Calculate"):
            st.success(m / v)

    elif calc_page == "C1V1 Dilution":
        C1 = st.number_input("C₁", 0.0)
        V1 = st.number_input("V₁", 0.0)
        C2 = st.number_input("C₂", 0.0)
        V2 = st.number_input("V₂", 0.0)
        if st.button("Calculate"):
            if C1 == 0:
                st.success((C2 * V2) / V1)
            elif V1 == 0:
                st.success((C2 * V2) / C1)
            elif C2 == 0:
                st.success((C1 * V1) / V2)
            elif V2 == 0:
                st.success((C1 * V1) / C2)

    elif calc_page == "Molarity (from moles)":
        n = st.number_input("Moles")
        V = st.number_input("Volume (L)")
        if st.button("Calculate"):
            st.success(n / V)

    elif calc_page == "Molarity (from grams)":
        g = st.number_input("Grams")
        mm = st.number_input("Molar mass")
        V = st.number_input("Volume (L)")
        if st.button("Calculate"):
            st.success((g / mm) / V)

    elif calc_page == "Molarity by dilution":
        M1 = st.number_input("M₁", 0.0)
        V1 = st.number_input("V₁", 0.0)
        M2 = st.number_input("M₂", 0.0)
        V2 = st.number_input("V₂", 0.0)
        if st.button("Calculate"):
            if M1 == 0:
                st.success((M2 * V2) / V1)
            elif V1 == 0:
                st.success((M2 * V2) / M1)
            elif M2 == 0:
                st.success((M1 * V1) / V2)
            elif V2 == 0:
                st.success((M1 * V1) / M2)

    elif calc_page == "Normality":
        ge = st.number_input("Gram equivalents")
        V = st.number_input("Volume (L)")
        if st.button("Calculate"):
            st.success(ge / V)

    elif calc_page == "Normality by dilution":
        N1 = st.number_input("N₁", 0.0)
        V1 = st.number_input("V₁", 0.0)
        N2 = st.number_input("N₂", 0.0)
        V2 = st.number_input("V₂", 0.0)
        if st.button("Calculate"):
            if N1 == 0:
                st.success((N2 * V2) / V1)
            elif V1 == 0:
                st.success((N2 * V2) / N1)
            elif N2 == 0:
                st.success((N1 * V1) / V2)
            elif V2 == 0:
                st.success((N1 * V1) / N2)

    elif calc_page == "Molarity → Normality":
        M = st.number_input("Molarity")
        n = st.number_input("n-factor")
        if st.button("Calculate"):
            st.success(M * n)

    elif calc_page == "Molality":
        n = st.number_input("Moles")
        kg = st.number_input("Solvent mass (kg)")
        if st.button("Calculate"):
            st.success(n / kg)

    elif calc_page == "Percentage Solution":
        a = st.number_input("Solute")
        b = st.number_input("Solution")
        if st.button("Calculate"):
            st.success((a / b) * 100)

    elif calc_page == "Moles Calculator":
        g = st.number_input("Mass (g)")
        mm = st.number_input("Molar mass")
        if st.button("Calculate"):
            st.success(g / mm)

    elif calc_page == "DNA Concentration":
        A = st.number_input("A260")
        d = st.number_input("Dilution", 1.0)
        if st.button("Calculate"):
            st.success(A * 50 * d)

    elif calc_page == "RNA Concentration":
        A = st.number_input("A260")
        d = st.number_input("Dilution", 1.0)
        if st.button("Calculate"):
            st.success(A * 40 * d)

    elif calc_page == "DNA Purity":
        a260 = st.number_input("A260")
        a280 = st.number_input("A280")
        if st.button("Calculate"):
            st.success(a260 / a280)

    elif calc_page == "Osmotic Pressure":
        i = st.number_input("i")
        M = st.number_input("M")
        T = st.number_input("T (K)")
        if st.button("Calculate"):
            st.success(i * M * 0.0821 * T)

    elif calc_page == "pH":
        h = st.number_input("[H⁺]")
        if st.button("Calculate"):
            st.success(-math.log10(h))

    elif calc_page == "Hardy–Weinberg":
        p = st.slider("p", 0.0, 1.0, 0.5)
        q = 1 - p
        if st.button("Calculate"):
            st.success({"p²": p * p, "2pq": 2 * p * q, "q²": q * q})

else:
    # -------------------------------------------------
    # NAVIGATION TABS BASE VIEWS
    # -------------------------------------------------
    if st.session_state.current_tab == "Home":
        # Layout Banner top header card
        st.markdown("""
        <div class="biocal-banner">
            <h1>Biocal</h1>
            <p>Lab Companion</p>
            <div style="font-size: 12px; opacity:0.8; margin-top: 10px;">✨ 20+ scientific calculators for biotech & research</div>
        </div>
        """, unsafe_allow_html=True)

        # Live Search Bar field
        search_query = st.text_input("🔍 Search calculators...", placeholder="Search calculators...")

        # Recent Search elements row
        st.markdown('<div class="section-title">🕒 Recent</div>', unsafe_allow_html=True)
        rec_col1, rec_col2, _ = st.columns([2, 1.5, 4])
        with rec_col1:
            if st.button("Percentage Solution", key="rec_pct"):
                open_calculator("Percentage Solution")
                st.rerun()
        with rec_col2:
            if st.button("Molarity", key="rec_mol"):
                open_calculator("Molarity (from moles)")
                st.rerun()

        # Generate Cards Display Grid System
        st.markdown('<div class="section-title">All Calculators</div>', unsafe_allow_html=True)
        filtered_tools = [t for t in tools_config if
                          search_query.lower() in t["name"].lower() or search_query.lower() in t["desc"].lower()]

        for idx in range(0, len(filtered_tools), 2):
            grid_cols = st.columns(2)

            # Left Card
            with grid_cols[0]:
                t_item = filtered_tools[idx]
                st.markdown(f"""
                <div class="calc-card">
                    <div class="calc-icon">{t_item['icon']}</div>
                    <div class="calc-name">{t_item['name']}</div>
                    <div class="calc-desc">{t_item['desc']}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Open {t_item['name']}", key=f"grid_btn_{t_item['name']}", use_container_width=True):
                    open_calculator(t_item['name'])
                    st.rerun()

            # Right Card
            with grid_cols[1]:
                if idx + 1 < len(filtered_tools):
                    t_item = filtered_tools[idx + 1]
                    st.markdown(f"""
                    <div class="calc-card">
                        <div class="calc-icon">{t_item['icon']}</div>
                        <div class="calc-name">{t_item['name']}</div>
                        <div class="calc-desc">{t_item['desc']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Open {t_item['name']}", key=f"grid_btn_{t_item['name']}", use_container_width=True):
                        open_calculator(t_item['name'])
                        st.rerun()

    elif st.session_state.current_tab == "Convert":
        st.markdown('<div class="section-title">🔄 Standard Conversions</div>', unsafe_allow_html=True)

        # Length Module
        st.markdown('<div class="convert-section"><div class="convert-header">📏 Length</div>', unsafe_allow_html=True)
        l_val = st.number_input("Enter value", key="len_in", min_value=0.0)
        l_f = st.selectbox("From", ["Kilometers (km)", "Meters (m)"], key="len_from")
        l_t = st.selectbox("To", ["Meters (m)", "Kilometers (km)"], key="len_to")
        if st.button("Convert Length"):
            res = l_val * 1000 if "km" in l_f.lower() else l_val / 1000
            st.success(f"Result: {res}")
        st.markdown('</div>', unsafe_allow_html=True)

        # Temperature Module
        st.markdown('<div class="convert-section"><div class="convert-header">🌡️ Temperature</div>',
                    unsafe_allow_html=True)
        t_val = st.number_input("Enter value", key="temp_in")
        t_f = st.selectbox("From", ["Celsius (°C)", "Fahrenheit (°F)"], key="temp_from")
        t_t = st.selectbox("To", ["Fahrenheit (°F)", "Celsius (°C)"], key="temp_to")
        if st.button("Convert Temperature"):
            res = (t_val * 9 / 5) + 32 if "celsius" in t_f.lower() else (t_val - 32) * 5 / 9
            st.success(f"Result: {res}")
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.current_tab == "History":
        st.markdown('<div class="section-title">⏱️ Calculation History</div>', unsafe_allow_html=True)
        st.info("Your localized session calculation history logs will appear here.")

    elif st.session_state.current_tab == "Settings":
        st.markdown('<div class="section-title">⚙️ App Settings</div>', unsafe_allow_html=True)
        st.toggle("High Precision Floats", value=True)
        st.selectbox("Default Volume Base System Unit", ["µL", "mL", "L"])

# Space element block padding to protect components from getting overlapped by bottom fixed container
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# =====================================================
# SYSTEM PERSISTENT FLOATING BOTTOM NAV BAR
# =====================================================
st.markdown('<div class="bottom-nav-container">', unsafe_allow_html=True)
nav_cols = st.columns(4)

with nav_cols[0]:
    if st.button("🏠\nHome", key="nav_h", use_container_width=True):
        nav_to_tab("Home")
        st.rerun()
with nav_cols[1]:
    if st.button("🔄\nConvert", key="nav_c", use_container_width=True):
        nav_to_tab("Convert")
        st.rerun()
with nav_cols[2]:
    if st.button("⏱️\nHistory", key="nav_hi", use_container_width=True):
        nav_to_tab("History")
        st.rerun()
with nav_cols[3]:
    if st.button("⚙️\nSettings", key="nav_s", use_container_width=True):
        nav_to_tab("Settings")
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
