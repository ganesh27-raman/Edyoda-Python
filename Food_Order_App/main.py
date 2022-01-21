import admin
import user
class Restraunt:
    def __init__(self):
       pass

    
def main():
    print("1. Admin Panel\n2. User Panel")
    choice = int(input("Enter the Choice(1 or 2): "))
    if choice==1:
        admin_panel= admin.Admin()
        admin_panel.admin_function()
        
    elif choice==2:
        user_panel = user.User()
        user_panel.user_functionalities()
    else:
        print("Enter the valid choice")


if __name__=="__main__":
    main()