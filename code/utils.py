import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def set_seed(seed):
    """
    Set random seed for reproducibility.
    """
    np.random.seed(seed)


def generate_timestamps(days, interval_minutes):
    """
    Generate timestamps for the simulation.

    Example:
    21 days
    15-minute interval
    """

    start = datetime(2025, 1, 1)

    total_points = days * 24 * (60 // interval_minutes)

    timestamps = []

    for i in range(total_points):
        timestamps.append(
            start + timedelta(minutes=i * interval_minutes)
        )

    return timestamps


def daily_pattern(hour):
    """
    Daily traffic pattern.

    Low traffic:
        Midnight - Early Morning

    High traffic:
        Morning
        Evening
    """

    return 1 + 0.8 * np.sin((hour - 8) * 2 * np.pi / 24)


def weekly_pattern(day):
    """
    Weekdays are busier than weekends.
    """

    if day % 7 < 5:
        return 1.2

    return 0.8


def random_noise(std):
    """
    Generate Gaussian noise.
    """

    return np.random.normal(0, std)