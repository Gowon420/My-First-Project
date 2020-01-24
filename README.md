# My-First-Project
I love Programming a lot
I want to become a software developer



# A program that reverse a text

message = input('Enter Message: ')
translated = ''
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    
    i = i - 1
print(translated)
