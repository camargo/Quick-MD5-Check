# Quick MD5 Hash Check by Chris Camargo

import sys
import hashlib

def main():
	try:
		filename = sys.argv[1]
		realMd5 = sys.argv[2]
	except IndexError:
		print("Usage: <file to check> <file's valid MD5 hash>")
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