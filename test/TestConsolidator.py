import unittest

from Consolidator import Consoliator
from Plot import plot
consolidator = Consoliator()

class TestConsolidator(unittest.TestCase):


    def test_setUp(self):
        data = consolidator.setUp()
        self.assertEqual(len(data), 3)

    def test_consolidateTax(self):
        data = consolidator.setUp()
        data2 = consolidator.consolidateTax(data[1], data[2])

    def test_plot(self):
        plot()

    def test_getPrice(self):
        consolidator.getPrice()

    #def consolidateAddress(self):

    #def consolidate(self):

    #def write(self):

if __name__ == '__main__':
    unittest.main()