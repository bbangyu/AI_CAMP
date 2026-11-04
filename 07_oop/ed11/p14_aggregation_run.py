
class Player:
    def __init__(self, name:str):
        self.name = name


class Team:
    def __init__(self,players:list[Player]):
        self.players = players

player01 = Player("손흥민")
player02 = Player("이강인")

team = Team([player01, player02])