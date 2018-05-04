class Doge():
    def __init__(self, dogColor, dogBreed):
        self.color = dogColor
        self.breed = dogBreed

    def fuck(self, newDog):
        return self.color, self.breed[:3]+newDog.breed[2:5]


dog1 = Doge("Brown","Chihuahua")
dog2 = Doge("White","Husky Brandy")
dog3 = Doge(dog1.fuck(dog2)[0], dog1.fuck(dog2)[1])

print(dog3.breed)