import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------------
# DATA LOAD
# -----------------------------------------------------------

@st.cache_data
def load_data():
    data = pd.read_csv("turkey_earthquakes(1915-2024_feb).csv")

    # Convert date column
    data["Olus tarihi"] = pd.to_datetime(data["Olus tarihi"], errors="coerce")
    return data

df = load_data()

st.title("Member 1 - Earthquake Analysis Focused on Time & Magnitude")

# =====================================================================
# GRAPH 1 — TIME SERIES (Earthquake Count by Year)
# =====================================================================

st.subheader("1. Earthquake Counts by Year (Time Series + Slider)")

# Year range slider
min_year = int(df["Olus tarihi"].dt.year.min())
max_year = int(df["Olus tarihi"].dt.year.max())

selected_years = st.slider(
    "Select the Year Range",
    min_year, max_year,
    (1970, 2024)
)

# Filter data
df_filtered = df[
    (df["Olus tarihi"].dt.year >= selected_years[0]) &
    (df["Olus tarihi"].dt.year <= selected_years[1])
]

year_counts = df_filtered["Olus tarihi"].dt.year.value_counts().sort_index()

fig1 = px.line(
    x=year_counts.index,
    y=year_counts.values,
    markers=True,
    labels={"x": "Year", "y": "Earthquake Count"},
    title="Earthquake Frequency Over the Years"
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
**Question Addressed:**  
📌 *“How has the number of earthquakes in Turkey changed between 1915–2024?”*

This chart helps to identify long-term trends in earthquake frequency.
""")

# =====================================================================
# GRAPH 2 — VIOLIN PLOT (Distribution of Magnitude Types)
# =====================================================================

st.subheader("2. Distribution by Magnitude Type (Violin Plot)")

mag_choice = st.selectbox(
    "Select Magnitude Type",
    ["MD", "ML", "Mw"]
)

df_mag = df[df[mag_choice].notna()]

fig2 = px.violin(
    df_mag,
    y=mag_choice,
    box=True,
    points="all",
    color_discrete_sequence=["#FF5733"],
    title=f"Distribution of {mag_choice} Magnitude"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown(f"""
**Question Addressed:**  
📌 *“Within which range does the {mag_choice} magnitude concentrate in Turkey?”*

This visualization compares the distribution of different magnitude types (MD, ML, Mw).
""")

# =====================================================================
# GRAPH 3 — HISTOGRAM (Depth Distribution by Magnitude Range)
# =====================================================================

st.subheader("3. Depth Distribution by Magnitude (Histogram + Slider)")

# 🔧 FIXED: xM -> Mw
min_mag = float(df["Mw"].min())
max_mag = float(df["Mw"].max())

selected_mag = st.slider(
    "Select Magnitude Range",
    min_mag, max_mag,
    (4.0, 6.0)
)

df_depth = df[
    (df["Mw"] >= selected_mag[0]) &
    (df["Mw"] <= selected_mag[1]) &
    (df["Derinlik"].notna())
]

fig3 = px.histogram(
    df_depth,
    x="Derinlik",
    nbins=50,
    color_discrete_sequence=["#2E86C1"],
    title=f"Depth Distribution for Mw Magnitude Range {selected_mag[0]}–{selected_mag[1]}",
    labels={"Derinlik": "Depth (km)", "count": "Number of Earthquakes"}
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
**Question Addressed:**  
📌 *“Are earthquakes of different magnitudes more shallow or deeper?”*

This histogram shows how depth varies depending on magnitude range.
""")

st.success("Member 1's analysis section has been completed successfully.")
