print("You are a plant!")


class Plant:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.life = 10
        self.xp = 0
        self.level = 1

    def drink(self):
        # Absorb water through roots.
        self.addxp(10)
        print("You have absorbed water +10 XP")

    def breath(self):
        # Photosynthesise.
        self.addxp(20)
        self.life += 5
        print("You have gone through photosynthesis and grown +20 XP +5 HP")

    def addxp(self, xp):
        self.xp += xp
        if self.xp > 100:
            self.level += 1
            self.xp = 0
            print("Plant has reached level", self.level)


p1 = Plant()
print("XP", p1.xp, "HP", p1.life)

print("I am a human")


class Human:
    def __init__(self):
        self.x = 5
        self.y = 10
        self.life = 50
        self.xp = 0

    def water(self):
        # Give water to the plant.
        self.xp += 10
        p1.drink()
        print("I have watered the plant +10 XP")


h1 = Human()
print("XP", h1.xp, "HP", h1.life)

for _ in range(8):
    h1.water()

p1.drink()
p1.breath()

print("Plant", "XP", p1.xp, "HP", p1.life)
print("Human", "XP", h1.xp, "HP", h1.life)