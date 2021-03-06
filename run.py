#!/usr/bin/env python3.9
#from tabnanny import check
from re import search
import string
import random
from sys import platform
from user import User
from credentials import Credentials
def create_account(fname,lname,pid,email): 
    """funtion to create user account"""
    new_user = User(fname,lname,pid,email)
    return new_user

def save_account(user):
   return User.save_user(user)

def delete_account(user):
    """function to delete user account"""
    user.delete_user()

def add_credential(platform,u_name,e_address,password,p_number):
    """funtion to create credential"""
    new_credential = Credentials(platform,u_name,e_address,p_number,password)
    return new_credential

def save_credential(credential):
    return Credentials.save_credentials(credential)

def del_credential(credential):
    """funtion to delete credential"""
    return Credentials.delete_credentials(credential)

def find_credential(platform):
    """Function to find save credentials by platfrom name"""
    return Credentials.find_by_platform(platform)

def check_existing_credential(platform):
    """Function to chek if credentials exist"""
    return Credentials.credentials_exist(platform)

def display_credential():
    """funtion to display  all credentials"""
    return Credentials.display_credentials()

def copy_this(platform):
    return Credentials.copy_password(platform)



def main():
    print("Hello welcome to password manager.what is your name?")
    user_name = input()
    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("use these short codes : ca - creat your account, dc- delete account ")
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
            print(f"Your Password Locekr Account {f_name} {l_name} has been created")
            print('\n')

            while True:
                print("""USE THESE SHORT CODES TO ADD CREDENTIALS:
                  ip-input platform,
                  del-c -delete credentials,
                  fc-find credentials, 
                  dsc-display credentials,
                  gp-generate platform random passwor 
                  cp-copy password """)
                short_code = input().lower()

                if short_code == 'ip':
                    print("Save a platform")
                    platform = input()

                    print("username....")
                    u_name = input()

                    print("Email")
                    e_address = input()

                    print("p_number")
                    p_number = input()

                    print("password")
                    password = input() 


                    save_credential(add_credential(platform,u_name,e_address,password,p_number))
                    print('/n')
                    print(f"{platform} credential has been created")
                    print('/n')

                    
                elif short_code ==  'dsc':
                    if display_credential():
                        print("Heres the list of all your ceredntials")
                        print('/n')
                       
                        for credentials in display_credential():
                            print(f"{credentials.platform}----{credentials.username}....{credentials.email}...{credentials.phone_no}")
                            print('/n')

                        else:
                            
                            print("Nothing to display")
                          
                elif short_code == "fc":
                    print("Enter the platform you wan to find")
                    search_credential = input()
                    if check_existing_credential(search_credential):
                        search_platform = find_credential(search_credential)
                        print(f"{search_platform.platform} {search_platform.username} {search_platform.phone_no} {search_platform.email}")
                        print('-'*20)
                        print(f"Your accounts are: {search_platform.platform}")
                    else:
                        print("Credential not found")

                elif short_code == 'del-c':
                    print("Which platform credential do you want to delete\n")
                    delete_platform = input()
                    if check_existing_credential(delete_platform):
                        credential = find_credential(delete_platform)
                        del_credential(credential)
                        print("credentials deleted")
                    else:
                        print("can't find credential to delete")

                
                elif short_code == 'gp':
                    print("what platform would you want to geneate password for? >")
                    platform = input()
                    S = 8
                    rand = ''.join(random.choices(string.ascii_letters + string.digits,k = S))
                    print("Your  generated password is:" +str(rand))

                elif short_code == 'cp':
                  print("Enter platform you want its password copied")
                  my_password = input()
                  if check_existing_credential(my_password):
                     credentials = find_credential(my_password)
                     credentials.copy_password(my_password)
                     print("password copied")
                  else:
                      print("nothing copied")
           

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
