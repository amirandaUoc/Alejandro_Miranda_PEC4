import unittest
from orfManagement import countOrf,countOrfByClassDescription,countClassByOrfDescription

class OrfManagementTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._testFilePath = "input/testOrfManagement.pl"

    def testCountOrfByClassDescription(self):
         self.assertEqual(0,countOrfByClassDescription(self._testFilePath, "noFound"))
         self.assertEqual(1,countOrfByClassDescription(self._testFilePath, "test class"))

    def testCountOrf(self):
        self.assertEqual({'1,1,0,0': 2, '1,1,1,0': 15, '1,1,3,0': 1},countOrf(self._testFilePath))

    def testCountClassByOrfDescription(self):
        self.assertEqual(2,countClassByOrfDescription(self._testFilePath,"test",5))
        self.assertEqual(1,countClassByOrfDescription(self._testFilePath,"UDP-glucose"))



suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(OrfManagementTest))
unittest.TextTestRunner(verbosity=2).run(suite)
