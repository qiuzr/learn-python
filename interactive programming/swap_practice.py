a= raw_input("please input a :")
b= raw_input("please input b :")
def swap():
	global a,b
	a,b=b,a
	print"swap a and b"
	print"a=",a
	print"b=",b
	print" "
swap()