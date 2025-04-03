def calculate_metrics(conversation):
    """Compute silence and overtalk durations."""
    utterances = sorted(conversation, key=lambda x: x["stime"])
    total_duration = utterances[-1]["etime"] - utterances[0]["stime"]

    silence_duration = 0
    overtalk_duration = 0
    prev_etime = utterances[0]["etime"]

    for i in range(1, len(utterances)):
        stime, etime, speaker = (
            utterances[i]["stime"],
            utterances[i]["etime"],
            utterances[i]["speaker"],
        )

        # Silence Calculation
        if stime > prev_etime:
            silence_duration += stime - prev_etime

        # Overtalk Calculation
        for j in range(i):
            prev_etime, prev_speaker = (
                utterances[j]["etime"],
                utterances[j]["speaker"],
            )
            if prev_speaker != speaker and stime < prev_etime:
                overtalk_duration += min(etime, prev_etime) - stime

        prev_etime = max(prev_etime, etime)

    silence_percentage = (silence_duration / total_duration) * 100
    overtalk_percentage = (overtalk_duration / total_duration) * 100

    return silence_percentage, overtalk_percentage
