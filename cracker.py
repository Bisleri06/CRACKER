import crypt
import sys
import re

def usage():														# The help function.
	print('''\033[94m
 _                         _    
| |__   ___ _ __ __ _  ___| | __
| '_ \ / __| '__/ _` |/ __| |/ /
| | | | (__| | | (_| | (__|   < 
|_| |_|\___|_|  \__,_|\___|_|\_\
\033[92m

usage: hcrack [hash-to-crack-here] [wordlist]

Report any bugs.
\033[91m
NOTE: PLEASE USE A "\\" OR ALSO KNOWN AS "backslash" BEFORE EVERY "$" CHARACTER IN YOUR hash-to-crack-here ARGUMENT FOR SOME REASONS OR IT MAY BREAK THE CRACKER.
''')

def testpass(passw,fi,salt):											# The cracker function.
	i=0
	for w in fi.readlines():
		i+=1
		l=w.strip("\n")
		cw=crypt.crypt(l,salt)
		if(cw==passw):
			print("\033[94m[+]\033[97mPassword is \033[91m"+w+"\033[0m")
			return

	print("\033[91m[-]\033[97mPassword not found"+"\033[0m")


def main():

	arg=sys.argv
	
	if(len(arg)!=3):
		print("Invalid number of arguments")								# If user enters rubbish.
		usage()
		exit(1)

	word=open(arg[2],"r")

	pat=r"[\$]"
	passw=arg[1]
	if(len(re.findall(pat,passw))==3):
		m=passw.split("$")												# The password verification.
		salt=m[2]
		che="$"+m[1]+"$"
		salt=che+salt


		print("\033[94m[+]\033[97mCracking the hash")
		testpass(passw,word,salt)		
	
	else:															# Incase if the user enters some thing else.
		print("Wrong format of password entered")
		usage()
		word.close()
		exit(1)

main()
