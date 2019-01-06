import math
import time


# s and k are defined in find_price.
# n is the current level/time step
# sum is the cumulative sum of the path being evaluated
def binomial_pricing(s, k, n, sum):

    su = s * u  # calculate up price
    sd = s * d  # calculate down price

    if (n == N):  # base case (leaf node) n is current level
        return max(0, (sum/(n+1))-k)
    else:
        fu = binomial_pricing(su, k, n + 1, sum + su)
        fd = binomial_pricing(sd, k, n + 1, sum + sd)
    return max(math.exp(-r * dt) * (p * fu + (1 - p) * fd), 0);

def find_price(linelist):
    global dp, u, d, p, dt, r, N        #define global values for "constants" so no need to pass as parameters
    for data in linelist:
        r = float(data[0])              #risk free interest rate
        T = float(data[1])              #time to expiration
        N = float(data[2])              #number of time steps
        dt = T/N                        #delta t
        v = float(data[3])              #volatility
        s = float(data[4])              #starting stock price
        k = float(data[5])              #strike price
        u = math.exp(v*math.sqrt(dt))   #u
        d = 1/u                         #d
        p =(math.exp(r*dt)-d)/(u-d)     #probability of up movement

        t1 = time.time()*1000
        print(binomial_pricing(s, k, 0, s))
        runtime = time.time()*1000-t1
