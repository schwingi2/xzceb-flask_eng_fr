import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(''), '400')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class Testfrench_to_english(unittest.TestCase): 
    def test3(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello' ) 
        self.assertEqual(french_to_english(''), '400')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()