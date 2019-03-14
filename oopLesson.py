#create a class
class BasketballPlayer():
    first_name = "abc"

    #initialize a new object / contructor
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.__attr = 0 #private variable

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    #common used "workaround" to give access to private attributes (if its needed)
    def get_private_attribute(self): #public function
        return self.__attr

    def set_private_attribute(self,value): #public function
        self.__attr = value



createfancybasketballplayer = BasketballPlayer("Very","Sexy",221, 100,999,1000,888)
#with the keyword you can change the order of the parametes
lebron = BasketballPlayer(first_name="Lebron", last_name="James", weight_kg=113, height_cm=203, points=27.2, rebounds=7.4, assists=7.2)
kev_dur = BasketballPlayer(points=27.2,first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, rebounds=7.1, assists=4)
print(createfancybasketballplayer.first_name)
print(createfancybasketballplayer.last_name)
print(lebron.weight_kg)
print(createfancybasketballplayer.points)
print(kev_dur.points)

#create a list of our objects (players)
list_bball_players = [lebron, kev_dur]
print(type(list_bball_players))
#print the last and the firstname of our players
for player in list_bball_players:
    print(player.last_name + ", " + player.first_name)

print(lebron.weight_to_lbs())

"""
public private access example
"""

lebron.first_name="modified lebron"
print(lebron.first_name)
#private attribute access
#print(lebron.__attribute) --> will not work
print(lebron.get_private_attribute())
#lebron.__attribute = 10 --> will not work
lebron.set_private_attribute(10)
print(lebron.get_private_attribute())
