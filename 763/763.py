divisions = 10000

while divisions == 0:
    divisions = input("Enter Amoeaba Divisions (INT): ")
    try:
        divisions = int(divisions)
    except:
        divisions = 0
        print("Please enter an INT other than 0")

amoebas = 2*divisions+1

class PetriDish:
    def __init__(self, culture):
        self.culture = culture
        self.steps = []

    def reproduce(self, amoeba, index):
        x = (amoeba[0]+1, amoeba[1], amoeba[2])
        y = (amoeba[0], amoeba[1]+1, amoeba[2])
        z = (amoeba[0], amoeba[1], amoeba[2]+1)

        if x in self.culture:
            valid = False
        elif y in self.culture: 
            valid = False
        elif z in self.culture:
            valid = False
        else: # Valid division found
            valid = True
            self.culture.append(x)
            self.culture.append(y)
            self.culture.append(z)
            self.steps.append(self.culture.pop(index))


print("Total Amoebas: " + str(amoebas))

petri_dish = PetriDish([(0,0,0)])
idx = 0
while len(petri_dish.culture) < amoebas:
    petri_dish.reproduce(petri_dish.culture[idx], idx)
    idx +=1
    if idx > len(petri_dish.culture):idx=0

print("Amoebas Simulated: " + str(len(petri_dish.culture)))
