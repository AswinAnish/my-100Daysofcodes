l=0
u=0
c=0
d=0

pw=input("ENTER A PASSWORD:-")

if len(pw)<6:
	print("length should be greater than 6")
	
else:
	for i in pw:
		if(i.isupper()):
			u=u+1
		if(i.islower()):
			l=l+1
		if(i.isdigit()):
			d=d+1
		if (i=='@' or i=='#' or i=='$'):
			c=c+1
	print(l,u,c,d)
	if l>=1 and u>=1 and c>=1 and d>=1:
		print("the password is valid")
	else:
		print("the password is not valid")
	
		 
