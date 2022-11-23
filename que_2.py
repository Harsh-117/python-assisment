class Triangle():
    def __init__(self,s):
        self.s=s
    def validate_triangle(self,p):
        if len(p)==3 and (p[0]+p[1])>p[2]:
            return 'Valid Triangle'
        else:
            return 'Invalid Triangle'

class Rectangle():
    def __init__(self,s):
        self.s=s
    def validate_rectangle(self,p):
        if len(p)==4 and (p[0]==p[2]) and (p[1]==p[3]):
            return 'Valid Rectangle'
        else:
            return 'Invalid Rectangle'
x = list(map(int,input().split()))
T = Triangle(x)
print(T.validate_triangle(x))
y = list(map(int,input().split()))
R= Rectangle(y)
print(R.validate_rectangle(y))
