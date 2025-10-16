def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

name = input("Enter the student's name: ")

g1 = float(input("Enter grade 1: "))
g2 = float(input("Enter grade 2: "))
g3 = float(input("Enter grade 3: "))
g4 = float(input("Enter grade 4: "))
g5 = float(input("Enter grade 5: "))

grades = [g1, g2, g3, g4, g5]

average = sum(grades) / 5

letter = get_letter_grade(average)

print(name)
print("Average:", round(average, 1))
print("Letter Grade:", letter)
