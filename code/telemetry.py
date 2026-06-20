import numpy as np
import pandas as pd

from utils import (
    daily_pattern,
    weekly_pattern,
    random_noise,
)
def generate_telemetry(timestamps):
    """
    Generate synthetic network telemetry data.
    """

    rows = []

    for ts in timestamps:

        hour = ts.hour
        day = ts.weekday()

        load = daily_pattern(hour) * weekly_pattern(day)

        users = 500 * load + random_noise(20)

        traffic = 100 * load + random_noise(5)

        signal = 95 - load * 2 + random_noise(1)

        latency = 20 + load * 6 + random_noise(1)

        cpu = 35 + load * 15 + random_noise(3)

        memory = 45 + load * 10 + random_noise(2)

        temperature = 40 + load * 4 + random_noise(1)

        packet_loss = max(0, random_noise(0.3))

        throughput = traffic * 9 + random_noise(10)

        retransmissions = max(0, random_noise(0.5))

        error_rate = max(0, random_noise(0.2))

        availability = 99.99 - random_noise(0.01)

        rows.append([
            ts,
            users,
            traffic,
            signal,
            latency,
            cpu,
            memory,
            temperature,
            packet_loss,
            throughput,
            retransmissions,
            error_rate,
            availability
        ])
        columns = [
        "timestamp",
        "users",
        "traffic",
        "signal_quality",
        "latency",
        "cpu_usage",
        "memory_usage",
        "temperature",
        "packet_loss",
        "throughput",
        "retransmissions",
        "error_rate",
        "availability"
    ]

    return pd.DataFrame(rows, columns=columns)