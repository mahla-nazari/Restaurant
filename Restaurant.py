#my Functions___________________________________________________________________
    
    
    def isalpha_isspace(n):
        p = 0
        for i in n:
            if ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('Z') or ord(i)==32:
                p+=1
        if p==len(n):
            return True
        return False
        


    def isnumber(n):
        p = 0
        for i in n:
            if ord('0')<=ord(i)<=ord('9'):
                p+=1
        if p==len(n):
            return True
        return False
        
    def check_phone_number(n):
        if isnumber(n)==True and len(n)==11 and n[0:3]=='021':
            
            return True
        return False





#Class_______________________________________________________________________________

class Restaurant:

    def __init__(self,name,tpy,menu,location,phone_number,working_hours\
                 ,capacity,delivery):

        self.name = name
        self.tpy = tpy
        self.menu = menu
        self.location = location   
        self.phone_number = phone_number             
        self.working_hours = working_hours                
        self.capacity = capacity                              
        self.delivery = delivery
        
        
    #validations______________________________________________________________________
        if isalpha_isspace(name):
            pass
        else:
            print("Enter valid name")
            
            
        
        if isalpha_isspace(tpy):
            pass
        else:
            print('Enter valid type')
            
        
        
        if type(menu)==dict:
            pass
        else:
            print("Enter valid menu")
            
            
            
        if isalpha_isspace(location):
            pass
        else:
            print('Enter valid location')
        
        
        
        
        if check_phone_number(phone_number):
            pass
        else:
            print('Enter valid phone number')
            
            
            
            
        if type(working_hours)==tuple and len(working_hours)==2:
            pass
        else:
            print("Enter the start of working hours and the end of working hours in the main tuple ")
            
        
        if type(capacity)==int:
            pass
        else:
            print("Enter valid capacity")
        
        
        if type(delivery)==bool:
            pass
        else:
            print("for the delivery ,Enter True or False")


            
            
 #the class functions_______________________________________________________________________________________________           
    def show_the_menu(self):
        for name in self.menu:
            print("{0:<10}  |  {1:>10}".format(name ,self.menu[name]['price']))
            

    def update_menu(self , food ,number):
        self.menu[food]['number'] = self.menu[food]['number']-number


    def billing(self , food , number):
        return self.menu[food]['price']*number

    def new_customer(self , number , time ,current_capacity):
        if self.working_hours[0]<time<self.working_hours[1]:
            if number>current_capacity:
                print("sorry.we do not have available table for you! ")
            else:
                print('welcome!')
        else:
            print("sorry.we are closed.")


    def take_order(self):
        self.show_the_menu()
        food = input("welcome.what do you want?: ")
        if food in self.menu:
            number = int(input('how many do you want?: '))
            if number>self.menu[food]['number']:
                print("sorry.we do not have enough of that.")
            else:
                self.update_menu(food, number)
                total =self.billing(food, number)
                print(f'your food is ready and total is {total}')
                print("Thank you for choosing us!")

        else:
            print(f"sorry.we do not serve {food} here!")