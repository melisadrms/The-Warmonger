from tabulate import tabulate
class Faction: 
    def __init__(self, name=" ", enemypointer1=0, enemypointer2=0 , units=0, attackpoint=0, healthpoint=0, regnumber=0, totalhealth=0, flag=True):
        self.name = name
        self.enemypointer1 = enemypointer1
        self.enemypointer2 = enemypointer2
        self.units = units
        self.attackpoint = attackpoint
        self.healthpoint = healthpoint
        self.regnumber = regnumber
        self.totalhealth = totalhealth
        self.flag = flag
    


    def PrintFaction(self, player):
        print("zabaduaad")
        if self.flag == True:
            status = "Alive"
        else: 
            status = "Defeat"

        if player.name == "Orcs":
            print(tabulate([
                ['Status:', status],
                ['Number of Units', self.units]],
                headers=['Faction Name:', self.name]))
            
        elif player.name == "Dwarves":
            print("Dwarves")
        elif player.name == "Elves":
            print("Elves")

class Orcs(Faction):

    def __init__(self):
        self.name = "Orcs"
        self.enemypointer1 = 2
        self.enemypointer2 = 3
        self.units = int(input('Please give a unit for the Orcs Faction:'))
        self.attackpoint = int(input('Please give an attack point for the Orcs Faction:'))
        self.healthpoint = int(input('Please give an health point for the Orcs Faction:'))
        self.regnumber = int(input('Please give an regeneration number for the Orcs Faction:'))
        self.totalhealth = self.units * self.healthpoint
        self.flag = True

class Dwarves(Faction):
    def __init__(self):
        self.name = "Dwarves"
        self.enemypointer1 = 1
        self.enemypointer2 = 3
        self.units = int(input('Please give a unit for the Dwarves Faction:'))
        self.attackpoint = int(input('Please give an attack point for the Dwarves Faction:'))
        self.healthpoint = int(input('Please give an health point for the Dwarves Faction:'))
        self.regnumber = int(input('Please give an regeneration number for the Dwarves Faction:'))
        self.totalhealth = self.units * self.healthpoint
        self.flag = True

class Elves(Faction):
    def __init__(self):
        self.name = "Elves"
        self.enemypointer1 = 1
        self.enemypointer2 = 2
        self.units = int(input('Please give a unit for the Elves Faction:'))
        self.attackpoint = int(input('Please give an attack point for the Elves Faction:'))
        self.healthpoint = int(input('Please give an health point for the Elves Faction:'))
        self.regnumber = int(input('Please give an regeneration number for the Elves Faction:'))
        self.totalhealth = self.units * self.healthpoint
        self.flag = True    

class Merchant():
    def __init__(self, firstfraction, secondfraction, thirdfraction, weaponpointfirst, armorpointfirst, revenue, weaponpointleft, armorpointleft):
        self.firstfraction = firstfraction
        self.secondfraction = secondfraction
        self.thirdfraction = thirdfraction
        self.weaponpointfirst = weaponpointfirst
        self.armorpointfirst = armorpointfirst
        self.revenue = revenue
        self.weaponpointleft = weaponpointleft
        self.armorpointleft = armorpointleft

def Game (): 

    msg = "Welcome to The Warmonger Game"
    print(msg)
    player1 = Orcs()
    player2 = Dwarves()
    player3 = Elves()
    player1.PrintFaction(player1)

Game()




