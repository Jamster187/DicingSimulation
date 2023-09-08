import random
import matplotlib.pyplot as plt

total = 30000
performances = [[], [], [], [], [], [], [], [], [], [], []]

def roll():
    roll=random.randint(1, 100)
    return roll

def betamount():
    bet = random.randint(1,300)
    return bet

def resetTotal():
    global total
    total = 30000
    
def test():
    resultsList = []
    for i in range(10000):
        roll123 = roll()
        resultsList.append(roll123)
    onecount = resultsList.count(1)
    hundredcount = resultsList.count(100)
    print(onecount, hundredcount)

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
    if i == 50:
        if result == "WIN":
            total += bet
        else:
            total -= (bet * 0.9)  
    else:
        if result == "WIN":
            total += bet
        else:
            total -= bet
    return

def trial(trialSize):
    # runs a sample of trialSize size, through each house edge condition and
    # appends the results in their respective lists
    count = 0
    for x in range(50, 61, 1):
        for i in range(trialSize):
            wager(x)
            performances[count].append(total)
        resetTotal()
        count += 1
            
def plotGraph():
    x, y = [], [ [], [], [], [], [], [], [], [], [], [], [] ]
    listSize = len(performances[0])
    
    for i in range(listSize):
        x.append(i)
        
    for z in range(0, 11, 1):
        for i in range(listSize):
            y[z].append(performances[z][i])
            
    plt.figure(1)
    plt.plot(x, y[0], label="50x2 5% rake")
    plt.plot(x, y[1], label="51x2")
    plt.plot(x, y[2], label="52x2")
    plt.plot(x, y[3], label="53x2")
    plt.plot(x, y[4], label="54x2")
    plt.plot(x, y[5], label="55x2")
    plt.plot(x, y[6], label="56x2")
    plt.plot(x, y[7], label="57x2")
    plt.plot(x, y[8], label="58x2")
    plt.plot(x, y[9], label="59x2")
    plt.plot(x, y[10], label="60x2")
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

trial(100000)
plotGraph()
