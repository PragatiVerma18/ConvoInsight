import json
import matplotlib.pyplot as plt
import os
import pandas as pd
import streamlit as st
import yaml

from analysis import detect_profanity, detect_privacy_violation
from metrics import calculate_metrics
from visualization import (
    plot_pie_chart,
    plot_bar_chart,
    plot_dual_line_chart,
)

st.title("Call Conversation Analysis Tool")

uploaded_file = st.file_uploader("Upload a JSON or YAML file", type=["json", "yaml"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".yaml"):
            conversation_data = yaml.safe_load(uploaded_file)
        elif uploaded_file.name.endswith(".json"):
            conversation_data = json.load(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a JSON or YAML file.")
            st.stop()

        if not isinstance(conversation_data, list) or not all(
            isinstance(item, dict) for item in conversation_data
        ):
            st.error("Invalid file structure. Please upload a valid conversation file.")
            st.stop()

        silence_pct, overtalk_pct = calculate_metrics(conversation_data)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
        st.stop()

    tab1, tab2 = st.tabs(["Analysis Results", "Call Quality Metrics"])

    # Tab 1: Display analysis results
    with tab1:
        analysis_method = st.selectbox("Select Analysis Method", ["Regex", "LLM"])
        entity = st.selectbox(
            "Select Entity to Analyze", ["Profanity Detection", "Privacy Violation"]
        )

        if st.button("Analyze"):
            try:
                with st.spinner("Analyzing..."):
                    call_id = os.path.splitext(os.path.basename(uploaded_file.name))[0]

                    if entity == "Profanity Detection":
                        results = detect_profanity(
                            conversation_data, analysis_method, call_id
                        )
                    else:
                        results = detect_privacy_violation(
                            conversation_data, analysis_method, call_id
                        )

                st.success("Analysis Complete!")

                st.subheader("Analysis Results")

                if results:
                    st.warning("Flagged Utterances:")

                    for i, res in enumerate(results, start=1):
                        st.markdown(f"### Flagged Utterance {i}")
                        st.markdown(
                            f"""
                            <style>
                                table {{
                                    width: 100%;
                                    border-collapse: collapse;
                                }}
                                th, td {{
                                    border: 1px solid #ddd;
                                    padding: 8px;
                                    text-align: left;
                                }}
                                th {{
                                    background-color: #f2f2f2;
                                    font-weight: bold;
                                }}
                                tr:nth-child(even) {{
                                    background-color: #f9f9f9;
                                }}
                                tr:hover {{
                                    background-color: #f1f1f1;
                                }}
                            </style>
                            <table>
                                <tr><th>Call ID</th><td>{res['call_id']}</td></tr>
                                <tr><th>Speaker</th><td>{res['speaker']}</td></tr>
                                <tr><th>Timestamp</th><td>{res['timestamp']}</td></tr>
                                <tr><th>Flagged Utterance</th><td>{res['flagged_utterance']}</td></tr>
                                <tr><th>Reason</th><td>{res['reason']}</td></tr>
                            </table>
                            """,
                            unsafe_allow_html=True,
                        )
                else:
                    st.success("No issues detected!")

            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")

    # Tab 2: Display visualization (metrics remain constant)
    with tab2:
        st.subheader("Call Quality Metrics")

        try:
            chart_type = st.selectbox(
                "Select Chart Type", ["Pie Chart", "Bar Chart", "Dual Line Chart"]
            )

            if chart_type == "Pie Chart":
                st.pyplot(plot_pie_chart(silence_pct, overtalk_pct))

            elif chart_type == "Bar Chart":
                st.pyplot(plot_bar_chart(silence_pct, overtalk_pct))

            elif chart_type == "Dual Line Chart":
                chart = plot_dual_line_chart(conversation_data)
                if chart:
                    st.pyplot(chart)
                else:
                    st.warning("No data available for the Dual Line Chart.")

        except Exception as e:
            st.error(f"An error occurred while generating the chart: {e}")
