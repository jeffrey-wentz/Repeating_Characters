# this program takes a string from the letter and tells them the first repeating character
user_string = input("Please enter your string: ")
empty_list = []
for char in user_string:
    if char in empty_list:
        print(char)
        break
    else:
        empty_list.append(char)
