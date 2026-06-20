import numpy as np
import pandas as pd


def inject_faults(df):

    df = df.copy()

    df["fault"] = "Normal"

    # Randomly select 5% of rows for High Latency faults
    latency_faults = df.sample(frac=0.05, random_state=42).index

    # Increase latency values
    df.loc[latency_faults, "latency"] *= 3

    # Mark these rows as High Latency
    df.loc[latency_faults, "fault"] = "High Latency"

    # Randomly select another 5% of rows
    traffic_faults = df[df["fault"] == "Normal"].sample(
        frac=0.05,
        random_state=24
    ).index

    # Increase traffic
    df.loc[traffic_faults, "traffic"] *= 2

    # Increase users
    df.loc[traffic_faults, "users"] *= 2

    # Mark fault
    df.loc[traffic_faults, "fault"] = "Traffic Spike"

    # Randomly select another 5% of normal rows
    cpu_faults = df[df["fault"] == "Normal"].sample(
        frac=0.05,
        random_state=100
    ).index

    # Increase CPU usage
    df.loc[cpu_faults, "cpu_usage"] = (
        95 + np.random.rand(len(cpu_faults)) * 5
    )

    # Increase memory usage
    df.loc[cpu_faults, "memory_usage"] = (
        90 + np.random.rand(len(cpu_faults)) * 10
    )

    # Mark fault
    df.loc[cpu_faults, "fault"] = "CPU Overload"
          # Randomly select another 5% of normal rows
    temperature_faults = df[df["fault"] == "Normal"].sample(
        frac=0.05,
        random_state=55
    ).index

    # Increase temperature
    df.loc[temperature_faults, "temperature"] = (
        75 + np.random.rand(len(temperature_faults)) * 10
    )

    # Mark fault
    df.loc[temperature_faults, "fault"] = "High Temperature"
    return df
