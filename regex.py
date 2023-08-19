import re
txt='''KAITRINA KAIF	39 years	16 JUL 1983 phone number: 017-12378912
DEEPIKA PADUKONE	36 years	5 JAN 1986 phone number: 017-17578912
PRIYANKA CHOPRA	40 years	18 JUL 1982 phone number: 017-12753912
KANGANA RANAUT	35 years	23 MAR 1987 phone number: 017-12379581
ANUSHKA SHARMA	34 years	1 MAY 1988 phone number: 017-58278912
ALIA BHATT	29 years	15 MAR 1993 phone number: 017-12395612
SHRADDHA KAPOOR	35 years	3 MAR 1987 phone number: 018-22378912 fjieeol34@hotmail.com
SARA A KHAN	27 years	12 AUG 1995 phone number: 01912378512 abdjli@gamil.com'''
x=re.findall("\d{2} [a-zA-Z]{1,3}", txt)
print(x)
y=re.findall("\d{3}-?\d{8}", txt)
print(y)
z=re.findall("[\w.]+\@[\w.]+",txt)
print(z)