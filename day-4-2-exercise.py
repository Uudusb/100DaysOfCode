# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

numberOfNames = len(names)
index = random.randint(0, numberOfNames - 1)

print(f"{names[index]} is goind to buy the meal today!" )
