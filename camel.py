def main():
     name = input()
     camel_to_snake(name)
     
#      new_name=''
     
#      for x in name:
#          if x==x.upper():
#              new_name+= '_'+x.lower()
             
#          else:
#              new_name+=x
        # print(new_name)
             



def camel_to_snake(camel):
    for char in camel:
        if char == camel[0]:
            continue
        if char.isupper():
            camel = camel.replace(char,f"_{char.lower()}")
    print(camel.lower())

main()




