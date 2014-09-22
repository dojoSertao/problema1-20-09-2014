def joga(valor):
	if (valor % 3 == 0 and valor % 5 == 0):
		return 'bomba_atomica'
	else:
		if (valor % 3 == 0 or valor % 5 == 0):
			return 'bomba'
		else:
			return valor