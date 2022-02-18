#!/usr/bin/env python3.9
from tabnanny import check
from user import User
def create_account(fname,lname,pid,email): 
    new_user = User(fname,lname,pid,email)
    return new_user

def save_account(user):
   return User.save_user(user)

def delete_account(user):
    user.delete_user()




def main():
    print("Hello welcome to password manager.what is your name?")
    user_name = input()
    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("use these short codes : ca - creat you account, dc- delete account")
        short_code = input().lower()
        if short_code == 'ca':
            print("Create account")
            print("_"*10)

            print("First Name.....")
            f_name = input()

            print("Last Name....")
            l_name = input()

            print("Personal ID...")
            p_id = input()

            print("Email....")
            e_mail = input()

            save_account(create_account(f_name,l_name,p_id,e_mail))
            print('\n')
            print(f"Your Account {f_name} {l_name} has been created")
            print('\n')
           

        elif short_code == 'dc':
              print("Enter your personal id to delete the account")
              deleted_user = input()
              if save_account(deleted_user):
                    user = create_account(deleted_user)
                    delete_account(user)
                    print("Accont deleted")
              else:
                    print("Dont have an account")
                    



        else:
            print("short code not available")
if __name__ == '__main__':
    main()
