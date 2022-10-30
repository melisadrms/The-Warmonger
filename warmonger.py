from tabulate import tabulate
class Faction: 
    def __init__(self, name,enemypointer1, enemypointer2, units=0, attackpoint=0, healthpoint=0, regnumber=0, totalhealth=0, flag=True):
        self.name = name
        self.enemypointer1 = enemypointer1
        self.enemypointer2 = enemypointer2
        self.units = units
        self.attackpoint = attackpoint
        self.healthpoint = healthpoint
        self.regnumber = regnumber
        self.totalhealth = totalhealth
        self.flag = True
  
    def AssignEnemies(self):
        if self.name == "Orcs":
            self.enemypointer1 = Dwarves()
            self.enemypointer2 = Elves()
        if self.name == "Dwarves":
            self.enemypointer1 = Orcs()
            self.enemypointer2 = Elves()
        if self.name == "Elves":
            self.enemypointer1 = Orcs()
            self.enemypointer2 = Dwarves()
    
    def PerformAttack(attacker):
        if attacker.name == "Orcs":
            Orcs.PerformAttack(attacker, attacker.enemypointer1, attacker.enemypointer2)
        if attacker.name == "Dwarves":
            Dwarves.PerformAttack(attacker, attacker.enemypointer1, attacker.enemypointer2)
        if attacker.name == "Elves":
            Elves.PerformAttack(attacker, attacker.enemypointer1, attacker.enemypointer2)

    # def ReceiveAttack(receiver):
    #     if receiver.name == "Orcs":
    #         Orcs.ReceiveAttack(receiver,)

    def PrintFaction(self):

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

        if self.name == "Orcs":
            print(tabulate(d)) 
        elif self.name == "Dwarves":
            print(tabulate(d))
        elif self.name == "Elves":
            print(tabulate(d))

class Orcs(Faction):

    def __init__(self):
        self.name = "Orcs"
        self.units = 50
        self.attackpoint = 500
        self.healthpoint = 500
        self.regnumber = 500
        self.totalhealth = self.units * self.healthpoint
        self.flag = True
    
    def PerformAttack(self, enemy1, enemy2):
        if (enemy1.flag==False and enemy2.flag==True) or (enemy1.flag==True and enemy2.flag==False):
            attack = self.attackpoint * self.units
        elif enemy1.flag==True and enemy2.flag==True:
            if enemy1.name == "Elves":
                attack = (self.units * 0.7) * self.attackpoint
                enemy1.ReceiveAttack(attack,self.name)
            if enemy2.name == "Elves":
                attack = (self.units * 0.7) * self.attackpoint
                enemy2.ReceiveAttack(attack,self.name)
            if enemy1.name == "Dwarves" : 
                attack = (self.units * 0.3) * self.attackpoint
                enemy1.ReceiveAttack(attack)
            if enemy2.name == "Dwarves" :
                attack = (self.units * 0.3) * self.attackpoint
                enemy2.ReceiveAttack(attack)

    def ReceiveAttack(self,attack,attacker):
        if attacker == "Elves":
            attack -= attack * 0.75
        elif attacker == "Dwarves":
            attack -= attack * 0.8
        self.units -= attack / self.healthpoint
    
    def PurchaseWeapon(self,weaponPoints):
        self.attackpoint += 2*weaponPoints
        gold_to_return = 20*weaponPoints
        print(gold_to_return)
        return gold_to_return
    
    def PurchaseArmors(self,armorPoints):
        self.healthpoint = self.healthpoint + 3*armorPoints
        gold_to_return = 1*armorPoints
        return gold_to_return

    def printorc():
        print("Stop running, you’ll only die tired!")

class Dwarves(Faction):
    def __init__(self):
        self.name = "Dwarves"
        self.units = 500
        self.attackpoint = 500
        self.healthpoint = 500
        self.regnumber = 500
        self.totalhealth = self.units * self.healthpoint
        self.flag = True

    def PerformAttack(self, enemy1, enemy2):
        if (enemy1.flag==False and enemy2.flag==True) or (enemy1.flag==True and enemy2.flag==False):
            self.attack = self.attackpoint * self.units
            print("")
        elif enemy1.flag==True and enemy2.flag==True:
            if enemy1.name == "Orcs":
                self.attack = (self.units * 0.5) * self.attackpoint
                enemy1.ReceiveAttack(self.attack,self.name)
            if enemy2.name == "Orcs":
                self.attack = (self.units * 0.5) * self.attackpoint
                enemy2.ReceiveAttack(self.attack,self.name)

            if enemy1.name == "Elves" : 
                self.attack = (self.units * 0.5) * self.attackpoint
                enemy1.ReceiveAttack(self.attack,self.name)
            if enemy2.name == "Elves" :
                self.attack = (self.units * 0.5) * self.attackpoint
                enemy2.ReceiveAttack(self.attack,self.name)

    def ReceiveAttack(self,attack):
        self.units -= attack / self.healthpoint

    def PurchaseWeapon(self,weaponPoints):
        self.attackpoint += weaponPoints
        gold_to_return = 10*weaponPoints
        return gold_to_return
    
    def PurchaseArmors(self,armorPoints):
        self.healthpoint = self.healthpoint + 2* armorPoints
        gold_to_return = 3*armorPoints
        return gold_to_return
    
    def printdwarves():
        print("Taste the power of our axes!")

