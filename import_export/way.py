import sys
import os 

def change_way(symbol='\\', num=0, inside='/'):
	string = os.path.dirname(os.path.realpath(__file__))
	spl_string = string.split('\\')
	if not num == 0 :
		spl_string = spl_string[:num]
	listToStr = symbol.join([str(elem) for elem in spl_string])
	if not inside == '/' :
		listToStr = listToStr + inside
	return listToStr