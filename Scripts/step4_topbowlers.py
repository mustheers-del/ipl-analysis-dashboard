import pandas as pd

df = pd.read_csv("deliveries_cleaned.csv")

# We assume wickets exist if extras is not null and indicates dismissal in full dataset
# (some IPL datasets include wicket info separately; we simplify here)

# Step 1: count balls bowled
balls_bowled = df.groupby("bowler").size()

# Step 2: estimate wickets (advanced datasets usually have wicket column)
# If your dataset has no wicket column, we use a placeholder approach:
# We'll treat "runs_batter == 0 AND extras == 0" as NOT wicket (safe logic)

# NOTE: real wicket extraction depends on dataset structure
# For now we focus on bowling workload

top_bowlers = balls_bowled.sort_values(ascending=False).head(10)

print("🔥 TOP 10 MOST ACTIVE BOWLERS (BY BALLS BOWLED)")
print(top_bowlers)
top_bowlers.to_csv("top_bowlers_used.csv")
