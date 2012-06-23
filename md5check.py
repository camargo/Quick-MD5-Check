'''
Quick MD5 Hash Check

Copyright © Chris Camargo 2011-2012, All rights reserved.

This software has only three copyright restrictions. 
Firstly, this copyright notice must remain intact and unmodified. 
Secondly, the Author, Chris Camargo, 
must be appropriately and prominantly credited in any documentation associated with any derived work. 
Thirdly unless otherwise negotiated with the author, 
you may not sell this program commercially, reasonable distribution costs excepted.

Use and or distribution of this software implies acceptance of the above.
'''

import sys
import hashlib

def main():
	try:
		filename = sys.argv[1]
		realMd5 = sys.argv[2]
	except IndexError:
		print("Usage: <file to check> <file valid MD5 hash>")
		sys.exit()
	else:
		testFile = open(filename, "rb")
		newHash = hashlib.md5()
	
		while True:
			piece = testFile.read(1024)
			if piece:
				newHash.update(piece)
			else:
				hashedMd5 = newHash.hexdigest()
				break
	
	if (hashedMd5 == realMd5):
		print("MD5 Varified! :)")
	else:
		print("MD5 NOT Varified :(")
	
	testFile.close()

if __name__ == '__main__':
	main()