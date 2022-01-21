class User:
    def __init__(self):
        self.user_details = {}
        self.order_details = []
    
    def user_registration(self):
        print("Welcome To Hotel")
        user_name = input("Enter your name: ")
        user_ph = int(input("Enter the mobile number: "))
        user_email = input("Enter the email id: ")
        user_password = input("Enter the password: ")
        self.user_details = {"Name": user_name, "Mobile Number": user_ph, "E-Mail ID": user_email, "Password": user_password}
        print("User Account Successfully Created")
        for i in self.user_details:
            print(i, ":", self.user_details[i])
    
    

    def user_login(self):
        
        while True:
            print("Welcome to Hotel")
            email = input("Enter the e-mail ID: ")
            password = input("Enter the Password: ")
            if len(self.user_details)!=0:
                if email==self.user_details["E-Mail ID"]:
                    if password == self.user_details["Password"]:
                        print("Successfully Logged In!!!")
                        break
                    else:
                        print("Invalid Password")
                else:
                    print("Email ID is not registered")
            else:        
                reg = input(" User not Found!!\nDo you want to register: ")
                if reg.upper() in ["YES", "Y"]:
                    self.user_registration()
                elif reg.upper() in ["NO", "N"]:
                    print("Thank You")
                else:
                    print("Choose Valid Option")               
    
    

    def order_place(self):
        
        menu = ["1. Tandoori Chicken (4 pieces) [INR 240]", "2. Vegan Burger (1 Piece) [INR 320]", "3. Truffle Cake (500gm) [INR 900]"]
        print("Menu Food List")
        for i in menu:
            print(i)
        while True:
            print("\n1. Place the Order\n2. Previous Step ")
            order=input("\nEnter the Choice: ")
            if order=="1":
                print("Enter the Food number to be ordered separated by comma:")
                input_=input().split(",")
                for i in input_:
                    z=int(i)
                    if z<=len(menu):
                        self.order_details.append(menu[z-1])
                    else:
                        print("Sorry! Food Id ",z, " is not available")
                print("\nList of food item you selected :")
                for j in self.order_details:
                    print(j)
                print("Order Successfully Created\n")
                print("If you place more order SELECT 1 or to EXIT press 2")
            elif order=="2":
                break
            else:
                print("!! Invalid Number !!\n")
    
    

    def update_user_profile(self):
      
         while True:
            print("Select Below Options to Update Your Profile Details\n")
            print("1. Name\n2. Mobile number\n3. Email ID\n4. Password\n5. Previous Menu")
            x=input("Select the option to Edit(1 or 2 or 3 or 4 or 5): ")
            if x=="1":
                self.user_details["Name"]=input("Enter your updated full name : ")
                print("\n!! Detail Updated Successfully !!\n")
            elif x=="2":
                self.user_details["Mobile Number"]=int(input("Enter your updated 10 digit phone number : "))
                print("\n!! Detail Updated Successfully !!\n")      
            elif x=="3":
                self.user_details["E-Mail ID"]=input("Enter your updated email id : ")
                print("\n!! Detail Updated Successfully !!")
            elif x=="4":
                self.user_details["Password"]=input("Enter your updated password : ")
                print("\n!! Detail Updated Successfully !!\n")
            elif x=="5":
                break
            else:
                print("\n!! Invalid Number Entered !!\n")
                
            if x in ["1","2","3",'4',"5"]:
                for i in self.user_details:
                    print(i, ":",self.user_details[i])
            else:
                print("\nPlease Enter correct Input\n")

    
    def order_history(self):
        print("Previous Order:")
        for i in self.order_details:
            print(i)
    

    def user_functionalities(self):
        print("Welcome To Hotel")
        print("\n1. Register\n2. Login\n3. Close")
        a = int(input("Select the Option(1 or 2 or 3): "))
        if a==1:
            self.user_registration()
        elif a==2:
            self.user_login()
            while True:
                print("\nPlease select one of the option belew:\n")
                print("1. Place A New Order\n2. View Order History\n3. Update Profile\n4. Log Out\n5. Exit")
                b=int(input("Select the Option(1 or 2 or 3 or 4 or 5): "))
                if b==1:
                    self.order_place()
                elif b==2:
                    self.order_history()
                elif b==3:
                    self.update_user_profile()
                elif b==4:
                    self.user_login()
                elif b==5:
                    break
                else:
                    print("Choose Valid Option")
        else:
            print("Please, Select Valid Input")
        

        #IF USER WANTS TO CONTINUE
        yes_or_no = input("Do you want to continue(YES or Y / NO or N ): ")
        if yes_or_no.upper() in ["YES", "Y"]:
            self.user_functionalities()
        elif yes_or_no.upper() in ["NO", "N"]:
            print("Thank You")
        else:
            print("Enter Valid Case")