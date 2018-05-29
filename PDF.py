import sys
from os import listdir
try:
	from fpdf import FPDF
except Exception as e:
	print("Please install 'fpdf' using 'pip3 install fpdf'")
	sys.exit(1)
 

def main():
	# location of the images
	path = ''

	notesImages = listdir(path)
	notesImages.sort()

	pdf = FPDF('P', 'mm', 'A4')

	x, y, w, h = 0, 0, 210, 297

	for image in notesImages:
		pdf.add_page()
		pdf.image(path + '/' + image, x, y, w, h)

	pdf.output('name.pdf', 'F')

if __name__ == '__main__':
	main()