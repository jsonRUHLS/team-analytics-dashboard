import pandas as pd
import matplotlib.pyplot as plt

def win_loss_ratio():
    """Creates a bar chart for the win/loss ratio."""
    data_path = "../data/team_performance.csv"
    data = pd.read_csv(data_path)

    team = data.get("Team", ["Team"])[0]  # Fallback to "Team" if data is missing
    win_loss_counts = data["Result"].value_counts()

    plt.figure(figsize=(8, 6))
    plt.bar(win_loss_counts.index, win_loss_counts.values, color=["green", "red"])
    plt.title(f"Win/Loss Ratio for {team}", fontsize=14)
    plt.ylabel("Number of Games", fontsize=12)
    plt.xlabel("Result", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    chart_path = f"../charts/{team}_win_loss_ratio.png"
    plt.savefig(chart_path)
    plt.show()
    print(f"Win/Loss ratio chart saved to {chart_path}")

if __name__ == "__main__":
    win_loss_ratio()
