#
# LimeadeStand
# Based on the old DOS Lemonade Stand game :)
# Elara Willett
# March 2016
#

from time import sleep
import random

#constants - change these to balance game
oneLimePrice = 1
tenAgavePrice = 5
hundredCupPrice = 2

#game play values
numLimes = 0 
numAgaves = 0
numCups = 0
readyLimeade = 0
money = 10.0
weather = 0
salesPrice = 0
day = 1

#function to query user for how much of an ingredient to buy
#returns a quantity (that is nonnegative int and affordable)
def queryUserBasedOn(price) :
    try :
        qtyInput = int(raw_input("How many would you like? "))
        if qtyInput < 0 :
            print("Opps, try again!")
            return queryUserBasedOn(price)
        elif qtyInput*price > money :
            print("You cannot afford that many. Try again.")
            return queryUserBasedOn(price)
        else :
            return qtyInput
    except ValueError:
        print("Opps, try again!")
        return queryUserBasedOn(price)
    
#function to query user for how much lime-ade to make
#updates global variables and returns nothing
def makeLimeade() :
    global numLimes
    global numAgaves
    global readyLimeade
    try :
        numPitchers = int(raw_input("How many pitchers of lime-ade will you prepare for today's customers? "))
        if(numPitchers < 0) :
            print("Opps, try again!")
            makeLimeade()
        elif numPitchers > numLimes :
            print("You don't have enough limes. Try again.")
            makeLimeade()
        elif numPitchers > numAgaves : 
            print("You don't have enough agave. Try again.")
            makeLimeade()
        else :
            readyLimeade = 10*numPitchers
            numLimes -= numPitchers
            numAgaves -= numPitchers
    except ValueError :
        print("Opps, try again!")
        makeLimeade()

#function to query user for how much to charge per cup
#updates global variable and returns nothing
def determineSalesPrice() :
    global salesPrice
    try :
        inputPrice = int(raw_input("How many CENTS will you charge per cup of lime-ade today? "))
        if(inputPrice < 0) :
            print("Opps, try again!")
            determineSalesPrice()
        else :
            salesPrice = inputPrice
    except ValueError :
        print("Opps, try again!")
        determineSalesPrice()
 
#function to calculate and display the sales of lime-ade during a given time period
#updates global variables and returns the amount of lime-ade sold
def sellLimeade(hours) :
    global weather
    global numCups
    global readyLimeade
    
    print("Between " + hours + " the weather is...")
    sleep(1)
    if random.randint(0,2)!=0 :
        weather = random.randint(1,7)
    
    if weather == 1 :
        print(" | | | | ")
        print("| | | | |     A hurricane! Oh no!!!!!")
        print(" | | | | ")
    elif weather == 2 or weather == 3  :
        print("~ ~ ~ ~ ~ ")
        print(" ~ ~ ~ ~      A little windy! Bummer!")
        print("~ ~ ~ ~ ~ ")
    elif weather == 4 or weather == 5 :
        print("  \\   / ")
        print("    o         Clear and sunny! Wonderful!")
        print("  /   \\")
    else :
        print("  \\ | / ")
        print(" -- o --      Very very hot!!!! GREAT for business!")
        print("  / | \\  ")
    sleep(1)
    
    if salesPrice >= 500 :
        customers = 0
    else :
        customers = 25*weather*26/(salesPrice+1)
    limeadeSold = min(customers, numCups, readyLimeade)
    if customers == limeadeSold :
        print("Yay! "+ str(customers) + " customers wanted to buy your lime-ade and you sold a cup to all of them!\n")
    else :
        print("Hmmm...."+ str(customers) + " customers wanted to buy your lime-ade, but you only had " + str(limeadeSold) + " cups available to sell.\n")
    sleep(2)
 
    numCups -= limeadeSold 
    readyLimeade -= limeadeSold 
    return limeadeSold

