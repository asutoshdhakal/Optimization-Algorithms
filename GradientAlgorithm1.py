import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def main():
    start_program()
    plt.show()

def graph_function(x):
    xOriginal = np.linspace(0,1,100)
    y = (6*xOriginal - 2)*(6*xOriginal - 2)* np.sin(12*xOriginal - 4) 
    plt.plot(xOriginal,y, x, (6*x - 2)*(6*x - 2)* np.sin(12*x - 4), 'ro') 

def start_program():
    
    for i in range(1, 31):
        np.random.seed(i)
        gradient_ascent(np.random.rand())
        
def gradient_ascent(randNum):
    
    alpha = pow(10, -4)
    x = randNum
    boolean = True

    while boolean:
        derivative = (24*(3*x - 1)* (np.sin(12*x - 4) + (6*x - 2)* np.cos(12*x - 4)))
        change = alpha*derivative
        x = x - change 
        if(derivative < pow(10, -3) and derivative > - pow(10, -3)):
            boolean = False
    graph_function(x)
    
    
main()