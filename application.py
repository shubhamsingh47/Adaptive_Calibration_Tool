import streamlit as st
from src.pipeline.ui import render_ui


def main():
    st.set_page_config(page_title="Adaptive Calibration", layout="wide")
    render_ui()


if __name__ == "__main__":
    main()
