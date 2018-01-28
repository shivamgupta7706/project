import matplotlib.pyplot as plt
def main():
	#Choice of the User which graph to draw
	choice=input("Which Graph is to be drawn\n1.Line Graph\n2.Point Graph\n")
	t=input("Enter the title for the Graph: ")
	xlab=input("Enter the Label for X-axis: ")
	ylab=input("Enter the label for Y-axis: ")
	#Title for Graph
	plt.title(t)
	#X-Label for the Graph
	plt.xlabel(xlab)
	#Y-Label for the Graph 
	plt.ylabel(ylab)

	contentx=[int(x) for x in input("Enter the Values for X axis: ").split()]
	contenty=[int(y) for y in input("Enter the Values for Y axis: ").split()]
	if choice == '1':
		plt.plot(contentx,contenty)
	elif choice == '2':
		plt.scatter(contentx,contenty,contentx,color='r')
	else:
	 	print("Wrong Choice!")

	#for Display of the Graph
	plt.show()

if __name__ == '__main__':
	main()