def main():
    print("What is your first name?")
    myFirstName = input()
    print("What is your last name?")
    myLastName = input()
    print("How old are you in months?")
    myAgeMonths = input()
    print("What is your favorite color?")
    myColor = input()
    print("Where were you born?")
    myBirthPlace = input()
    print("How many people are in your family?")
    myFamily = input()
    print("What is the brand of your favorite bubbly water?")
    myWater = input()

    print( "Your full name is " + myFirstName + " " + myLastName + ". " + "You are " + str(int(myAgeMonths)//12) + " years and " + str(int(myAgeMonths)%12) + " months old.")
    print( "Your favorite color is " + myColor + ".")
    print( "You were born in " + myBirthPlace + " and you have " + myFamily + " people in your family.")
    print( "Oh and your favorite bubbly water is that tsp tsp tsp ahhhh " + myWater + "!")
if __name__ == "__main__":
    main()
