import pandas as pd

# Load data
df = pd.read_csv("data/telemetry.csv")

# Rules for anomaly detection
df["cpu_anomaly"] = df["cpu_usage"] > 90
df["latency_anomaly"] = df["latency"] > 200
df["packet_loss_anomaly"] = df["packet_loss"] > 5

# Combined fault flag
df["fault"] = (
    df["cpu_anomaly"] |
    df["latency_anomaly"] |
    df["packet_loss_anomaly"]
)

# Show results
print("\n🚨 Faulty Records Detected:")
print(df[df["fault"]].head(20))

# Save results
df.to_csv("data/telemetry_with_faults.csv", index=False)

print("\n✅ Fault detection complete. Output saved.")