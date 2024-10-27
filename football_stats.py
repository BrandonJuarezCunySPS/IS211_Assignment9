import requests
from bs4 import BeautifulSoup

# URL for CBS NFL Stats Touchdowns
url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"

def scrape_football_stats():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the specific table
    table = soup.find('table')
    if table is None:
        print("No table found on the page.")
        return

    rows = table.find_all('tr')[1:21]  # Skip header and take top 20

    print("Top 20 Players in Touchdowns:")
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 9:  # Ensure there are enough columns
            player_info = columns[0].text.strip()  # Player name with position and team
            touchdowns = columns[8].text.strip()  # Touchdowns

            # Split player_info to get name, position, and team
            parts = player_info.splitlines()
            player = parts[0].strip()  # First line is the player's name
            position = parts[1].strip()  # Second line is the player's position
            team = parts[3].strip() if len(parts) > 3 else "N/A"  # Third line is the team, default if not found

            # Print the formatted output
            print(f"Player: {player}, Position: {position}, Team: {team}, Touchdowns: {touchdowns}")

if __name__ == "__main__":
    scrape_football_stats()
    pass
