class User:

    user_list = []
    def __init__(self, first_name, last_name, personal_id,email):
        self.first_name = first_name
        self.last_name = last_name
        self.personal_id = personal_id
        self.email = email

    def save_user(self):
        User.user_list.append(self)