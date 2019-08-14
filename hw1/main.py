def main():
    print("What is your first name?")
    myFirstName = input()
    print("What is your last name?")
    myLastName = input()
    print("How old are you in months?")
    myAgeMonths = input()
    print("Your full name is " + myFirstName + " " + myLastName + ".")
    print( "You are " + str(int(myAgeMonths)//12) + " years old and " + str(int(myAgeMonths)%12) + " months old.")
if __name__ == "__main__":
    main()
