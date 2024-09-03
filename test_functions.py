#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:15:29 2024

@author: raminpahnabi
"""
# #Test
import unittest
import os

class TestFunctions(unittest.TestCase):
    
    def setUp(self):
        home = os.path.dirname(os.path.abspath(__file__))
        # Path to the data file inside the submodule
        self.data_file_path = home + '/data.txt'
        self.InputData()
        
    def InputData(self):
        # self.results_a = 5
        # self.results_b = 10
        # self.expected_results_c = 15
        # with open('data.txt', 'r') as file:
        with open(self.data_file_path, 'r') as file:
            data = file.readlines()
            self.results_a = int(data[0].strip())
            self.results_b = int(data[1].strip())
            self.expected_results_c = int(data[2].strip())

           
    def Function_a(self):
        return self.results_a

    def Function_b(self):
        return self.results_b

    def Function_c(self, a, b):
        return a + b

    def test_Function_a(self):
        print("Test 1")
        self.assertEqual(self.Function_a(), self.results_a, f"Function_a failed for this student")

    def test_Function_b(self):
        self.assertEqual(self.Function_b(), self.results_b, f"Function_b failed for this student")

    def test_Function_c(self):
        a = self.Function_a()
        b = self.Function_b()
        val = self.Function_c(a, b) == self.expected_results_c
        self.assertTrue(val,f"Function_c failed for this student")
        # self.assertEqual(self.Function_c(a, b), self.expected_results_c, f"Function_c failed for this student")

if __name__ == '__main__':
    unittest.main()

# import unittest
# import os

# class TestFunctions(unittest.TestCase):

#     def setUp(self):
#         self.InputData()

#     def InputData(self):
#         # Assuming 'private-repo' is the name of your submodule directory
#         data_file_path = os.path.join('private-repo', 'data.txt')
#         with open(data_file_path, 'r') as file:
#             data = file.readlines()
#             self.results_a = int(data[0].strip())
#             self.results_b = int(data[1].strip())
#             self.expected_results_c = int(data[2].strip())

#     def Function_a(self):
#         return self.results_a

#     def Function_b(self):
#         return self.results_b

#     def Function_c(self, a, b):
#         return a + b

#     def test_Function_a(self):
#         self.assertEqual(self.Function_a(), self.results_a, f"Function_a failed for this student")

#     def test_Function_b(self):
#         self.assertEqual(self.Function_b(), self.results_b, f"Function_b failed for this student")

#     def test_Function_c(self):
#         a = self.Function_a()
#         b = self.Function_b()
#         val = self.Function_c(a, b) == self.expected_results_c
#         self.assertTrue(val, f"Function_c failed for this student")

# if __name__ == '__main__':
#     unittest.main()
