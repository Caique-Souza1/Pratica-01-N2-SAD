import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análise de Vendas E-Commerce",
    page_icon="📊",
    layout="wide"
)

st.title("📊 E-Commerce Sales & Profit Analysis")
st.markdown("### Sistemas de Apoio à Decisão")


@st.cache_data
def carregar_dados():
    df = pd.read_csv("ecommerce_sales_data.csv")

    df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.date

    return df


df = carregar_dados()

# Filtros
st.sidebar.header("Filtros")

categorias = st.sidebar.multiselect(
    "Categoria",
    df["Category"].unique(),
    df["Category"].unique()
)

regioes = st.sidebar.multiselect(
    "Região",
    df["Region"].unique(),
    df["Region"].unique()
)

df = df[
    (df["Category"].isin(categorias)) &
    (df["Region"].isin(regioes))
]

# KPIs
st.header("Resumo Geral")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Vendas", f"{df['Sales'].sum():,.2f}")
col2.metric("Lucro Total", f"{df['Profit'].sum():,.2f}")
col3.metric("Quantidade Vendida", int(df["Quantity"].sum()))
col4.metric("Registros", len(df))

# Base
st.header("Base de Dados")
st.dataframe(df, width="stretch")

# Estatísticas
st.header("Estatísticas Descritivas")
st.dataframe(df.describe(), width="stretch")

# Qualidade
st.header("Qualidade dos Dados")

c1, c2 = st.columns(2)

with c1:
    st.subheader("Valores Ausentes")
    st.dataframe(df.isnull().sum(), width="stretch")

with c2:
    st.subheader("Duplicados")
    st.write(df.duplicated().sum())

# Categorias
st.header("Categorias")

fig = px.bar(
    df["Category"].value_counts().reset_index(),
    x="Category",
    y="count",
)

st.plotly_chart(fig, use_container_width=True)

# Vendas
st.header("Distribuição das Vendas")

fig = px.histogram(df, x="Sales", nbins=30)
st.plotly_chart(fig, use_container_width=True)

# Lucro (corrigido)
st.header("Distribuição do Lucro")

fig = px.histogram(df, x="Profit", nbins=30)
st.plotly_chart(fig, use_container_width=True)

# Lucro por categoria
st.header("Lucro por Categoria")

lucro_categoria = (
    df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

fig = px.bar(
    lucro_categoria,
    x="Category",
    y="Profit",
    text_auto=".2s"
)

st.plotly_chart(fig, use_container_width=True)

# Vendas por região
st.header("Vendas por Região")

vendas_regiao = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    vendas_regiao,
    x="Region",
    y="Sales",
    text_auto=".2s"
)

st.plotly_chart(fig, use_container_width=True)

# Evolução 
st.header("Evolução das Vendas (mensal)")

vendas_data = (
    df.groupby(pd.to_datetime(df["Order Date"]).astype(str))["Sales"]
    .sum()
    .reset_index()
)

fig = px.line(
    vendas_data,
    x="Order Date",
    y="Sales",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# Scatter
st.header("Vendas vs Lucro")

fig = px.scatter(
    df,
    x="Sales",
    y="Profit",
    color="Category",
    hover_data=["Product Name"]
)

st.plotly_chart(fig, use_container_width=True)

# Resumos
st.header("Resumo por Categoria")

resumo_categoria = df.groupby("Category").agg(
    Quantidade=("Quantity", "sum"),
    Vendas=("Sales", "sum"),
    Lucro=("Profit", "sum")
)

st.dataframe(resumo_categoria, width="stretch")

st.header("Resumo por Região")

resumo_regiao = df.groupby("Region").agg(
    Quantidade=("Quantity", "sum"),
    Vendas=("Sales", "sum"),
    Lucro=("Profit", "sum")
)

st.dataframe(resumo_regiao, width="stretch")