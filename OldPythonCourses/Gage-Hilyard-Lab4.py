# --------------------------------------
# CSCI 127, Lab 4
# February 7, 2019
# Gage Hilyard
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")

# --------------------------------------

def process_seasons(seasons):
    for i in range(0, len(seasons)):
        process_season(i+1, seasons[i][0], seasons[i][1])
        total_wins = 0
        total_ties = 0
        total_losses = 0
        total_points = seasons[i][1]
        total_games = seasons[i][0]
        while total_points % 3 != 0:
            total_ties += 1
            total_games += -1
            total_points += -1
        total_wins = total_points/3
        total_games += -total_wins
        total_losses = total_games
        print(str(int(total_wins))+'-'+str(int(total_ties))+'-'+str(int(total_losses)))
        while(total_losses >= 2 and total_wins >= 0):
            total_wins += -1
            total_losses += -2
            total_ties += 3
            print(str(int(total_wins))+'-'+str(int(total_ties))+'-'+str(int(total_losses)))
        print("")

# --------------------------------------

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]
    process_seasons(soccer_seasons)

# --------------------------------------

main()
