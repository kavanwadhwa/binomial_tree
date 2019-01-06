import math
import time

# s and k are defined in find_price.
# n is the current level/time step
# c is the label of the current node (root node = 0, its up child is 1 and down child is 2, etc.)
def binomial_pricing(s, k, n, c):

    su = s*u                                                    #calculate up price
    sd = s*d                                                    #calculate down price

    if(n==N):                                                   #base case (leaf node) n is current level
        dp[c] = max(0, k-s)                                     #store option price of node c
        return max(0, k-s)
    else:
        if(dp[n+1+c]<0):                                        #check if up child of node c has option price in array already
            fu = binomial_pricing(su, k, n + 1, n + 1 + c)      #if not, call recursive function
        else:
            fu = dp[n+1+c]                                      #else use value already computed
        if (dp[n+2+c]<0):                                       #check if down child of node c has option price in array already
            fd = binomial_pricing(sd, k, n + 1, n + 2 + c)      #if not, call recursive function
        else:
            fd = dp[n+2+c]                                      #else use value already computed
        dp[c] = max(k-s, math.exp(-r * dt) * (p * fu + (1 - p) * fd))   #update option price array
    return max(k-s, math.exp(-r * dt) * (p * fu + (1 - p) * fd), 0);


def find_price(linelist):
    global dp, u, d, p, dt, r, N                #define global values for "constants" so no need to pass as parameters
    for data in linelist:
        r = float(data[0])                      # risk free interest rate
        T = float(data[1])                      # time to expiration
        N = float(data[2])                      # number of time steps
        dt = T / N                              # delta t
        v = float(data[3])                      # volatility
        s = float(data[4])                      # starting stock price
        k = float(data[5])                      # strike price
        u = math.exp(v * math.sqrt(dt))         # u
        d = 1 / u                               # d
        p = (math.exp(r * dt) - d) / (u - d)    # probability of up movement
        m = int((N + 1) * (N + 2) / 2)          # total number of nodes in lattice

        dp = [-1]*m                             #array of option prices at each node (size m)

        t1 = time.time() * 1000
        print(binomial_pricing(s, k, 0, 0))
        runtime = time.time()*1000-t1