class Elves(Faction):
    def __init__(self):
        self.name = "Elves"
        self.units = 500
        self.attackpoint = 500
        self.healthpoint = 500
        self.regnumber = 500
        self.totalhealth = self.units * self.healthpoint
        self.flag = True 

    def PerformAttack(self, enemy1, enemy2):

        if (enemy1.flag==False and enemy2.flag==True) or (enemy1.flag==True and enemy2.flag==False):
            self.attack = self.attackpoint * self.units
        elif enemy1.flag==True and enemy2.flag==True:
            if enemy1.name == "Orcs":
                self.attack = (self.units * 0.6) * self.attackpoint
                enemy1.ReceiveAttack(self.attack,self.name)
            if enemy2.name == "Orcs":
                self.attack = (self.units * 0.6) * self.attackpoint
                enemy2.ReceiveAttack(self.attack,self.name)

            if enemy1.name == "Dwarves" : 
                self.attack = (self.units * 0.4) * (self.attackpoint*1.5)
                enemy1.ReceiveAttack(self.attack,self.name)
            if enemy2.name == "Dwarves" :
                self.attack = (self.units * 0.4) * (self.attackpoint*1.5)
                enemy2.ReceiveAttack(self.attack,self.name)

    def ReceiveAttack(self,attack,attacker):
        if attacker == "Orcs":
            attack += attack * 1.25
        elif attacker == "Dwarves":
            attack -= attack * 0.75
        self.units -= attack / self.healthpoint
    
    def PurchaseWeapon(self,weaponPoints):
        self.attackpoint += weaponPoints * 2
        gold_to_return = 15*weaponPoints
        return gold_to_return
    
    def PurchaseArmors(self,armorPoints):
        self.healthpoint = self.healthpoint + 4* armorPoints
        gold_to_return = 5* armorPoints
        return gold_to_return

    def printelves():
        print("You cannot reach our elegance.") 

class Merchant():
    def __init__(self, firstfaction=0, secondfaction=0, thirdfaction=0, weaponpointfirst=0, armorpointfirst=0, revenue=0, weaponpointleft = 0, armorpointleft = 0):
        self.firstfaction = firstfaction
        self.secondfaction = secondfaction
        self.thirdfaction = thirdfaction
        self.weaponpointfirst = 500
        self.armorpointfirst = 500
        self.revenue = 0
        self.weaponpointleft = weaponpointleft 
        self.armorpointleft = armorpointleft

    def AssignFactions(player):
        if player.name == "Orcs":
            player.enemypointer1 == Dwarves()
            player.enemypointer2 == Elves()
        elif player.name == "Dwarves":
            player.enemypointer1 == Orcs()
            player.enemypointer2 == Elves()
        elif player.name == "Elves":
            player.enemypointer1 == Orcs()
            player.enemypointer2 == Dwarves()

    def sellWeapons(self ,player, weaponpoint):
        gold_to_return = 0
        if player.flag == False:
            print("The faction you want to sell weapons is dead!")
        elif weaponpoint > self.weaponpointleft:
            print("You try to sell more weapons than you have in possession.")
        else:
            player.PurchaseWeapon(weaponpoint)
            self.weaponpointleft = self.weaponpointleft - weaponpoint
            print("Weapons Sold!")
            self.revenue += gold_to_return
            print(self.revenue)

    def sellArmors(self ,player, armorpoint):
        if player.flag == False:
            print("The faction you want to sell armors is dead!")
        elif armorpoint > self.armorpointleft:
            print("You try to sell more armors than you have in possession.")
        else:
            player.PurchaseArmor(armorpoint)
            self.armorpointleft = self.armorpointleft - armorpoint
            print("Armors Sold!")
    
    def EndTurn(self):
        self.weaponpointleft = self.weaponpointfirst
        self.armorpointleft = self.armorpointfirst
        
def Game (): 
    msg = "Welcome to The Warmonger Game"
    print(msg)
    player1 = Orcs()
    player2 = Dwarves()
    player3 = Elves()
    Faction.AssignEnemies(player1)
    Faction.AssignEnemies(player2)
    Faction.AssignEnemies(player3)
    merchant = Merchant()
    Faction.PerformAttack(player1)
    merchant.weaponpointleft = merchant.weaponpointfirst
    Merchant.sellWeapons(merchant,player1,30)

#236 gold_to_return'e bakacaksın

Game()




