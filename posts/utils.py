import math


def estimate_reading_time(text, wpm=225):
    words = text.strip().split()
    estimated_time = math.ceil(len(words) / wpm)
    return estimated_time
