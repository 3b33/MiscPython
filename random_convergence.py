import random as rnd
import matplotlib.pyplot as plt

def diceThrowsToError(goal=1/6,error=.05):
    dt = [0,0,0,0,0,0] # dice throws
    dt[rnd.randint(0,5)] += 1 # prevent div by zero
    while not goal-goal*(error/2) <= dt[0]/sum(dt) <= goal+goal*(error/2):
        dt[rnd.randint(0,5)] += 1
        #if sum(dt) % 10**5 == 0:
        #    print(sum(dt),round(goal,3),error,round(dt[0]/sum(dt[1:]),6))
        #    print(dt)
    #print(dt)
    return sum(dt)

if __name__ == "__main__":
    errors = [.01]
    while errors[-1] < .99: errors.append(errors[-1]+1/50)
    errors[-1] = .99
    avgs = []
    for error in errors:
        lens = []
        for a in range(10**4):
            lens.append(diceThrowsToError(1/6, error))
        avgs.append(sum(lens)/len(lens))
        print('Error threshold %s achieved with an average of %s throws.' % (round(error,2), round(avgs[-1],2)))
    
    plt.figure(figsize=(6,6))
    plt.xlabel('Error threshold 0.01 - 0.99 (1-99%)')
    plt.ylabel('Average number of dice throws')
    plt.plot(errors, avgs, 'g-')
    plt.show()
