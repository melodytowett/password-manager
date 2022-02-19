class Credentials:
    credential_list = []

    def __init__(self,platform, username,email,phone_no):

        self.platform = platform
        self.username = username
        self.email = email
        self.phone_no = phone_no 

    def save_credentials(self):
        Credentials.credential_list.append(self)

    
    def delete_credentials(self):
        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_platform(cls,platform):
        for credentials in cls.credential_list:
            if credentials.platform == platform:
                return credentials

    @classmethod
    def credentials_exist(cls,platform):
        for credentials in cls.credential_list:
            if credentials.platform == platform:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        return cls.credential_list