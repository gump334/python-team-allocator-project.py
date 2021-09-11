#random module comes with a lot of methods to move around numbers
import random
#my list of players 
players = ["Matt", "Amy", "Bob", "Jan", "Rob", "Donna", "Terrell", "Mary", "Tim", "Becky"]

print("Welcome to Team Allocator!")
#While loop over team until you decide if you want to keep the current team
while True:
    random.shuffle(players)
    team1 = players[:len(players)//2]
    print("Team 1 captain: " + random.choice(team1))
    print("Team 1:")
    for player in team1:
      print(player)
    print()

    team2 = players[len(players)//2:]
    print("Team 2 captain: " + random.choice(team2))
    print("Team 2:")
    for player in team2:
      print(player)
    response = input("Pick teams again? Type y or n: ")
    if response.lower() == "n":
        break