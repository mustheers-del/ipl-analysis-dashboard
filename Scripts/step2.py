import json
import os
import pandas as pd

folder_path = "ipl_json"

match_data = []

for file in os.listdir(folder_path):
    if file.endswith(".json"):
        file_path = os.path.join(folder_path, file)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        info = data["info"]

        match_data.append({
            "match_id": file.replace(".json", ""),
            "team1": info["teams"][0],
            "team2": info["teams"][1],
            "city": info.get("city"),
            "venue": info.get("venue"),
            "date": info["dates"][0],
            "season": info.get("season"),
            "toss_winner": info["toss"]["winner"],
            "toss_decision": info["toss"]["decision"],
            "winner": info["outcome"].get("winner")
        })

df = pd.DataFrame(match_data)

print(df.head())

df.to_csv("matches_cleaned.csv", index=False)
