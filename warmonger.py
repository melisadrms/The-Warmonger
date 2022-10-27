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

class Orcs(Faction):
    def __init__(self, name, enemypointer1, enemypointer2, units, attackpoint, healthpoint, regnumber, totalhealth, flag):
        super().__init__(name, enemypointer1, enemypointer2, units, attackpoint, healthpoint, regnumber, totalhealth, flag)
        
    def constructor(orc):
        lala = int(input("enter input here:"))
        print(lala)
    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.name,self.enemypointer1, self.healthpoint, 
            self.regnumber))     
class Dwarves(Faction):
    def __init__(self, name, enemypointer1, enemypointer2, units, attackpoint, healtpoint, regnumber, totalhealth, flag):
        super().__init__(name, enemypointer1, enemypointer2, units, attackpoint, healtpoint, regnumber, totalhealth, flag)
class Elves(Faction):
    def __init__(self, name, enemypointer1, enemypointer2, units, attackpoint, healtpoint, regnumber, totalhealth, flag):
        super().__init__(name, enemypointer1, enemypointer2, units, attackpoint, healtpoint, regnumber, totalhealth, flag)

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
     

Game()



