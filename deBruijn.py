import subprocess
import os


def nextFour(string,pop):
	if (type(string) != list) or not(all((i==0)or(i==1)) for i in string):
		print('Wrong input, please type in a five letter list of zeros and ones')
	string.append((string[-5]+string[-3])%2)
	if pop == True:
		string.pop(0)
	return string

def getDeBruijn(string):
	for n in range(0,26,1):
		string = nextFour(string,False)
		print(string)

	# string.insert(0,0)

def wholeDeBruijn(string):
	values = ''
	for n in range(0,26,1):
		string = nextFour(string,False)
		print(string)
		temp = copy(string[-5:-1])
		values += IdentifySingle(temp)
		values += ', '

	# string.insert(0,0)
	print(values)


def IdentifySingle(string):
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
	string = [0,0,1,1,1]
	# print(IdentifyFive(string))
	
	lan = IdentifyToTex(string)

	# string.extend(string)
	# for i in range(0,31,1):
	# 	print(IdentifySingle(string[i:i+5]))



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


	