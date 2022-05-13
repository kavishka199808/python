Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=2
a
2
type(a)
<class 'int'>
a=b=c=1
a
1
b
1
c
1
type(a)
<class 'int'>
a=45
type(a)
<class 'int'>
b='This is a string'
type(b)
<class 'str'>
c=2+1j
type(c)
<class 'complex'>
d=[1,2,3,5,6]
type(d)
<class 'list'>
3/4
0.75
3//4
0
25/5
5.0
25//5
5
-20//3
-7
-20/3
-6.666666666666667
-20%3
1
a=3
print(a)
3
print("Hello world")
Hello world
a,b,c  = 1,2.5,"a,b,c"
print(a,b,c)
1 2.5 a,b,c
print(a,b,c sep="=")
SyntaxError: invalid syntax
print(a,b,c, sep="=")
1=2.5=a,b,c
print(a,b,c, sep=" ")
1 2.5 a,b,c
w,x,y,z = 10,15,20,25
print(w,x,y,z)
10 15 20 25
print(w,x,y,z sep='-')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(w,x,y,z, sep='-')
10-15-20-25
print(w,x,y,z, sep='*')
10*15*20*25
input("Enter Number : ")
Enter Number : 23
'23'
a = int(input('Enter a number'))
Enter a number14

print(a)
14

a=float(input('Enter a number'))
Enter a number14
print(a)
14.0
