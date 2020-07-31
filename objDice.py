import secrets

class Die:
    def __init__(self, faces):
        self.faces = faces

    def __str__(self):
        return  "Face Value: {} ".format(str(faces))

#----------------------------------------------------------------------

class Roll:
    def __init__(self, how_many, dice_list):
        self.how_many = how_many
        self.dice_list = dice_list

    def roll_dice():
        results_list = []
        for i in len(dice_list):
            results_list.append(secrets.randbelow(dice_list[i]))
        return results_list


#----------------------------------------------------------------------

class Dice_Collection:
    def __init__(self):
        self.dice_list = []

    def add_dice_to_list(self, face_value, how_many):
        self.dice_list.append([face_value, how_many])
        

#----------------------------------------------------------------------

def main():
    which_die = input("Which die? ")
    how_many = input("how_many? ")
    
    diceCollection = new Dice_Collection()
    diceList = diceCollection.
    roll = new Roll()
   

main()
