#Deena Dayal

#import random
#coinFace = ['heads, 'tails']
#create a coin class w attributes:
    #coinValue = 0.0
    #coinName = 'none'
#set and get attributes
#behaviors:
    #getBalance- if coinFace is 'heads', add coinValue
    #coinFlip - randomly flips coin, return coinFace
#create coin objects(pass appropriate arguments)
#initialize a sum/total/result to 0.0
#while total is < 1.00
#flip the coins
#if coinFace == heads, add coinValue to total
#print updated total
#if total = 1.00
#print you win
#if total > 1.00
#print you lose

import random
class Coin:
    #faces of coin
    coinFace = ["Tails", "Heads"]

    def __init__(self, coinValue = 0.0, coinName = "None"):
        self.coinValue = coinValue
        self.coinName = coinName
        self.coinFace = "Heads" 
    
    def coinFlip(self):
        #random.choice() to choose random coin face from list
        self.coinFace = random.choice(Coin.coinFace)
    
    def getCoinFace(self):
        return self.coinFace
    
    def setCoinValue(self, coinValue):
        self.coinValue = coinValue

    def getCoinValue(self):
        return self.coinValue

    def setcoinName(self, coinName):
        self.coinName = coinName

    def getcoinName(self):
        return self.coinName
    
    def __str__(self): 
        return ("{}: {}".format(self.coinName, self.coinFace))
    

def main():
    coinTotal = 0.0
    #assign each coin to it's value and name
    quarter = Coin(0.25, "Quarter")
    nickel = Coin(0.05, "Nickel")
    dime = Coin(0.10, "Dime")
    print("Sum balance: ${:.2f}\n".format(coinTotal))
    while coinTotal < 1:
        quarter.coinFlip()
        nickel.coinFlip()
        dime.coinFlip()
        print("tossing the coins. . .\nHere are the sides:")
        print("{}\n{}\n{}\n".format(quarter, nickel, dime))
        if quarter.getCoinFace() == "Heads":
            coinTotal += quarter.getCoinValue()
        if nickel.getCoinFace() == "Heads":
            coinTotal += nickel.getCoinValue()
        if dime.getCoinFace() == "Heads":
            coinTotal += dime.getCoinValue()
        print("Sum balance: ${:.2f}\n".format(coinTotal))
    if coinTotal == 1.00:
        print("Game over. You win.")
    if coinTotal > 1.00:
        print("Game over. You lose.")

main()
