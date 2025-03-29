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

This will launch a local server where users can upload call data and visualize metrics.
