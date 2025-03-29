# Call Analysis and Profanity Detection

> This project analyzes call data to measure overtalk and silence metrics while also detecting profanity and sensitive information using regex-based and LLM-based approaches.

## Features

- **Call Analysis**: Computes silence and overtalk percentages.
- **Visualization**: Generates charts for call metrics.
- **Profanity Detection**: Uses regex and ChatGPT API for comparison.
- **Sensitive Data Detection**: Identifies sensitive information like account numbers and SSNs.
- **Streamlit App**: Provides an interactive UI for users to analyze call data.

## Setup Instructions

### Prerequisites

Ensure that the following dependencies are installed:

- Python 3.8+
- Virtual environment

### Installation

1. Clone the repository:

```shell
https://github.com/PragatiVerma18/call-analysis.git
cd call-analysis
```

2. Create and activate a virtual environment:

```shell
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```shell
pip install -r requirements.txt
```

4. Set up environment variables in `.env`:

```shell
OPENAI_API_KEY="your-api-key"
```

5. Run the Streamlit App:

```shell
streamlit run app.py
```

> This will launch a local server where users can upload call data and visualize metrics.

## Streamlit App Overview

Once the app is running, you can interact with the following features:

### 1. File Upload:

- Upload a `.json` or `.yaml` file containing call conversation data. Find example file here - [example-conversation.json](./example-conversation.json).
- The app will parse the file and extract relevant information such as speaker activity, timestamps, and text.

### 2. Tabs for Analysis and Visualization:

- The app is divided into two main tabs:

- **Analysis Results**:

  - Select an analysis method (`Regex` or `LLM`) to detect profanity or privacy violations.
  - View flagged utterances in the conversation.
  - Get feedback on whether any issues were detected.

- **Call Quality Metrics**:
  - Choose from multiple visualization options to analyze call quality:
  - **Pie Chart**: Displays the proportions of silence, overtalk, and normal conversation.
  - **Bar Chart**: A horizontal bar chart (Gantt Chart style) for comparing silence, overtalk, and normal conversation percentages.
  - **Dual Line Chart**: Plots the speaking activity of both the agent and the customer over time, highlighting overtalk segments.

### 3. Analysis Features:

- **Profanity Detection**:
  - Detects offensive language in the conversation using either regex-based or LLM-based methods.
- **Privacy Violation Detection**:
  - Identifies sensitive information such as account numbers, SSNs, and other personal identifiers.

### 4. Call Quality Metrics:

- **Silence Percentage**:

  - Measures the proportion of the call where neither party is speaking.

- **Overtalk Percentage**:

  - Measures the proportion of the call where both parties are speaking simultaneously.

- **Normal Conversation**:
  - Represents the remaining portion of the call where only one party is speaking at a time.

### 5. Interactive Visualizations:

- The app provides intuitive visualizations to help users understand call dynamics:
  - **Pie Chart**: For an overall breakdown of silence, overtalk, and normal conversation.
  - **Bar Chart**: For comparing metrics side by side.
  - **Dual Line Chart**: For analyzing speaker activity over time.

### 6. Insights:

- Based on the analysis, the app provides insights into call quality and compliance.
