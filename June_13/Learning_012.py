# While
i = 0
while i < 5:
    print(i)
    i = i + 1
# write a program that calculates and displays the letter
# given numerical score
# A = 90-100, B = 80-89, C = 70-79, D = 60-69, F = 0-59

score = int(input("Enter your score: "))
if score >= 90 and score <= 100:
    print("A grade")
elif score >= 80 and score <= 89:
    print("B grade")
elif score >= 70 and score <= 79:
    print("C grade")
elif score >= 60 and score <= 69:
    print("D grade")
elif score >= 0 and score <= 59:
    print("F grade")
else:
    print("Invalid score")
