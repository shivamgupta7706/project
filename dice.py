import random as r
def main():

	s='y'
	while s=='y':
		k=r.randint(1,6)
		if k==6:
			s='y'
		else:
			s='n'
		print(k,end=" ")
	print()

if __name__ == '__main__':
	main()