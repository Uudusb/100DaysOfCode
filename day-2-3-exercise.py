# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


YearsLeft = 90 - int(age)
MonthsLeft = YearsLeft * 12
WeeksLeft = YearsLeft * 52
DaysLeft = YearsLeft * 365

print(f"You have {DaysLeft} days, {WeeksLeft} weeks, and {MonthsLeft} months left.")
