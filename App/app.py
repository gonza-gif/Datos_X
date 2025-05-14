import streamlit as st
import pandas as pd
import numpy as np

# Datos
data = [
    {
    "vendedor": "MARIANO",
    "suma_compra_usd": 288264.26,
    "suma_venta_usd": 399461.19,
    "total_usd": 687725.45
  },
  {
    "vendedor": "GUSTAVO",
    "suma_compra_usd": 361279.64,
    "suma_venta_usd": 309284.34,
    "total_usd": 670563.98
  },
  {
    "vendedor": "EZEQUIEL",
    "suma_compra_usd": 198112.15,
    "suma_venta_usd": 98131.63,
    "total_usd": 296243.78
  },
  {
    "vendedor": "CHANO",
    "suma_compra_usd": 32812,
    "suma_venta_usd": 61206.76,
    "total_usd": 94018.76
  },
  {
    "vendedor": "JONY",
    "suma_compra_usd": 36401.1,
    "suma_venta_usd": 48054.16,
    "total_usd": 84455.26
  },
  {
    "vendedor": "POCHO",
    "suma_compra_usd": 25016.8,
    "suma_venta_usd": 14717.16,
    "total_usd": 39733.96
  },
  {
    "vendedor": "BOMBA",
    "suma_compra_usd": 0,
    "suma_venta_usd": 37900,
    "total_usd": 37900
  },
  {
    "vendedor": "VIRGINIA",
    "suma_compra_usd": 26200,
    "suma_venta_usd": 4500,
    "total_usd": 30700
  },
  {
    "vendedor": "GULA",
    "suma_compra_usd": 15004,
    "suma_venta_usd": 2800,
    "total_usd": 17804
  },
  {
    "vendedor": "GINO",
    "suma_compra_usd": 0,
    "suma_venta_usd": 7660,
    "total_usd": 7660
  },
  {
    "vendedor": "GABI RUIZ",
    "suma_compra_usd": 400,
    "suma_venta_usd": 4011.5,
    "total_usd": 4411.5
  },
  {
    "vendedor": "MATIAS",
    "suma_compra_usd": 2403.54,
    "suma_venta_usd": 0,
    "total_usd": 2403.54
  },
  {
    "vendedor": "LUCIA",
    "suma_compra_usd": 162,
    "suma_venta_usd": 400,
    "total_usd": 562
  }
]

df = pd.DataFrame(data)

# Título
st.title("Compra y Venta de Vendedores")

# Muestra el dataframe de forma bonita
st.dataframe(df)

# O incluso un gráfico si deseas
st.bar_chart(df.set_index('vendedor')['total_usd'])

