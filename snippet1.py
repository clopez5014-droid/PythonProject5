db = open("output.txt", "a")

a = "Hello"
b = "How do you do?"

db.write(a + ", " + b + "\n")
db.close()

