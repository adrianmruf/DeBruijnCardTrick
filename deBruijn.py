import subprocess
import os

"""
The trick has five audience members cut a deck of cards repeatedly and then take a card each.
The mathematician then asks a few questions: “Who had porridge for breakfast?” “Who is holding
a red card?” “Is anyone a Pisces?” “Who has a dog called Stanley?”. The answers to these
questions are sufficient to allow the mathematician to name the card that each person is holding.
This is a python script that
	* Prints the order in which you have to arrange the cards before your performance
	* takes the relevant information ("Who is holding a red card?") and prints the values of the
	  cards the spectators are holding
	* compiles a LaTeX beamer presentation whose title page displays the five cards the audience
	  members are holding

Have fun performing this trick!
"""


def nextFour(string,pop):
	"""
	Input: List of five {0,1} bits
	Output: The input list extended by the next bit in a de Bruijn sequence (given by the irreducible
			polynomial x**5 - x**2 - 1) and the first bit deleted (if pop is set to True) or not (if
			pop is set to False)
	"""
	if (type(string) != list) or not(all((i==0)or(i==1)) for i in string):
		print('Wrong input, please type in a five letter list of zeros and ones')
	string.append((string[-5]+string[-3])%2)
	if pop == True:
		string.pop(0)
	return string

def getDeBruijn(string):
	"""
	Input: Inital list of five {0,1} bits
	Output: The whole (punctured) de Bruijn sequence starting from that position
	"""
	for n in range(0,26,1):
		string = nextFour(string,False)
		print(string)


def wholeDeBruijn(string):
	"""
	Input: Initial list of five {0,1} bits
	Output: The order of the deck used in The de Bruijn Card Trick
	"""
	values = ''
	for n in range(0,31,1):
		values += IdentifySingle(string)
		values += ', '
		string = nextFour(string,True)

	print(values)


def IdentifySingle(string):
	"""
	Input: List of five {0,1} bits
	Output: The card this 5-letter substring of the de Bruijn sequence corresponds to
	"""
	if (type(string) != list) or (len(string)!=5) or not(all((i==0)or(i==1)) for i in string):
		print('Wrong input, please type in a five letter list of zeros and ones')
	cardValue = ''

	x = ''
	x += str(string[-3]) + str(string[-2]) + str(string[-1])

	if int(x,2) != 1:
		if int(x,2) == 0:
			cardValue += '8'
		else:
			cardValue += str(int(x,2))
	else:
		cardValue += 'A'


	if string[0] == 0 and string[1] == 0:
		cardValue += '\u2663'
	if string[0] == 0 and string[1] == 1:
		cardValue += '\u2660'
	if string[0] == 1 and string[1] == 0:
		cardValue += '\u2666'
	if string[0] == 1 and string[1] == 1:
		cardValue += '\u2665'

	return cardValue

def IdentifyFive(string):
	"""
	Input: The list of five {0,1} bits you obtain from the spectators
	Output: The values of the cards they are holding
	"""
	if (type(string) != list) or (len(string)!=5) or not(all((i==0)or(i==1)) for i in string):
		print('Wrong input, please type in a five letter list of zeros and ones')
	cards = ''
	cards += IdentifySingle(string)
	for i in range(0,4,1):
		cards += ', '
		nextFour(string,True)
		cards += IdentifySingle(string)
	return cards


def IdentifySingleToTex(string):
	"""
	Input: List of five {0,1} bits
	Output: Latex code corresponding to the value of the card this 5-letter substring encodes
	"""
	if (type(string) != list) or (len(string)!=5) or not(all((i==0)or(i==1)) for i in string):
		print('Wrong input, please type in a five letter list of zeros and ones')
	cardValue = '\crd'

	x = ''
	x += str(string[-3]) + str(string[-2]) + str(string[-1])

	if int(x,2) == 0:
		cardValue += 'eig'
	elif int(x,2) == 1:
		cardValue += 'A'
	elif int(x,2) == 2:
		cardValue += 'two'
	elif int(x,2) == 3:
		cardValue += 'tre'
	elif int(x,2) == 4:
		cardValue += 'four'
	elif int(x,2) == 5:
		cardValue += 'five'
	elif int(x,2) == 6:
		cardValue += 'six'
	elif int(x,2) == 7:
		cardValue += 'sev'
	# if int(x,2) != 1:
	# 	if int(x,2) == 0:
	# 		cardValue += '8'
	# 	else:
	# 		cardValue += str(int(x,2))
	# else:
	# 	cardValue += 'A'


	if string[0] == 0 and string[1] == 0:
		cardValue += 'c'
	if string[0] == 0 and string[1] == 1:
		cardValue += 's'
	if string[0] == 1 and string[1] == 0:
		cardValue += 'd'
	if string[0] == 1 and string[1] == 1:
		cardValue += 'h'

	return cardValue

def IdentifyToTex(string):
	"""
	Input: The list of five {0,1} bits you obtain from the spectators
	Output: Latex code corresponding to the values of the five cards the spectators are holding
	"""
	if (type(string) != list) or (len(string)!=5) or not(all((i==0)or(i==1)) for i in string):
		print('Wrong input, please type in a five letter list of zeros and ones')
	cards = ''
	cards += IdentifySingleToTex(string)
	for i in range(0,4,1):
		cards += ' '
		nextFour(string,True)
		cards += IdentifySingleToTex(string)
	return cards




if __name__ == "__main__":
	print("Arrange your deck according to this order (of 31 cards):")
	wholeDeBruijn([0,0,0,0,1])

	### Modify this next line in accordance with the distribution of red (1) and black (0) cards the
	### spectators are holding
	string = [0,0,1,1,1]

	print("Those are the values of the cards the spectators are holding:")
	temp = string.copy()
	print(IdentifyFive(temp))

	temp2 = string.copy()
	lan = IdentifyToTex(temp2)

	### This creates a LaTeX beamer presentation which has the cards the spectators are holding on the
	### title page

	with open("de_Bruijn.tex", "w") as tex_file:
		tex_file.write(r"""\documentclass[10pt]{beamer}
\usepackage{amsmath, amssymb, xcolor}
\usepackage{pstricks-pdf}
\usepackage{pst-poker}
\title{\Large \textcolor{black}{What if we would use math to do card tricks?}}
\author{\large\textcolor{gray!90!black}{Adrian~M. Ruf}}
\date{}
\setbeamertemplate{navigation symbols}{}
\begin{document}
\begin{frame}
	\maketitle
	\vspace{-5em}
	\centering
	\begin{postscript}
	""")
		tex_file.write(lan)
		tex_file.write(r"""
\end{postscript}
\end{frame}
\begin{frame}
\centering \huge Thanks!
\end{frame}
\end{document}""")
	subprocess.call(["/Library/TeX/texbin/latex", "de_Bruijn.tex"])
	subprocess.call(["/Library/TeX/texbin/dvips", "-o" "de_Bruijn.ps", "de_Bruijn.dvi"])
	subprocess.call(["/usr/local/bin/ps2pdf", "de_Bruijn.ps"])
	subprocess.call(["/Library/TeX/texbin/latex", "de_Bruijn.tex"])


	
