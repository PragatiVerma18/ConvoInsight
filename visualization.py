import matplotlib.pyplot as plt
import streamlit as st


def plot_pie_chart(silence_pct, overtalk_pct):
    """Plot a pie chart for call quality metrics."""
    labels = ["Silence", "Overtalk", "Normal Conversation"]
    values = [silence_pct, overtalk_pct, 100 - silence_pct - overtalk_pct]
    colors = ["blue", "orange", "gray"]

    fig, ax = plt.subplots()
    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
    )
    ax.set_title("Call Quality Metrics")
    return fig


def plot_bar_chart(silence_pct, overtalk_pct):
    """Plot a bar chart (Gantt Chart style) for call quality metrics."""
    metrics = ["Silence", "Overtalk", "Normal Conversation"]
    normal_pct = 100 - silence_pct - overtalk_pct
    values = [silence_pct, overtalk_pct, normal_pct]

    fig, ax = plt.subplots()
    ax.barh(metrics, values, color=["blue", "orange", "green"])
    ax.set_xlabel("Percentage")
    ax.set_title("Call Quality Metrics")
    ax.set_xlim(0, 100)
    return fig


def plot_dual_line_chart(conversation_data):
    """Plot a dual line chart for speaker activity."""
    if not conversation_data or not isinstance(conversation_data, list):
        st.error("Invalid conversation data for Dual Line Chart.")
        return None

    max_time = int(max(utt["etime"] for utt in conversation_data))
    timeline = list(range(max_time + 1))

    speaker_1_activity = [0] * len(timeline)
    speaker_2_activity = [0] * len(timeline)

    for utt in conversation_data:
        stime = int(utt["stime"])
        etime = int(utt["etime"])
        if utt["speaker"] == "Agent":
            for t in range(stime, etime + 1):
                speaker_1_activity[t] = 1
        elif utt["speaker"] == "Customer":
            for t in range(stime, etime + 1):
                speaker_2_activity[t] = 1

    fig, ax = plt.subplots()
    ax.plot(
        timeline,
        speaker_1_activity,
        label="Agent",
        color="blue",
        linewidth=2,
    )
    ax.plot(
        timeline,
        speaker_2_activity,
        label="Customer",
        color="orange",
        linewidth=2,
    )

    overtalk = [
        1 if s1 == 1 and s2 == 1 else 0
        for s1, s2 in zip(speaker_1_activity, speaker_2_activity)
    ]
    ax.fill_between(
        timeline,
        overtalk,
        color="red",
        alpha=0.3,
        label="Overtalk",
    )

    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Activity (1 = Speaking, 0 = Silent)")
    ax.set_title("Dual Line Chart: Speaker Activity")
    ax.legend()

    return fig
