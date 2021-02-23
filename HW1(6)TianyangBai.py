# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:25:37 2021

@author: hulkb
"""


print("Question 6: part 1")

import pandas as pd
ReadExcel = pd.read_excel(r'C:\Users\hulkb\Desktop\Academic\PythonP\HW1\Sample1.xlsx')

print(ReadExcel)

df1 = pd.DataFrame(ReadExcel, columns = ['Account_Bal', 'Prop_01', 'Prop_03', 'Prop_05'])
print(df1.describe())
print(df1.sum())

print("")
print("Question 6: part 2")

class customer:
    num_customer = 0
    def __init__(self, name, customer_id, zip_address, ssn):
        self.name = name
        self.customer_id = customer_id
        self.zip_address = zip_address
        self.ssn = ssn
        customer.num_customer += 1
        
    def customerout(self):
        num_customer -= 1
    

    def Account_Bal(self, money):
        self.money = money
    def get_Bal(self):
        print(self.money)
    def customer_rate(self, rate1, rate2):
        self.rate1 = rate1
        self.rate2 = rate2
    def get_customer_rate(self):
        print('customer {} rating is {}, {} '. format(self.name, self.rate1, self.rate2))
    def customer_grade(self, grade1, grade2, grade3, grade4):
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade4 = grade4
    def get_customer_grade(self):
        print('customer grades are {}, {}, {}, {}'.format(self.grade1, self.grade2, 
                                                          self.grade3, self.grade4))


print("")
print("Testing our class functions: ")
customer1 = customer('Sun', 10634, 30895, 45820794)
print(customer1.name) # should get 'Sun'
customer1.Account_Bal(387.99)
customer1.get_Bal() # should get '387.99'
customer1.customer_rate('C', 'B')
customer1.get_customer_rate() # should get 'customer Sun rating is C, B'
customer1.customer_grade(30, 0.39, 89, 74)
customer1.get_customer_grade() # should get 'customer grades are 30, 0.39, 89, 74'
print("")
print("Testing Over")

