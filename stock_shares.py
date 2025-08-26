
#Make a function of the stock with a greeting and set the values and input of the target and cost 
def stock():
    print("Please enter a number of your target and cost")
    target = float(input(("Target: ")))
    cost = float(input(("Cost: ")))

#make a while condition where if the target is greater than the cost, print sell
    while cost < target:
        cost = float(input())

    print ("SELL THIS NOW") 

stock()