import unittest


class e2f(unittest.TestCase): 
    def test1(self): 
       
        #Example:
        self.assertEqual("Bonjour", "Bonjour") 

class e2f2(unittest.TestCase): 
    def test1(self): 
        self.assertEqual("merci", "merci") 



class f2e(unittest.TestCase): 
    def test1(self): 
       
        #Example:
        self.assertEqual("Hello", "Hello") 

class f2e2(unittest.TestCase): 
    def test1(self): 
        self.assertEqual("fast", "fast") 

if __name__ == '__main__':
    unittest.main()
