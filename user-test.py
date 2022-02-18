
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

if __name__ == '__main__':
    unittest.main()
    




