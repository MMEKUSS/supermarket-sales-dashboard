import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    data = pd.read_csv("supermarket_sales.csv")
    data["Date"] = pd.to_datetime(data["Date"])
    return data

def get_summary(data):
    summary = data[["Unit price", "Quantity", "Total", "Rating"]].describe()
    return summary

def plot_sales_over_time(data):
    sales_by_date = data.groupby("Date")["Total"].sum()

    fig, ax = plt.subplots()
    sales_by_date.plot(ax=ax)

    ax.set_title("Sales Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Sales")

    plt.xticks(rotation=45)
    fig.tight_layout()

    return fig
