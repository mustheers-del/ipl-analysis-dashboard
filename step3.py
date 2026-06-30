import json
import os
import pandas as pd

folder_path = "ipl_json"

ball_data = []

for file in os.listdir(folder_path):
    if file.endswith(".json"):
        file_path = os.path.join(folder_path, file)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        match_id = file.replace(".json", "")

        innings = data["innings"]

        for inning in innings:
            team = inning["team"]

            for over in inning["overs"]:
                over_num = over["over"]

                for delivery in over["deliveries"]:
                    ball_data.append({
                        "match_id": match_id,
                        "batting_team": team,
                        "over": over_num,
                        "batter": delivery["batter"],
                        "bowler": delivery["bowler"],
                        "runs_batter": delivery["runs"]["batter"],
                        "runs_total": delivery["runs"]["total"],
                        "extras": delivery["runs"]["extras"],
                    })

df = pd.DataFrame(ball_data)

print(df.head())

df.to_csv("deliveries_cleaned.csv", index=False)