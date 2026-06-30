import json
import os
import pandas as pd

folder_path = "ipl_json"

batsman_runs = {}
bowler_runs = {}
bowler_balls = {}
bowler_wickets = {}

for file in os.listdir(folder_path):
    if file.endswith(".json"):
        path = os.path.join(folder_path, file)

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        innings = data["innings"]

        for inning in innings:
            for over in inning["overs"]:
                for ball in over["deliveries"]:

                    batter = ball["batter"]
                    bowler = ball["bowler"]

                    runs = ball["runs"]["batter"]

                    # ---------------- BATSMAN ----------------
                    batsman_runs[batter] = batsman_runs.get(batter, 0) + runs

                    # ---------------- BOWLER ----------------
                    bowler_runs[bowler] = bowler_runs.get(bowler, 0) + ball["runs"]["total"]
                    bowler_balls[bowler] = bowler_balls.get(bowler, 0) + 1

                    # ---------------- WICKETS ----------------
                    if "wickets" in ball:
                        bowler_wickets[bowler] = bowler_wickets.get(bowler, 0) + 1

# ---------------- BATSMEN TABLE ----------------
bat_df = pd.DataFrame(list(batsman_runs.items()), columns=["batsman", "runs"])
bat_df = bat_df.sort_values(by="runs", ascending=False)

# ---------------- BOWLER TABLE ----------------
bowl_df = pd.DataFrame({
    "bowler": list(bowler_runs.keys()),
    "runs": list(bowler_runs.values()),
    "balls": [bowler_balls.get(b, 0) for b in bowler_runs.keys()],
    "wickets": [bowler_wickets.get(b, 0) for b in bowler_runs.keys()]
})

bowl_df["overs"] = bowl_df["balls"] / 6
bowl_df["economy"] = bowl_df["runs"] / bowl_df["overs"]

bowl_df = bowl_df.sort_values(by="wickets", ascending=False)

# ---------------- OUTPUT ----------------
print("\n🔥 TOP 10 BATSMEN")
print(bat_df.head(10))

print("\n🎯 TOP 10 BOWLERS")
print(bowl_df.head(10))

# ---------------- SAVE FILES ----------------
bat_df.to_csv("final_batsmen_stats.csv", index=False)
bowl_df.to_csv("final_bowlers_stats.csv", index=False)