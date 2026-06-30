import pandas as pd

df = pd.read_csv("deliveries_cleaned.csv")

top_batsmen = df.groupby("batter")["runs_batter"].sum().sort_values(ascending=False).head(10)

print("🔥 TOP 10 BATSMEN")
print(top_batsmen)

# SAVE TO FILE (IMPORTANT FOR PORTFOLIO)
top_batsmen.to_csv("top_batsmen.csv")