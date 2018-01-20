# This has been hard coded to work with uncompressed a 24b and 32b pixel .bmp files
import math
import numpy as np
import os

def inputBMP(fileName, pFlag = 'n'):
	if not (os.path.exists(fileName)):
		print "File not found."
		return 0
	if(pFlag == 'p'):
		print "Opening", fileName, "...",
	with open(fileName, "rb") as imageFile:
		file = imageFile.read()
		bmpBytes = bytearray(file)

	if (bmpBytes[0] != 66 or bmpBytes[1] != 77):	# .bmp files start with "BM"
		print "ERROR: Incorrect Filetype (only .bmp files accpeted)"
		return

	pixelSize     = bmpBytes[28]
	bytesPerPixel = pixelSize/8
	fileSize      = bmpBytes[3]*256+bmpBytes[2]	# two byte little-endian value
	headerSize    = bmpBytes[10]
	pixelArray    = bytearray(fileSize - headerSize)
	imgWidth      = bmpBytes[18]
	imgHeight     = bmpBytes[22]
	offset        = ((fileSize-headerSize)-(imgWidth*imgHeight*bytesPerPixel))/imgHeight%4

	for x in range(0, fileSize - headerSize):
		pixelArray[x] = bmpBytes[x + headerSize]

	if bytesPerPixel < 3 or bytesPerPixel > 4:
		print "ERROR: Image Size (only 23 bit and 32 bit pixels accpeted accepted)"
		return

	pixels = [[[0 for k in xrange(3)] for j in xrange(imgWidth)] for i in xrange(imgHeight)]
	counter = 0
	for i in xrange(imgHeight):
		for j in xrange(imgWidth):
			for k in range(bytesPerPixel-3, bytesPerPixel):
				pixels[i][j][k-(bytesPerPixel-3)] = pixelArray[counter]
				counter += 1
			counter += (bytesPerPixel-3)
		counter += offset

	# average is based on gray scale RGB value
	normalizedArray = [[np.average(pixels[i][j])/255 for j in xrange(imgWidth)] for i in xrange(imgHeight)]
	
	inputArray = []
	for i in range(0, imgHeight):
		for j in range(0, imgWidth):
			inputArray.append(normalizedArray[i][j])

	if(pFlag == 'p'):
		print " Input array length:", len(inputArray)
	if(pFlag == 'p'):
		#for i in xrange(0,imgHeight,1):
		for i in xrange(imgHeight-1, -1, -1):
			print "\t",
			for j in range(0, imgWidth):
				print '%.1d' % inputArray[imgWidth*i+j],
			print ""
		print ""
	return inputArray