'''
Author: Darian Lopez / https://github.com/midwestcoder2020
Github : https://github.com/midwestcoder2020
Purpose: Allows user to enter name of Google device location csv file 
and convert it to a google earth pro friendly kml file to be inported and viewed

Note: 'tool dynamically creates kml tags based of csv header columns. Tool also prepends the corresponding column name to the each xml object which allows for future identification when viewed in google earth pro or similar platform'
'''


def getFileName():

	fileName = input("Enter the file name to be parsed)
	return fileName


def genFile(fileName):
	data = open(fileName).readlines()
	cols = data[0].split(",")
	finalEntry =[]
	totalEntry = data[1:]
	print(totalEntry)

	with open("mock_data.kml","a+") as f:
		f.write("{}\n".format(r'<?xml version="1.0" encoding="UTF-8"?>'))
		f.write("{}\n".format(r'<kml xmlns="http://www.opengis.net/kml/2.2">'))
		f.write("{}\n".format(r'<Folder>'))

		for y in range(len(totalEntry)):
			f.write("{}\n".format('\t<Placemark>'))
			for x in range(len(cols)):
				f.write("{}\n".format('\t<{}>'.format(cols[x])))
				f.write("{}\n".format('\t\t{}'.format(cols[x]+" "+totalEntry[y].split(",")[x].replace("\n",""))))
				f.write("{}\n".format('\t</{}>'.format(cols[x])))
			f.write("{}\n".format('\t</Placemark>'))
		f.write("{}\n".format(r'</Folder>'))
		f.write("{}\n".format(r'</kml>'))
	f.close()
	
if name == __main__:
	
	
	try:
		fileName = getFileName()
	except:
		print("unable to get user file input")
	
	try:
		getFileName(fileName)
	except:
		print("unable to parse and generate file")
