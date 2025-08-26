
#Make a function where the tuition will increase 3% every year for 5 years 
def tuition():
    print("Projeected tuition increase for the next 5 years")
#set values for the tution, rate, and the years
    tuition = 8000
    tuitionRate = 0.03
    years = 1

#make a for loop that loops 5 times and adds the new year and tuition and demicals for the prices. 
    for years in range (1, 6):
        tuition *= (1 + tuitionRate)
        print(f"Year {years}: ${tuition: .2f}")


tuition()