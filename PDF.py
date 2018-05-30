import sys
from os import listdir
try:
	from fpdf import FPDF
except Exception as e:
	print("Please install 'fpdf' using 'pip3 install fpdf'")
	sys.exit(1)

def main():
	# location of the images
	
	path = input("Provide the path for IMAGES")
	notesImages = listdir(path)
	notesImages.sort()

	pdf = FPDF('P', 'mm', 'A4')

	x, y, w, h = 0, 0, 210, 297

	for image in notesImages:
		pdf.add_page()
		pdf.image(path + '/' + image, x, y, w, h)

	namePdf = input('Provide name of PDF "USE .pdf" including destination folder\n')
	pdf.output(namePdf, "F")

if __name__ == '__main__':
	main()