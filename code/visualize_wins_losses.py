import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def visualize_wins_losses():
    """
    Visualizes the wins and losses of a team with team scores and opponent scores.
    Displays a grouped bar chart with clear differentiation between wins and losses.
    """
    # Load data
    data_path = "../data/team_performance.csv"
    data = pd.read_csv(data_path)

    # Extract relevant columns
    weeks = data["Week"]
    team_scores = data["Score"]
    opponent_scores = data["OpponentScore"]
    results = data["Result"]

    # Define bar positions
    x = np.arange(len(weeks))
    width = 0.4

    # Create the bar chart
    plt.figure(figsize=(14, 8))
    plt.bar(x - width/2, team_scores, width, label="Team Score", color="blue", alpha=0.7)
    plt.bar(x + width/2, opponent_scores, width, label="Opponent Score", color="red", alpha=0.7)

    # Annotate results (Win/Loss) above bars
    for i, result in enumerate(results):
        color = "green" if result == "Win" else "black"
        plt.text(x[i], max(team_scores[i], opponent_scores[i]) + 1, result, ha="center", color=color, fontsize=10)

    # Add labels, title, and legend
    team = data["Team"].iloc[0] if "Team" in data.columns else "Team"
    plt.title(f"{team} Wins and Losses with Scores", fontsize=16)
    plt.xlabel("Week", fontsize=12)
    plt.ylabel("Scores", fontsize=12)
    plt.xticks(ticks=x, labels=weeks, rotation=45)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Save and show the plot
    chart_path = f"../charts/{team}_wins_losses_scores.png"
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.show()

    print(f"Wins and Losses chart saved to {chart_path}")

if __name__ == "__main__":
    visualize_wins_losses()
