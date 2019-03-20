# This program returns the first recurring character and it's index in a string submitted by the user.


# loops through the program until user terminates program
while True:
    user_string = input("Please enter your string: ")
    user_list = []
    flag = 0
    
    # iterates through each character of the user's string. if the char is in the user list then we have
    # have found our recurring char. Prints that character and for the bonus it also prints the initial
    # index of recurring character. If the character is not in the user list then it gets added.
    for char in user_string:
        if char in user_list:
            print("\n######################################")
            print("# First recurring character: " + char)
            print("# Index where original char found: " + str(empty_list.index(char)))
            print("######################################")
            flag = 1
            break
        else:
            empty_list.append(char)
    
    # if our flag did not get set by finding a recurring character print this message.
    if flag == 0:
        print("\n######################################")
        print("# No recurring characters found!")
        print("######################################")

    cont = input("\nWould you like to continue?: ")
    if cont in ("no", "n", "nah", "0"):
        break
