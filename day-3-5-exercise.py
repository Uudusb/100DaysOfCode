# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t_count = lower_name1.count("t") + lower_name2.count("t")
r_count = lower_name1.count("r") + lower_name2.count("r")
u_count = lower_name1.count("u") + lower_name2.count("u")
e_count = lower_name1.count("e") + lower_name2.count("e")
l_count = lower_name1.count("l") + lower_name2.count("l")
o_count = lower_name1.count("o") + lower_name2.count("o")
v_count = lower_name1.count("v") + lower_name2.count("v")

trueTotal = t_count + r_count + u_count + e_count
loveTotal = l_count + o_count + v_count + e_count
print(f"T occurs in {t_count} times")
print(f"R occurs in {r_count} times")
print(f"U occurs in {u_count} times")
print(f"E occurs in {e_count} times")
print(f"Total = {trueTotal}")
print(f"L occurs in {l_count} times")
print(f"O occurs in {o_count} times")
print(f"V occurs in {v_count} times")
print(f"E occurs in {e_count} times")
print(f"Total = {loveTotal}")

loveScore = str(trueTotal) + str(loveTotal)

print(f"Love Store = {loveScore}")

loveScoreInt = int(loveScore)

if loveScoreInt < 10 or loveScoreInt > 90:
  print(f"Your love score is {loveScoreInt}, you go together like coke and mentos.")
elif loveScoreInt > 40 and loveScoreInt < 50:
  print(f"Your love score is {loveScoreInt}, you are alright together.")
else:
  print(f"Your love score is {loveScoreInt}.")
