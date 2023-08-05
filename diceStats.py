import random
import matplotlib.pyplot as plt

total = 30000
performances = [[], [], [], [], []]

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
    count = 0
    for x in range(51, 56, 1):
        for i in range(trialSize):
            wager(x)
            performances[count].append(total)
        resetTotal()
        count += 1
        
def hl(perfList):
    #prints the high and low of the casino bankroll during the trial given
    #the corresponding house edge list
    low = min(perfList)
    high = max(perfList)
    print("High: ", high, "low: ", low)
            
def plotGraph():
    x, y = [], [ [], [], [], [], [] ]
    listSize = len(performances[0])
    
    for i in range(listSize):
        x.append(i)
    for z in range(0, 5, 1):
        for i in range(listSize):
            y[z].append(performances[z][i])       
    plt.figure(1)
    plt.plot(x, y[0], label="51x2")
    plt.plot(x, y[1], label="52x2")
    plt.plot(x, y[2], label="53x2")
    plt.plot(x, y[3], label="54x2")
    plt.plot(x, y[4], label="55x2")
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
plotGraph()
