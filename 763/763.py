divisions = 0

while divisions == 0:
    divisions = input("Enter Amoeaba Divisions (INT): ")
    try:
        divisions = int(divisions)
    except:
        divisions = 0
        print("Please enter an INT other than 0")

amoebas = 2*divisions+1

petri_dish = [[0,0,0]]

def valid_division(amoeba, divide):
    x = [amoeba[0]+1, amoeba[1], amoeba[2]]
    y = [amoeba[0], amoeba[1]+1, amoeba[2]]
    z = [amoeba[0], amoeba[1], amoeba[2]+1]

    if x in petri_dish:
        valid = False
    elif y in petri_dish: 
        valid = False
    elif z in petri_dish:
        valid = False
    else: # Valid division found
        valid = True

        if divide: # Only divide if a valid division is found
            petri_dish.append(x)
            petri_dish.append(y)
            petri_dish.append(z)

            petri_dish.remove(amoeba)

    return valid

print("Total Amoebas: " + str(amoebas))
