
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...
    if len(s) > 6:
        #print("Invalid,,,,SD")
        return False


    elif not s.isalnum():
        #print("Invalid____yyu")
        return False


    else:
        alphas = ""
        numbers = ""
        if s[0:2].isalpha() and s[-1:].isdigit():
            for letter in s:
                if letter.isdigit():
                    numbers += letter

            if numbers[0]== "0":
                #print("Invalid......000")
                return
            else:
                #print("Valid")
                return True

        else:
            #print("Invalid.....UUUU")
            return False

        


main()