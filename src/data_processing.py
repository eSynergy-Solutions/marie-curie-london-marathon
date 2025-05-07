import pandas as pd
from random import random


def get_data(path):
    df = pd.read_excel(path, index_col=False)

    if "id" not in df.columns:
        df["id"] = [
            "".join(
                [
                    chr(int(random() * 26) + 65)
                    if random() > 0.5
                    else str(int(random() * 10))
                    for _ in range(8)
                ]
            )
            for _ in range(len(df))
        ]
        df.to_excel(path)
    return df


def convert_time_to_minutes(time_str):
    """
    Convert various time formats to minutes.

    Examples:
    - "3:45:30" (3 hours, 45 minutes, 30 seconds) -> 225.5 minutes
    - "1:30" (1 hour, 30 minutes) -> 90 minutes
    - "45:30" (45 minutes, 30 seconds) -> 45.5 minutes
    - "2h 30m" -> 150 minutes
    - "90m" -> 90 minutes

    Args:
        time_str (str): Time string to convert

    Returns:
        float: Time in minutes
    """
    if pd.isna(time_str) or time_str == "":
        return 0

    # Handle formats like "2h 30m" or "90m"
    if "h" in time_str or "m" in time_str:
        hours = 0
        minutes = 0

        # Extract hours if present
        if "h" in time_str:
            h_parts = time_str.split("h")
            hours = float(h_parts[0].strip())
            time_str = h_parts[1]

        # Extract minutes if present
        if "m" in time_str:
            m_parts = time_str.split("m")
            minutes = float(m_parts[0].strip())

        return hours * 60 + minutes

    # Handle formats like "3:45:30" or "1:30" or "45:30"
    parts = time_str.split(":")

    if len(parts) == 3:  # Hours:Minutes:Seconds
        hours, minutes, seconds = map(float, parts)
        return hours * 60 + minutes + seconds / 60
    elif len(parts) == 2:  # Minutes:Seconds or Hours:Minutes
        if float(parts[0]) >= 24:  # Likely Minutes:Seconds
            minutes, seconds = map(float, parts)
            return minutes + seconds / 60
        else:  # Likely Hours:Minutes
            hours, minutes = map(float, parts)
            return hours * 60 + minutes
    else:  # Just minutes or unknown format
        try:
            return float(time_str)
        except Exception:
            return 0
