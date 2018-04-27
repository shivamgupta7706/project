def convolution(x_n, pos_x_n, h_n, pos_h_n):
	y_n = []
	pos_y_n = []

	for i in range(len(x_n)):
		for j in range(len(h_n)):
			y_n.append(x_n[i] * h_n[j])
			pos_y_n.append(pos_x_n[i] + pos_h_n[j])

	temp = get_ordered(y_n, pos_y_n)

	pos_y_n = temp.keys()
	y_n = temp.values()
	pos_y_n, y_n = zip(*sorted(zip(pos_y_n, y_n)))
	
	return y_n, pos_y_n

def get_ordered(y_n, pos_y_n):
	
	final = {x:0 for x in pos_y_n}

	for i in range(len(y_n)):
		final[pos_y_n[i]] += y_n[i] 

	return final

def main():
	x_n = [int(x) for x in input("Enter the value of x[n]: \n").split()]
	pos_x_n = [int(x) for x in input("Enter the 'n' of x[n]: \n").split()]
	h_n = [int(x) for x in input("Enter the value of h[n]: \n").split()]
	pos_h_n = [int(x) for x in input("Enter the 'n' of h[n]: \n").split()]

	y_n, pos_y_n = convolution(x_n, pos_x_n, h_n, pos_h_n)

	
	print("Convolution of the given signal is y[n] ")
	print(y_n)
	print("Position of the y[n] i.e n: ")
	print(pos_y_n)


	


if __name__ == '__main__':
	main()