import pandas as pd
import matplotlib.pyplot as plt

def visualize_team_performance():
    """
    Visualizes the games and touchdowns/goals for the season of the specified team.
    If the sport is NFL, it uses touchdowns; otherwise, it uses goals.
    """
    # Load data
    data_path = "../data/team_performance.csv"
    data = pd.read_csv(data_path)

    # Determine if sport is NFL
    is_nfl = "Touchdowns" in data.columns
    metric = "Touchdowns" if is_nfl else "Goals"
    team = data.get("Team", ["Team"])[0]  # Fallback to "Team" if the column doesn't exist

    # Create the bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(data["Week"], data[metric], color="skyblue", alpha=0.8)
    plt.title(f"{team} Performance: {metric} Per Game", fontsize=16)
    plt.xlabel("Game", fontsize=12)
    plt.ylabel(metric, fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Save and show the plot
    chart_path = f"../charts/{team}_performance_{metric.lower()}.png"
    plt.savefig(chart_path)
    plt.show()

    print(f"Performance chart saved to {chart_path}")

if __name__ == "__main__":
    visualize_team_performance()
