#Write a program to check how many times a character is repeated in a word?

character = input("Enter a the character to check the times it's reapeated: ")
word = "Welcome"
count = 0
for i in word:
    if i == character:
        count = count+1
print(count)