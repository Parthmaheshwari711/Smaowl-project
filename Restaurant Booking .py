spr=1000
print("Hello praani, welcome to Promato")
print("Promato will provide you info about the best restaurants in your area")
print("1.North Delhi")
print("2.South Delhi")
print("3.Noida Sector 14A")
ch=int(input("Choose your location"))
if(ch==1):
    restype=input("Enter Restaurant Type(Indian/Italian/Continental)")
    nopeople=int(input("Enter The Number Of Foodies"))
    for i in range (1,nopeople+1):
        print("Enter Name Of Foodie",i)
        name=input()
        print("Enter Age Of Foodie",i)
        age=input()
    if(restype=="Indian" or restype=="indian"):
        price=nopeople*spr
        print("The Best Indian restaurant there is Soda Botttleopenerwala with a rating of 4.5 and its open from 8am-12midnight")
        print("You can go by car to reach their quickly")
        print("price",price)
    elif(restype=="Italian" or restype=="italian"):
        price=nopeople*2000
        print("The best Italian restaurant there is Cafeteria and Co with an avg rating of 4.5 out of 5 by 5000 customers and it is open from 10am-midnight")
        print("The quickest way to reach there is by metro as there is a lot of traffic on the road")
        print("Your total price at Cafeteria and Co is",price)
        print("Advice-As per promato experts the pasta there is excellent")
    elif(restype=="Continental" or restype=="contintental"):
        print("The best Continental restaurant there is Ricos with an avg rating of 4.6 stars and it is open from 10am-11:59pm")
        price=nopeople*1500
        print("You can either take a taxi or go my metro to reach there")
        print("Your price for Ricos is",price)
        print("Thank you for using Promato")
        print("Designed by Parth Maheshwari aka the greatest coder ever")
        print("Till next time keep eating")
elif(ch==2):
    restype=input("Enter Restaurant Type(Indian/Italian/Continental)")
    nopeople=int(input("Enter The Number Of Foodies"))
    for i in range (1,nopeople+1):
        print("Enter Name Of Foodie",i)
        name=input()
        print("Enter Age Of Foodie",i)
        age=input()
    if(restype=="Indian" or restype=="indian"):
        price=nopeople*spr
        print("The best Indian restaurant there is JUGGERNAUT with a 4.5 star rating and it is open from 9am-11pm")
        print("The best way to reach there is by car as you would reach in about 10-15 min")
        print("your total price for JUGGERNAUT is",price)
        print("Thank you for using Promato")
        print("Designed by Parth Maheshwari aka the greatest coder ever")
        print("Till next time keep eating")
    elif(restype=="Italian" or restype=="italian"):
        price=nopeople*2750
        print("The best Italian restaurant there is Spago with a rating of 4.3 stars and its open from 9am-midnight")
        print("The quickest way to reach there is car or taxi as parking is not always available")
        print("Your total price is",price)
        print("Dhanayavad")
    elif(restype=="Continental" or restype=="continental"):
        price=nopeople*2.5*spr
        print("The best continental restaurant there is Olive Bar And Kitchen with a rating of 4.5 stars and it is open from 8am-!2 midnight")
        print("Your total price is",price)
        print("Merci")
elif(ch==3):
    restype=input("Enter Restaurant Type(Indian/Italian/Continental)")
    nopeople=int(input("Enter The Number Of Foodies"))
    for i in range (1,nopeople+1):
        print("Enter Name Of Foodie",i)
        name=input()
        print("Enter Age Of Foodie",i)
        age=input()
    if(restype=="Indian" or restype=="indian"):
        price=nopeople*900
        print("The best Indian restaurant there is Punjab grill with a rating of 4 out of 5 and it is open from 12noon-11pm")
        print("Suggestion- Food is not that good but there is no better option")
        print("You can go there by car and it will take you 10 min to reach")
        print("Your total price is",price)
        print("Thank you")
    elif(restype=="Italian" or restype=="italian"):
        price=nopeople*1250
        print("The best italian restaurant there is KA Eclairs and Cafe with a rating of 4.4 stars open from 10:30am-11:30pm")
        print("Use the local metro to reach there quickly")
        print("Your expense is",price)
        print("Thank you for using Promato")
        print("Designed by Parth Maheshwari aka the greatest coder ever")
        print("Till next time keep eating")
    elif(restype=="Continental" or restype=="continental"):
        price=nopeople*spr
        print("The best continental restaurant there is Cafe delhi heights with a 4.2 star rating and it is also in an excellent location and is open from 11am-11pm")
        print("You can reach there by either car or metro")
        print("Your MRP is",price)
        print("Thank you for using Promato")
        print("Designed by Parth Maheshwari aka the greatest coder ever")
        print("Till next time keep eating")
        
        
        
    
        
        
        

        
        
        
        
        


       
