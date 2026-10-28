import streamlit as st
from backend import load_data, get_summary, plot_sales_over_time

def main():
    st.title("Supermarket Sales Dashboard")

    data = load_data()

    st.sidebar.header("Controls")
    min_rating = st.sidebar.slider(
        "Minimum Rating",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )

    filtered_data = data[data["Rating"] >= min_rating]

    st.write("### Summary Statistics")
    updated_summary = get_summary(filtered_data)
    st.table(updated_summary)

    st.write("### Raw Data")
    st.dataframe(filtered_data)

    st.write("### Sales Over Time")
    fig = plot_sales_over_time(filtered_data)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
