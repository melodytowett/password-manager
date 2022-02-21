import email
import pyperclip


class Credentials:
    credential_list = []

    def __init__(self,platform, username,email,phone_no,password):

        self.platform = platform
        self.username = username
        self.email = email
        self.phone_no = phone_no
        self.password = password 

    def save_credentials(self):
        Credentials.credential_list.append(self)

    
    def delete_credentials(self):
        '''
        Method to delete credentials
        '''
        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_platform(cls,platform):
        '''
        method to find credentials by platform
        '''
        for credentials in cls.credential_list:
            if credentials.platform == platform:
                return credentials

    @classmethod
    def credentials_exist(cls,platform):
        '''
        method to chek if contact exist
        '''
        for credentials in cls.credential_list:
            if credentials.platform == platform:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method to display credentiasz saved
        '''
        return cls.credential_list
    

    @classmethod
    def copy_password(cls,platform):
        credentials_found = Credentials.find_by_platform(platform)
        pyperclip.copy(credentials_found.password)
        password_copied = pyperclip.paste()
        print(password_copied)
