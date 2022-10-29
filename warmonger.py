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
        self.flag = True
    
    def AssignEnemies(player):
        print("")
        if player.name == "Orcs":
            player.enemypointer1 == 2
            player.enemypointer2 == 3
        elif player.name == "Dworves":
            player.enemypointer1 == 1
            player.enemypointer2 == 3
        elif player.name == "Elves":
            player.enemypointer1 == 1
            player.enemypointer2 == 2


    def PrintFaction(self, player):

        if self.flag == True:
            status = "Alive"
        else: 
            status = "Defeat"

        d = [
            ["Faction Name:  ",  self.name],
            ["Status: ", status],
            ["Number of Units: ", self.units],
            ["Attack Point: ", self.attackpoint],
            ["Health Point: ", self.healthpoint],
            ["Unit Regen Number: ", self.regnumber],
            ["Total Faction Health: ", self.totalhealth]
        ]

        if player.name == "Orcs":
            print(tabulate(d)) 
        elif player.name == "Dwarves":
            print(tabulate(d))
        elif player.name == "Elves":
            print(tabulate(d))

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
    
    def performAttack():
        print("")
    
    def printorc():
        print("Stop running, you’ll only die tired!")

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
    
    def printdwarves():
        print("Taste the power of our axes!")

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

    def printelves():
        print("You cannot reach our elegance.") 

class Merchant(Faction):
    def __init__(self, firstfaction=0, secondfaction=0, thirdfaction=0, weaponpointfirst=0, armorpointfirst=0, revenue=0, weaponpointleft = 0, armorpointleft = 0):
        self.firstfaction = firstfaction
        self.secondfaction = secondfaction
        self.thirdfaction = thirdfaction
        self.weaponpointfirst = int(input("Please give a starting weapon point: "))
        self.armorpointfirst = int(input("Please give an starting armor point: "))
        self.revenue = 0
        self.weaponpointleft = weaponpointleft 
        self.armorpointleft = armorpointleft

    def AssignFactions(player):
        if player.name == "Orcs":
            player.firstfaction = 1
            player.secondfaction = 0
            player.thirdfaction = 0
        if player.name == "Dworves":
            player.firstfaction = 0
            player.secondfaction = 1
            player.thirdfaction = 0
        if player.name == "Elves":
            player.firstfaction = 0
            player.secondfaction = 0
            player.thirdfaction = 1
    
    def sellWeapons(self ,player, weaponpoint):
        if player.flag == False:
            print("The faction you want to sell weapons is dead!")
        elif weaponpoint > self.weaponpointleft:
            print("You try to sell more weapons than you have in possession.")
        else:
            player.attackpoint += weaponpoint
            self.weaponpointleft = self.weaponpointleft - weaponpoint
            print("Weapons Sold!")

    def sellArmors(self ,player, armorpoint):
        if player.flag == False:
            print("The faction you want to sell armors is dead!")
        elif armorpoint > self.armorpointleft:
            print("You try to sell more armors than you have in possession.")
        else:
            player.regnumber += armorpoint
            self.armorpointleft = self.armorpointleft - armorpoint
            print("Armors Sold!")
    
    def EndTurn(self):
        self.weaponpointleft = self.weaponpointfirst
        self.armorpointleft = self.armorpointfirst
        


def Game (): 

    msg = "Welcome to The Warmonger Game"
    print(msg)
    #player1 = Orcs()
    #player2 = Dwarves()
    player3 = Elves()
    merchant = Merchant()
    merchant.weaponpointleft = merchant.weaponpointfirst
    merchant.armorpointleft = merchant.armorpointfirst
    player3.PrintFaction(player3)
    print(merchant.weaponpointleft)
    Merchant.sellWeapons(merchant,player3,20)
    player3.PrintFaction(player3)
    Merchant.sellWeapons(merchant,player3,20)
    print(merchant.weaponpointleft)
    Merchant.sellWeapons(merchant,player3,20)
    print(merchant.weaponpointleft)

Game()




