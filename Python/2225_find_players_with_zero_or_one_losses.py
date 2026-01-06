from collections import Counter

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        player_wins = Counter([winner for winner, _ in matches])
        player_losses = Counter([loser for _, loser in matches])

        flawless_players = []
        for winner, _ in player_wins.items():
            if winner not in player_losses:
                flawless_players.append(winner)
            
        one_loss_players = []
        for loser, losses in player_losses.items():
            if losses == 1:
                one_loss_players.append(loser)
        
        return [sorted(flawless_players), sorted(one_loss_players)]

