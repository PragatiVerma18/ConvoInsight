import matplotlib.pyplot as plt


def plot_metrics(silence_percentage, overtalk_percentage):
    """Visualize silence and overtalk metrics."""
    labels = ["Silence", "Overtalk", "Speech"]
    values = [
        silence_percentage,
        overtalk_percentage,
        100 - (silence_percentage + overtalk_percentage),
    ]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(values, labels=labels, autopct="%1.1f%%", colors=["blue", "red", "green"])
    ax.set_title("Silence & Overtalk Distribution")
    return fig
