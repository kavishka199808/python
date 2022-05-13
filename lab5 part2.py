Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="Python"
s[0]
'P'
s[-2]
'o'
s[1]
'y'
range(10)
range(0, 10)
range
<class 'range'>
range(3,7)
range(3, 7)
s="abcdefghij"
s[2:5]
'cde'
s[3:6]
'def'
s[:]
'abcdefghij'
s[:4]
'abcd'
s[1:]
'bcdefghij'
s[1:6]
'bcdef'
s[1:6:2]
'bdf'
s[1:6:3]
'be'
s[-1]
'j'
s[::-1]
'jihgfedcba'
s[8:0:-1]
'ihgfedcb'
s[8::-1]
'ihgfedcba'
a=22
str(a)
'22'
bool(5>7)
False
bool(5==5)
True
bool()
False
chr(100)
'd'
chr(65)
'A'
ord('A')
65
5<7
True
eval('5<7')
True
eval('5+5')
10
a=input("Enter charactor")
Enter charactork
s
'abcdefghij'
a
'k'
b=ord(a)
print(b)
107

range(10)
range(0, 10)
list(rage(10))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    list(rage(10))
NameError: name 'rage' is not defined. Did you mean: 'range'?
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
list(rage(1,15,2))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list(rage(1,15,2))
NameError: name 'rage' is not defined. Did you mean: 'range'?
list(range(1,15,2))
[1, 3, 5, 7, 9, 11, 13]
list(range(9,2,-1))
[9, 8, 7, 6, 5, 4, 3]
list(range(10,1,-2))
[10, 8, 6, 4, 2]
list(range(10,2))
[]
