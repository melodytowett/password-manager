#!/usr/bin/env python3.9
from sys import platform
import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credentials("Facebook","Melody","melody@gmail.com","0786575342","Melo3903")


    def tearDown(self):
        Credentials.credential_list = []

    def test_init(self):
        self.assertEqual(self.new_credential.platform,"Facebook")
        self.assertEqual(self.new_credential.username,"Melody")
        self.assertEqual(self.new_credential.email,"melody@gmail.com")
        self.assertEqual(self.new_credential.phone_no,"0786575342")
        self.assertEqual(self.new_credential.password,"Melo3903")



    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_save_multiple_credentials(self):
        self.new_credential.save_credentials()
        mycredentials = Credentials("Whatsapp","Chepkorir","chepko@gmail.com","0712345678","M2345") 
        mycredentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)
    
    def test_delete_credentials(self):

        self.new_credential.save_credentials()
        mycredentials = Credentials("Whatsapp","Chepkorir","chepko@gmail.com","0712345678","M2345") 
        mycredentials.save_credentials
        mycredentials.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_firn_credentials_by_platform(self):
        self.new_credential.save_credentials()
        mycredentials = Credentials("Whatsapp","Chepkorir","chepko@gmail.com","0712345678","M2345") 
        mycredentials.save_credentials()
        whatsapp = Credentials.find_by_platform("Whatsapp")
        self.assertEqual(whatsapp.platform,mycredentials.platform)

        


