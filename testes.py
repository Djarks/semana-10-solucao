import unittest;
import numeroromano as nr;

class numeroromanoTest(unittest.TestCase):

    def testI(self):
        self.assertEqual(1, nr.converte('I'), 'Erro converter I');

    def testV(self):
        self.assertEqual(5, nr.converte('V'), 'Erro converter V');
    
    def testII(self):
        self.assertEqual(2, nr.converte('II'), 'Erro converter II');
    
    def testXXII(self):
        self.assertEqual(22, nr.converte('XXII'), 'Erro converter XXII');

    def testIX(self):
        self.assertEqual(9, nr.converte('IX'), 'Erro converter IX');
    
    def testXXIV(self):
        self.assertEqual(24, nr.converte('XXIV'), 'Erro converter XXIV');

if __name__ == "__main__":
  unittest.main()