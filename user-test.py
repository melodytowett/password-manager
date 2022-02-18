#!/usr/bin/env python3.9
import unittest
from user import User

class TestUser(unittest.TestCase):#helps in creating test cases

    def setUp(self):
        self.new_user = User("Melody","Chepkorir","01234","melochep@gmail.com")

#initializing object properly
    def test_init(self):
        self.assertEqual(self.new_user.first_name,"Melody")
        self.assertEqual(self.new_user.last_name,"Chepkorir")
        self.assertEqual(self.new_user.email,"melochep@gmail.com")
        self.assertEqual(self.new_user.personal_id,"01234")


# Save the user 
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
# teardown executes a set of instructions after every test
    def tearDown(self):
        User.user_list = []

#saving multiple users
    def test_save_multiple_user(self):
        self.new_user.save_user()
        second_user = User("Chep","Towett","towettchep@gmail.com","14567")
        second_user.save_user()
        self.assertEqual(len(User.user_list),2)
# delete Account
    def test_delete_user(self):
        self.new_user.save_user()
        second_user = User("Chep","Towett","towettchep@gmail.com","14567")
        second_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()
    




