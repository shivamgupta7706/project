import webbrowser as wb
def main():
	url="http://www.codeforces.com/"
	choice=int(input("\t1.To Display the User's Profile\n\t2.To see the Question:\n\t3.To Display User's Submission\n\t"))
	if choice==1:
		handle=input("Enter the CodeForces Handle of the User:")
		url=url+"profile/"+handle
	elif choice==2:
		con_no=int(input("Enter the Contest no.:\t"))
		level=input("Enter the Level:\t")
		url=url+"problemset/problem/"+str(con_no)+"/"+level
	elif choice ==3:
		handle=input("Enter the CodeForces Handle of the User:")
		url=url+"submissions/"+handle
	wb.open_new_tab(url)

if __name__ == '__main__':
	main()