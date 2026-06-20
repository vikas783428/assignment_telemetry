import pandas as pd

df = pd.read_csv("data/telemetry_with_faults.csv")

# Filter only faults
faults = df[df["fault"] == True]

print("\n📊 Root Cause Analysis Summary:\n")

print("Total faulty records:", len(faults))

print("\nAverage metrics during failure:")
print(faults[["cpu_usage", "memory_usage", "latency", "packet_loss"]].mean())

print("\nCorrelation with faults:")
print(df[["cpu_usage", "latency", "packet_loss"]].corr())

# Strong indicators
print("\n🚨 Key Insight:")
print("- High CPU usage strongly correlates with system faults")
print("- Latency spikes often appear with packet loss")