def mutate_string(string, position, character):
    # Convert string to list, since strings are immutable in Python
    string_list = list(string)

    # Replace the character at the specified position with the new character
    string_list[position] = character

    # Join the list back into a string and return the modified string
    return ''.join(string_list)


# Prompt user for input
string = input("Enter a string: ")
position, character = input("Enter a position and character separated by a space: ").split()
position = int(position)

# Call the mutate_string function and print the result
new_string = mutate_string(string, position, character)
print("Result:", new_string)

# and there's the results ==>
#C:\Users\Ragner\AppData\Local\Microsoft\WindowsApps\python3.11.exe "C:\Users\Ragner\Desktop\.vscode\project 1.py" 
#Enter a string: abracadabra
#Enter a position and character separated by a space: 5 k
#Result: abrackdabra

#Process finished with exit code 0
