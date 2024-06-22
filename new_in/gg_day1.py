import math
def latice_pint_insid_triangle(p,q,r):
    def triangle_area(p1,p2,p3):
        return abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))/2
    def boundary_point(p1,p2):
        return math.gcd(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]+1))
    A=triangle_area(p,q,r)
    B=boundary_point(p,q)+boundary_point(q,r)+boundary_point(r,p)-3
    I=A-B/2+1
    return int(I)

#input part
def get_point(pint_name):
    x,y=map(int,input(f"enter the pint {pint_name}: ").split())
    return (x,y)
p=get_point('p')
q=get_point('q')
r=get_point('r')

print("number of latis point is ",latice_pint_insid_triangle(p,q,r))
