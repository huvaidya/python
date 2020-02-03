add = 3333
def Matfun(x,y=55):
	add = x+y
	print("Addition is", add)
	sub = y-x
	mul = x*y
	print("Multiplication is:", mul)
	print(sub)
	return

def Fun_Name(name):
	print("Hello, ",name)
	return

def Func1():
	print("This is without parameter")
	return

Matfun(10,30)
Matfun(4)
print(add)
Fun_Name("Himanshu")
Func1()

# pass by ref vs pass by value

def Ref_Val(lst):
	print("Before: ", lst)
	#lst[2]="Replace"
	lst = [22,33,44,55]
	print("After: ", lst)
	return

lst1 = ["hi", "hello", 22, 55, "Python"]
Ref_Val(lst1)
#Ref_Val([1,2,3,4,5])
print(lst1)






