#create a class
class BasketballPlayer():
    first_name = "abc"
    #initialize a new object / contructor
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists, badexample):
        #bad
        first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        #bad bad bad
        badexample = badexample

createfancybasketballplayer = BasketballPlayer("Very","Sexy",221, 100, 1000,1000,1000,1)
print(createfancybasketballplayer.first_name)
print(createfancybasketballplayer.last_name)
#bad bad bad
#print(createfancybasketballplayer.badexample)