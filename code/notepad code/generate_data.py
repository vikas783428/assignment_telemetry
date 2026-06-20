import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Create output folder path
output_dir = "../data"
os.makedirs(output_dir, exist_ok=True)

# Generate data
n = 1000
start_time = datetime.now()

data = []

for i in range(n):
    timestamp = start_time + timedelta(seconds=i)

    cpu = random.uniform(10, 95)
    memory = random.uniform(20, 90)
    latency = random.uniform(1, 200)
    packet_loss = random.uniform(0, 5)

    # Inject faults
    if random.random() < 0.05:
        cpu = random.uniform(90, 100)
        latency = random.uniform(200, 500)
        packet_loss = random.uniform(5, 20)

    data.append([timestamp, cpu, memory, latency, packet_loss])

df = pd.DataFrame(data, columns=[
    "timestamp", "cpu_usage", "memory_usage", "latency", "packet_loss"
])

df.to_csv(output_dir + "/telemetry.csv", index=False)

print("Synthetic telemetry data generated successfully!")