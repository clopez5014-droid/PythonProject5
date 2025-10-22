# Define the Player class
class Player:
    def __init__(self, name, position):
        self.playerName = name
        self.playerPosition = position

    def __str__(self):
        return f"{self.playerName} - {self.playerPosition}"


# Define the NFLTeam class
class NFLTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players

    def display_team(self):
        print(f"Team Name: {self.teamName}")
        print("Players:")
        for player in self.players:
            print(f" - {player}")


# Create Player objects
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# Add them to a list
playerList = [player1, player2, player3, player4]

# Create the team
team = NFLTeam("Smashmouth Football", playerList)

# Output the team info
team.display_team()
