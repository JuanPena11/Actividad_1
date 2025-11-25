import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="University Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("university_student_data.csv")

df = load_data()

st.title("Dashboard Universitario – Admisión, Retención y Satisfacción")

# --- Filtros laterales ---
years = ["Todos"] + sorted(df["Year"].unique().tolist())
terms = ["Todos"] + sorted(df["Term"].unique().tolist())

selected_year = st.sidebar.selectbox("Selecciona un Año", years)
selected_term = st.sidebar.selectbox("Selecciona un Término", terms)

filtered = df.copy()

if selected_year != "Todos":
    filtered = filtered[filtered["Year"] == selected_year]

if selected_term != "Todos":
    filtered = filtered[filtered["Term"] == selected_term]

# --- KPIs ---
st.subheader("Indicadores Principales")
col1, col2, col3 = st.columns(3)

col1.metric("Filas filtradas", len(filtered))

col2.metric(
    "Retención Promedio",
    f"{filtered['Retention Rate (%)'].mean():.2f}%" if len(filtered)>0 else "N/A"
)

col3.metric(
    "Satisfacción Promedio",
    f"{filtered['Student Satisfaction (%)'].mean():.2f}%" if len(filtered)>0 else "N/A"
)

st.markdown("---")

# --- Gráfico 1: Retención por Año ---
st.subheader("Retención por Año")
fig1, ax1 = plt.subplots(figsize=(7,4))
sns.lineplot(data=filtered, x="Year", y="Retention Rate (%)", marker="o", ax=ax1)
st.pyplot(fig1)

# --- Gráfico 2: Satisfacción por Año ---
st.subheader("Satisfacción por Año")
fig2, ax2 = plt.subplots(figsize=(7,4))
sns.barplot(data=filtered, x="Year", y="Student Satisfaction (%)", ax=ax2)
st.pyplot(fig2)

# --- Gráfico 3: Spring vs Fall ---
st.subheader("Comparación Spring vs Fall")
fig3, ax3 = plt.subplots(figsize=(6,4))
sns.barplot(data=filtered, x="Term", y="Student Satisfaction (%)", ax=ax3)
st.pyplot(fig3)

st.markdown("---")
st.info("Dashboard generado para la Actividad 1 – Data Visualization and Dashboard Deployment")
