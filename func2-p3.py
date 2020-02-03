"""def Add(x,y):
	a=x+y
	print("Addition is: ",a)
	return
def Sub(p,q):
	s=q-p
	print("SUbtraction is: ",s)
	return

Add(10,40)
Sub(55,88)
"""
def Func3(mylst):
	print("Before Inside: ",mylst)
	#mylst[2]= 100 #Pass by reference
	mylst = [100,200,300] # Pass by value
	print("After Inside: ",mylst)
	return
lst = [1,2,3,4]
print("BEFORE OUTSIDE: ",lst)
Func3(lst)
print("AFTER OUTSIDE: ",lst)

"""
def join(*names,sep=":"):
    return sep.join(names)

print(join('hari','ravi','kumar'))
print(join('earth','mercury','venus',sep = ' -- '))"""