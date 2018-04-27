from math import e, pi

def getDFT(matrix, x, N):

	temp = []
	for i in range(N):
		temp_sum = 0
		for j in range(N):
			temp_sum += matrix[i][j] * x[j]
	
		temp.append(round(temp_sum.real, 2) + round(temp_sum.imag, 2) * 1j)

	return temp

def getMatrix(N, W):
	matrix = []
	for i in range(N):
		temp = [round((W ** (i*x)).real, 2) + round((W ** (i*x)).imag, 2) * 1j  for x in range(N)]
		matrix.append(temp)

	return matrix

def getW(N):
	b = (2*pi)/N
	temp = e ** complex(0, b)

	return round(temp.real, 2) + round(temp.imag, 2) * 1j

def getComplexed(a):
	complex_x = []
	for i in range(len(a)//2):
		complex_x.append(complex(a[2*i], a[2*i+1]))
	return complex_x

def main():
	N = int(input("Enter the value of N: "))
	W = getW(N)
	matrix = getMatrix(N, W)

	x = [int(x) for x in input("Enter the value of x[n] in format (a + ib) as 'a b' space seprated\n").split()]
	complex_x = getComplexed(x)
	
	X_n = getIDFT(matrix, x, N)

	print("Following is the IDTFT of the signal")
	for i in range(N):
		print('x['+str(i)+'] =',X_n[i])

if __name__ == '__main__':
	main()