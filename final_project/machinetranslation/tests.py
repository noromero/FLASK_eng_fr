import unittest
from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
  def test1(self):
    self.assertEqual(englishToFrench('Hello'),'Bonjour')
  def test2(self):
    self.assertNotEqual(englishToFrench('Hello'),'Hello')
  def test3(self):
    self.assertEqual(englishToFrench(0),'0')

class TestF2E(unittest.TestCase):
  def test1(self):
    self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
  def test2(self):
    self.assertNotEqual(frenchToEnglish('Bonjour'),'Bonjour')
  def test3(self):
    self.assertEqual(frenchToEnglish(0),'0')
    
unittest.main()  