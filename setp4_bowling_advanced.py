import pandas as pd

df = pd.read_csv("deliveries_cleaned.csv")

# ---------------------------
# STEP 1: BALLS BOWLED
# ---------------------------
balls = df.groupby("bowler").size().reset_index(name="balls_bowled")

# ---------------------------
# STEP 2: RUNS CONCEDED
# ---------------------------
runs = df.groupby("bowler")["runs_total"].sum().reset_index(name="runs_conceded")

# ---------------------------
# STEP 3: MERGE DATA
# ---------------------------
bowling = pd.merge(balls, runs, on="bowler")

# ---------------------------
# STEP 4: ECONOMY RATE
# economy = runs / overs
# overs = balls / 6
# ---------------------------
bowling["overs"] = bowling["balls_bowled"] / 6
bowling["economy_rate"] = bowling["runs_conceded"] / bowling["overs"]

# ---------------------------
# STEP 5: TOP BOWLERS (BY ECONOMY)
# ---------------------------
top_economy = bowling.sort_values("economy_rate").head(10)

print("🔥 TOP 10 BOWLERS (BEST ECONOMY RATE)")
print(top_economy)