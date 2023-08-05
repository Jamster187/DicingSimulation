import random
import matplotlib.pyplot as plt

total = 30000
performance51, performance52, performance53, performance54, performance55 \
= [], [], [], [], []

def roll():
    roll=random.randint(1, 100)
    return roll

def betamount():
    bet = random.randint(1,300)
    return bet

def resetTotal():
    global total
    total = 30000
    return 
    
def dYx2(Y):
    #This determines the house edge i.e y = 51 will be a 51x2 dice
    if roll() > Y:
        return "LOSS"
    else:
        return "WIN"
    
def wager(i):
    # simulates a dYx2 bet of random size
    global total
    bet = betamount()
    result = dYx2(i)
    if result == "WIN":
        total += bet
    else:
        total -= bet
    return

def trial(trialSize):
    # runs a sample of trialSize size, through each house edge condition and
    # appends the results in their respective lists
    for i in range(trialSize):
        wager(51)
        performance51.append(total)
    resetTotal()
    for i in range(trialSize):
        wager(52)
        performance52.append(total)
    resetTotal()
    for i in range(trialSize):
        wager(53)
        performance53.append(total)
    resetTotal()
    for i in range(trialSize):
        wager(54)
        performance54.append(total)
    resetTotal()
    for i in range(trialSize):
        wager(55)
        performance55.append(total)
    resetTotal()

def hl(perfList):
    #prints the high and low of the casino bankroll during the trial given
    #the corresponding house edge list
    low = min(perfList)
    high = max(perfList)
    print("High: ", high, "low: ", low)
            

def plotGraph():
    x, y1, y2, y3, y4, y5 = [], [], [], [], [], []
    
    for i in range(len(performance51)):
        x.append(i)
        y1.append(performance51[i])
    for i in range(len(performance52)):
        y2.append(performance52[i])
    for i in range(len(performance53)):
        y3.append(performance53[i])
    for i in range(len(performance54)):
        y4.append(performance54[i])
    for i in range(len(performance55)):
        y5.append(performance55[i])
        
    plt.figure(1)
    plt.plot(x, y1, label="51x2")
    plt.plot(x, y2, label="52x2")
    plt.plot(x, y3, label="53x2")
    plt.plot(x, y4, label="54x2")
    plt.plot(x, y5, label="55x2")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Bets")
    plt.ylabel("Bankroll $")
    plt.xlim(0, 10**8)
    plt.ylim(0, 10**8)
    plt.grid(axis="x")
    plt.style="grid"
    plt.legend()
    plt.show()
    
# Dice Simulation

trial(1000000)
hl(performance51), hl(performance52), hl(performance53), hl(performance54), \
hl(performance55)
plotGraph()
