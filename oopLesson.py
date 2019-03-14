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


createfancybasketballplayer = BasketballPlayer("Very","Sexy",221, 100,999,1000,888)
#with the keyword you can change the order of the parametes
lebron = BasketballPlayer(first_name="Lebron", last_name="James", weight_kg=113, height_cm=203, points=27.2, rebounds=7.4, assists=7.2)
kev_dur = BasketballPlayer(points=27.2,first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, rebounds=7.1, assists=4)
print(createfancybasketballplayer.first_name)
print(createfancybasketballplayer.last_name)
print(lebron.weight_kg)
print(createfancybasketballplayer.points)
print(kev_dur.points)