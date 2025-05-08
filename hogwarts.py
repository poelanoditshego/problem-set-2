students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# Improve the code:
# for student in students:
#     print(student)
    
# for i in range(len(students)):
#     print(i + 1, students[i])

# DICTIONARIES
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# WE CAN IMPROVE THIS DICTIONARY

# How we can only print Keys of dictionary
# for student in students:
#     print(student)
    
# How we can print both keys and values:
# for student in students:
#     # print(student, students[student])
#     print(student, students[student], sep = ", ") # Print a cleaner code

# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None}
# ]

# for student in students:
#     print(student["name"], student["house"],student["patronus"], sep = "....")


# MARIO GAME
# Print the columns
# def main():
#     height = input("Enter a number: ")
#     print_column(int(height))
    
    
# def print_column(height):
#     for _ in range(height):
#         print("#")
        
# main()

# Print the Rows
# def main():
#     print_row(4)
    
    
# def print_row(width):
#     print("?"*width)

# main()

# How we can implement both functions

# def main():
#     print_square(3)
    
# def print_square(size):
#     # For each row in square
#     for i in range(size):
        
#         # For each brick in row
#         for j in range(size):
            
#             # Print brick
#             print("#", end ="")
#         print()
    
# main()

def main():
    print_square(3)
    
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#"*width)
    
main()