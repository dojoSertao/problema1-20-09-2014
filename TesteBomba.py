import unittest
from Bomba import joga

class TesteBomba(unittest.TestCase):
	#Construir um metodo que, testes se o valor 1 e valido
	def testa_se_for_1(self):
		self.assertEqual(joga(1),1)

	def testa_se_for_2(self):
		self.assertEqual(joga(2),2)

	def testa_se_for_3(self):
		self.assertEqual(joga(3),'bomba')

	def testa_se_for_4(self):
		self.assertEqual(joga(4),4)

	def testa_se_for_5(self):
		self.assertEqual(joga(5),'bomba')

	def testa_se_for_6(self):
		self.assertEqual(joga(6),'bomba')

	def testa_se_for_7(self):
		self.assertEqual(joga(7),7)

	def testa_se_for_8(self):
		self.assertEqual(joga(8),8)

	def testa_se_for_9(self):
		self.assertEqual(joga(9),'bomba')

	def testa_se_for_15(self):
		self.assertEqual(joga(15),'bomba_atomica')

unittest.main()
