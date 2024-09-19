tournament_scores = [
       ['Player 1', [20, 30, 50]], 
       ['player 2', [60, 50, 30]], 
       ['player 3', [40, 50, 30]]
       ]
def find_winner(tournament_scores):
       store_averages_of_players = []
       for total_score_of_player in tournament_scores:
              average = sum(total_score_of_player[1]) / len(total_score_of_player[1])
              store_averages_of_players.append([total_score_of_player[0], average])
       store_averages_of_players.sort(key=lambda player: player[1], reverse=True)
       print(f'the winner is {store_averages_of_players[0][0]} with an average score { store_averages_of_players[0][1]:.2f}')

find_winner(tournament_scores)