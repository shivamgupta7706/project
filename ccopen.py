import webbrowser as wb
def main():
	url="https://www.codechef.com/"
	print("\tWhat do you want: ")
	choice=int(input("\t1.Open CodeChef \n\t2.Open Long Challenge \n\t3.Open any Question \n\t4.Open Profile of the User\n"))
	if choice==1:
		pass
	elif choice==2:
		t=input("Enter the MONTH: ")
		t=t.upper()
		url=url+t+'/'
	elif choice==3:
		y=input("Enter its Submission Code: ")
		y=y.upper()
		url=url+"problems/"+y+"/"
	elif choice==4:
		handle=input("Enter the CodeChef Handle of the User: ")
		url=url+"users/"+handle+"/"
	else :
		url="https://www.google.com/"
	wb.open_new_tab(url)

if __name__ == '__main__':
	main()