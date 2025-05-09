amount_due=50
insert_coin = 0

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))
        
    
    if amount_due > 0:
        if insert_coin != int(25) and insert_coin !=int(10) and insert_coin !=int(5):
            continue
        else:
            amount_due -= insert_coin
         
else:
    print(f"Change Owed: {(-1)*amount_due}")

        
       

            
            
        
#     valid_coins=['25','10','5']

#     if str(amount_paid) in valid_coins:
#         amount_due-=amount_paid
#         change+=amount_paid

        
#     if amount_due<=0:
#         break
    
# if change>50:
#     change=change-50
# else:
#     change=0
        
#print(f"change owed: {amount_due}")
        

