import re
import openai
import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")


PROFANITY_WORDS = {"damn", "hell", "shit", "fuck"}


SENSITIVE_INFO_PATTERNS = [r"\b\d{10,16}\b", r"\b(balance|account|SSN)\b"]


def detect_profanity(conversation, method):
    """Detect profanity in calls using regex or LLM."""
    flagged_calls = []

    if method == "Regex":
        for utterance in conversation:
            words = set(utterance["text"].lower().split())
            if words & PROFANITY_WORDS:
                flagged_calls.append(utterance["text"])

    elif method == "LLM":
        flagged_calls = chatgpt_analyze(
            conversation, "Identify utterances where the speaker uses profanity."
        )

    return flagged_calls


def detect_privacy_violation(conversation, method):
    """Detect privacy violations using regex or LLM."""
    flagged_calls = []
    verified = False

    if method == "Regex":
        for utterance in conversation:
            if (
                "date of birth" in utterance["text"].lower()
                or "address" in utterance["text"].lower()
            ):
                verified = True
            if (
                any(
                    re.search(pattern, utterance["text"], re.IGNORECASE)
                    for pattern in SENSITIVE_INFO_PATTERNS
                )
                and not verified
            ):
                flagged_calls.append(utterance["text"])

    elif method == "LLM":
        flagged_calls = chatgpt_analyze(
            conversation,
            "Identify utterances where the agent shares sensitive account information without verifying identity.",
        )

    return flagged_calls


def chatgpt_analyze(conversation, instruction):
    """Send conversation data to ChatGPT for analysis."""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    conversation_text = "\n".join(
        f"{utt['speaker']}: {utt['text']}" for utt in conversation
    )

    prompt = f"""
    You are analyzing a debt collection call transcript. Your task is:
    {instruction}
    Transcript:
    {conversation_text}
    Provide a list of flagged utterances.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI compliance expert."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    flagged_results = response.choices[0].message.content.strip()

    return flagged_results.split("\n") if flagged_results else []
