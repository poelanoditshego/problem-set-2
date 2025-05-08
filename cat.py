# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# for _ in range(3):
#     print("meow")

# print("meow\n"*2,"poelano\n"*2, end = "\n")

# Improving with user input:
# while True:
#     n = int(input("what is n? "))
#     if n < 0:
#         print('Enter a valid number!!')
#         continue
#     else:
#         break

    
# Improve the code.
# while True:
#     n = int(input("What is n? "))
#     if n > 0:
#         print(n)
#         break
    
# for _ in range(n):
#     print("meow")
    
    
# Using function to improve code.
def main():
    n = get_number()
    meow(n)
    pass

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow")
        
        
main()
    
    