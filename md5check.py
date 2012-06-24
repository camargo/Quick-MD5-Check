#!/usr/bin/env python
#
# Quick MD5 Hash Check
# Copyright (C) 2012 Chris Camargo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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