#function that determines if the user can obviously make no more money
def timeToQuit() :
    if money > 0 :
        return False
    if (numLimes >0 and numAgaves>0 and numCups>0) :
        return False
    return True


#
#
#GAME STARTUP
#
#
print("\nIt is time you start making some money around here... ")
sleep(1)
print("    __                     __")
print(" __|__|___________________|__|__ ")
print("|                               |")
print("|                               |")
print("|    L  I  M  E  -  A  D  E     |     Let's see how much money you")
print("|                               |         can make in one week!")
print("|_______________________________|")
print("   |  |                   |  |    ")
print("   |  |                   |  |        INGREDIENT PRICES:")
print("   |  |                   |  |        water = free!")
print("  _|  |___________________|  |_       10oz bottle of agave = $" + str(tenAgavePrice))
print(" / |__|                   |__| \\      1 organic lime = $" + str(oneLimePrice))
print("/_______________________________\\     100 cups = $" + str(hundredCupPrice))
print("|                               |")
print("|                               |     LIME-ADE RECIPE:")
print("| D  E  E - L  I  C  I  O  U  S |     - 1oz of agave")
print("|                               |     - one lime")
print("|                               |     - nine cups water")
print("|_______________________________|     Makes one pitcher (10 cups).")

#
#
#DAILY LOOP
#
#
while day in range(8) and not timeToQuit() :
    print("\nDAY " + str(day) + ": You have $" + "%.2f"%money + ", " + str(numLimes) + " limes, " + str(numAgaves)
          + "oz agave, and " + str(numCups) + " cups.")
    
    #purchase limes
    print("Limes are $" + str(oneLimePrice) + " each."),
    qty= queryUserBasedOn(oneLimePrice)
    money = money - qty*oneLimePrice
    numLimes += qty
    print("-->Now you have "+ str(numLimes) + " limes and $" + "%.2f"%money + ".")
    
    #purchase agave
    print("Ten ounce bottles of agave are $" + str(tenAgavePrice) + " each."),
    qty = queryUserBasedOn(tenAgavePrice)
    money -= qty*tenAgavePrice
    numAgaves += 10*qty
    print("-->Now you have "+ str(numAgaves) + " oz agave and $" + "%.2f"%money + ".")
    
    #purchase cups
    print("Packages of 100 cups are $" + str(hundredCupPrice) + " each."),
    qty = queryUserBasedOn(hundredCupPrice)
    money -= qty*hundredCupPrice
    numCups += 100*qty
    print("-->Now you have "+ str(numCups) + " cups and $" + "%.2f"%money + ".")
    
    makeLimeade()
    determineSalesPrice()
    print("-----------------------")
    
    limeadeSold = sellLimeade("ten and noon")
    limeadeSold += sellLimeade("noon and two")
    limeadeSold += sellLimeade("two and four")
    limeadeSold += sellLimeade("four and six")
    
    revenue = limeadeSold*salesPrice/100.0
    money += revenue
    print("You sold a total of " +str(limeadeSold) + " cups of lime-ade today for $" + str(revenue) + ". Now you have $" + "%.2f"%money + "!")

    rots = random.randint(0,numLimes)
    numLimes -= rots
    print("At the end of the day, you had to drink "+ str(readyLimeade)+ " extra cups of lime-ade")
    print("and " + str(rots) + " of your extra limes went bad.")
    
    day += 1
    print("---------------------------------------------------------------------")
    sleep(2)

#
#
# GAME END
#
#
if timeToQuit() :
    print("Looks like it's time to quit.")
else :
    print("Congratulations, you made it through the week and completed the game!")
if money < 200 :
    print("You score 1 star. Maybe try again.")
elif money < 400 :
    print("You score 2 stars. That's ok.")
elif money < 600 :
    print("You score 2 starts. Not too bad!")
elif money < 800 :
    print("You score 4 stars. Nice!!")
else :
    print("You score 5 stars! Great!!!")