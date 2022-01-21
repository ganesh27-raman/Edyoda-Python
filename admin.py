class Admin: 
    def __init__(self):
        self.food ={}
        self.food_id = len(self.food)+1
    def food_item(self):
        self.food_name = input("Enter the Food Name: ")
        self.food_quantity = input("Enter the Quantity: ")
        self.food_price = float(input("Enter the Food Price: "))
        self.food_discount = int(input("Enter the Discount: "))
        self.food_stock = int(input("Enter the Stock availability: "))
        self.food_items={"Name":self.food_name, "Quantity":self.food_quantity, "Price":self.food_price, "Discount":self.food_discount, "Stock":self.food_stock}
        self.food_id = len(self.food)+1
        self.food[self.food_id] = self.food_items
        print("Food Item successfully Added",self.food)
    
    def food_edit(self):
        update_food_id = int(input("Enter the food id needs to be updated: "))
        update_food_attribute = input("Enter the attribute: ")
        new_value = input("Enter the value: ")

        self.food[update_food_id][update_food_attribute] = new_value
        
        print("Food is successfully updated. ", self.food)
        continue_edit = input("Edit more(Yes or Y / No or N): ")
        if continue_edit.upper() in ["Yes","Y"]:
            self.food_edit()
        elif continue_edit.upper() in ["NO","N"]:
            print("Thanks for Updating")
        else:
            print("Enter Valid input")
    
    
    def food_view(self):
        for i in self.food:
            print("Food id: ",i,'\n')
            for j in self.food[i]:
                print(j,":",self.food[i][j])
        

    def food_delete(self):
        del self.food[int(input("Enter the Food ID to be deleted: "))]
        print("Remaining food items: ",self.food)
    
    
    def admin_function(self):
        print("A. Add New Foods\nB. Edit the Food Item\nC. View the Food Item\nD. Delete the Food Item")
        prefernce = input("Enter the Function(A or B or C or D): ")
        if prefernce.upper()=="A":
            self.food_item()
        elif prefernce.upper()=="B":
            self.food_edit()
        elif prefernce.upper()=="C":
            self.food_view()
        elif prefernce.upper()=="D":
            self.food_delete()
        else:
            print("Enter the valid input")
            self.admin_function()
              
        
        #IF ADMIN WANTS TO CONTINUE:
        yes_or_no = input(("Do you want to continue (Select Yes or Y / No or N): "))
        if yes_or_no.upper() in ["YES","Y"]:
            self.admin_function()
        elif yes_or_no.upper() in ["NO","N"]:
            print("Thank you")
        else:
            print("Enter the valid option")