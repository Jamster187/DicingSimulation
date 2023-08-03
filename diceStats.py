import random
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

total = 30000
performance51 = []
performance52 = []
performance53 = []
performance54 = []
performance55 = []

def roll():
    roll=random.randint(1, 100)
    return roll

def betamount():
    bet = random.randint(1,300)
    return bet

def d55x2():
    if roll() > 55:
        return "LOSS"
    else:
        return "WIN"

def d54x2():
    if roll() > 54:
        return "LOSS"
    else:
        return "WIN"

def d53x2():
    if roll() > 53:
        return "LOSS"
    else:
        return "WIN"

def d52x2():
    if roll() > 52:
        return "LOSS"
    else:
        return "WIN"
def d51x2():
    if roll() > 51:
        return "LOSS"
    else:
        return "WIN"
    
def wager(i):
    global total
    bet = betamount()
    if i == 51:
        result = d51x2()
    if i == 52:
        result = d52x2()
    if i == 53:
        result = d53x2()
    if i == 54:
        result = d54x2()
    if i == 55:
        result = d55x2()
    if result == "WIN":
        total += bet
    else:
        total -= bet
    return

def trial(trialSize):
    global total
    for i in range(trialSize):
        wager(51)
        performance51.append(total)
    total = 30000
    for i in range(trialSize):
        wager(52)
        performance52.append(total)
    total = 30000
    for i in range(trialSize):
        wager(53)
        performance53.append(total)
    total = 30000
    for i in range(trialSize):
        wager(54)
        performance54.append(total)
    total = 30000
    for i in range(trialSize):
        wager(55)
        performance55.append(total)
    total = 30000

def hl(perfList):
    low = min(perfList)
    high = max(perfList)
    print("High: ", high, "low: ", low)
            

def plotGraph():
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    for i in range(len(performance51)):
        x1.append(i)
        y1.append(performance51[i])
    for i in range(len(performance52)):
        x2.append(i)
        y2.append(performance52[i])
    for i in range(len(performance53)):
        x3.append(i)
        y3.append(performance53[i])
    for i in range(len(performance54)):
        x4.append(i)
        y4.append(performance54[i])
    for i in range(len(performance55)):
        x5.append(i)
        y5.append(performance55[i])
    plt.figure(1)
    plt.plot(x1, y1, label="51x2")
    plt.plot(x2, y2, label="52x2")
    plt.plot(x3, y3, label="53x2")
    plt.plot(x4, y4, label="54x2")
    plt.plot(x5, y5, label="55x2")
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
    
# Dice Stats

trial(1000000)
hl(performance51)
hl(performance52)
hl(performance53)
hl(performance54)
hl(performance55)
plotGraph()