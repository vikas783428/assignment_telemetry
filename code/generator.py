import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_data():
    os.makedirs("data", exist_ok=True)

    n = 1000
    start_time = datetime.now()

    rows = []

    for i in range(n):
        timestamp = start_time + timedelta(seconds=i)

        cpu = random.uniform(10, 95)
        memory = random.uniform(20, 90)
        latency = random.uniform(1, 200)
        packet_loss = random.uniform(0, 5)

        # inject faults
        if random.random() < 0.05:
            cpu = random.uniform(90, 100)
            latency = random.uniform(200, 500)
            packet_loss = random.uniform(5, 20)

        rows.append([timestamp, cpu, memory, latency, packet_loss])

    df = pd.DataFrame(rows, columns=[
        "timestamp", "cpu_usage", "memory_usage", "latency", "packet_loss"
    ])

    output_path = os.path.join("data", "telemetry.csv")
    df.to_csv(output_path, index=False)

    print("✅ Generated:", output_path)

if __name__ == "__main__":
    generate_data()