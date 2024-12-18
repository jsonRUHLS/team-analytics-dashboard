import random
import pandas as pd
import requests

def fetch_nfl_box_scores(api_key, team, season):
    """
    Fetches all final box scores for a given team across all weeks of a season.
    
    Args:
        api_key (str): Your API key for api.sportsdata.io.
        team (str): NFL team abbreviation (e.g., DAL for Dallas Cowboys).
        season (int): The season year (e.g., 2023).
        
    Returns:
        pd.DataFrame: DataFrame containing game data for the specified team and season.
    """
    all_games = []

    for week in range(1, 18):  # Regular NFL season has 17 weeks
        try:
            print(f"Fetching data for Week {week}...")
            url = f"https://api.sportsdata.io/v3/nfl/stats/json/BoxScoreByTeamFinal/{season}/{week}/{team}"
            headers = {"Ocp-Apim-Subscription-Key": api_key}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()

                # Find the team data in TeamGames
                team_game = next(
                    (game for game in data["TeamGames"] if game["Team"] == team),
                    None
                )

                if team_game:
                    games = {
                        "Week": f"Week {week}",
                        "Team": team_game["Team"],  # Add the team name
                        "Touchdowns": team_game["Touchdowns"],
                        "Score": team_game["Score"],
                        "OpponentScore": team_game["OpponentScore"],
                        "Result": "Win" if team_game["Score"] > team_game["OpponentScore"] else "Loss"
                    }
                    all_games.append(games)
                else:
                    print(f"No matching game data found for team {team} in Week {week}.")
            else:
                print(f"API Error for Week {week}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error fetching data for Week {week}: {e}")

    return pd.DataFrame(all_games)

def generate_mock_data(season, team):
    """Generates mock data for team performance."""
    games = [f"Week {i+1}" for i in range(1, 18)]
    touchdowns = [random.randint(0, 7) for _ in range(17)]
    scores = [random.randint(10, 35) for _ in range(17)]
    opponent_scores = [random.randint(10, 35) for _ in range(17)]
    results = ["Win" if scores[i] > opponent_scores[i] else "Loss" for i in range(17)]

    return pd.DataFrame({
        "Week": games,
        "Team": [team] * 17,
        "Touchdowns": touchdowns,
        "Score": scores,
        "OpponentScore": opponent_scores,
        "Result": results
    })

if __name__ == "__main__":
    api_key = input("Enter your NFL API key (leave blank for mock data): ")
    team = input("Enter the NFL team abbreviation (e.g., DAL for Dallas Cowboys): ")
    season = input("Enter the NFL season year (e.g., 2023): ")

    if api_key:
        data = fetch_nfl_box_scores(api_key, team, season)
    else:
        data = generate_mock_data(season, team)

    if data is not None and not data.empty:
        data.to_csv("../data/team_performance.csv", index=False)
        print("Data saved to ../data/team_performance.csv")
    else:
        print("No data available or failed to fetch data.")
