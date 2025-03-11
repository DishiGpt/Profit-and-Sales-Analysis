import numpy as np

class CrosswordGame:
    def __init__(self):
        self.grid = np.array([
            ['#', 'D', 'U', 'C', 'K', '#', 'D'],
            ['E', '#', '#', 'R', '#', '#', 'O'],
            ['M', '#', '#', 'O', '#', '#', 'V'],
            ['U', '#', 'S', 'W', 'A', 'N', 'E'],
            ['#', '#', 'P', '#', '#', '#', '#'],
            ['P', 'E', 'A', 'C', 'O', 'C', 'K'],
            ['#', '#', 'R', '#', '#', '#', '#'],
            ['P', 'A', 'R', 'R', 'O', 'T', '#'],
            ['#', '#', 'O', '#', '#', '#', '#'],
            ['#', '#', 'W', 'R', 'E', 'N', '#']
        ])
        self.words = {"4D": "SPARROW", "2A": "DUCK", "5A": "PEACOCK", "8A": "PARROT", "10A": "WREN"}
        self.scores = {"Player 1": 0, "Player 2": 0}
    
    def place_word(self, position, word, player):
        row, col = int(position[0]) - 1, 0 if position[1] == 'A' else int(position[0]) - 1
        direction = 'H' if position[1] == 'A' else 'V'
        
        if direction == 'H':
            correct = all(self.grid[row, col + i] == word[i] or self.grid[row, col + i] == '#' for i in range(len(word)))
        else:
            correct = all(self.grid[row + i, col] == word[i] or self.grid[row + i, col] == '#' for i in range(len(word)))
        
        if correct:
            self.scores[player] += len(word)
        else:
            self.scores[player] -= 1
    
    def play_game(self):
        for _ in range(10):
            for player in self.scores.keys():
                for pos, word in self.words.items():
                    self.place_word(pos, word, player)
        
        best_players = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)[:2]
        print("Best solutions:")
        for player, score in best_players:
            print(f"{player}: {score} points")

if __name__ == "__main__":
    game = CrosswordGame()
    game.play_game()
