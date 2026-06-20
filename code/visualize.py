import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
df = pd.read_csv(os.path.join("data", "telemetry.csv"))

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 🔴 Fault Detection Logic
df["fault"] = (
    (df["cpu_usage"] > 90) |
    (df["memory_usage"] > 85) |
    (df["latency"] > 100) |
    (df["packet_loss"] > 2)
)

# Style
sns.set_style("darkgrid")

# 1. CPU Usage (WITH FAULTS)
plt.figure()

plt.plot(df["timestamp"], df["cpu_usage"], label="CPU Usage")

plt.scatter(
    df[df["fault"]]["timestamp"],
    df[df["fault"]]["cpu_usage"],
    color="red",
    label="Fault",
    s=25
)

plt.title("CPU Usage Over Time (Fault Highlighted)")
plt.xlabel("Time")
plt.ylabel("CPU %")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Memory Usage (UPDATED ⭐ WITH FAULTS)
plt.figure()

plt.plot(df["timestamp"], df["memory_usage"], label="Memory Usage")

plt.scatter(
    df[df["fault"]]["timestamp"],
    df[df["fault"]]["memory_usage"],
    color="red",
    label="Fault",
    s=25
)

plt.title("Memory Usage Over Time (Fault Highlighted)")
plt.xlabel("Time")
plt.ylabel("Memory %")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# 3. Latency (with fault highlight)
plt.figure()

plt.plot(df["timestamp"], df["latency"], label="Latency")

plt.scatter(
    df[df["fault"]]["timestamp"],
    df[df["fault"]]["latency"],
    color="red",
    label="Fault",
    s=25
)

plt.title("Network Latency Over Time (Fault Highlighted)")
plt.xlabel("Time")
plt.ylabel("Latency (ms)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# 4. Packet Loss (with fault highlight)
plt.figure()

plt.plot(df["timestamp"], df["packet_loss"], label="Packet Loss")

plt.scatter(
    df[df["fault"]]["timestamp"],
    df[df["fault"]]["packet_loss"],
    color="red",
    label="Fault",
    s=25
)

plt.title("Packet Loss Over Time (Fault Highlighted)")
plt.xlabel("Time")
plt.ylabel("Packet Loss %")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

print("✅ Visualization complete")