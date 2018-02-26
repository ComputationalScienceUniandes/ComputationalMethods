import numpy as np
def intersection(p1, p2, c, R):

    def elevar(f):
        return f **2
    a = elevar(p2[0] - p1[0]) + elevar(p2[1] - p1[1]) + elevar(p2[2] - p1[2])
    b = 2.0 * ((p2[0] - p1[0]) * (p1[0] - c[0]) +(p2[1] - p1[1]) * (p1[1] - c[1]) +(p2[2] - p1[2]) * (p1[2] - c[2]))

    d = (elevar(c[0]) + elevar(c[1]) + elevar(c[2]) + elevar(p1[0]) + elevar(p1[1]) + elevar(p1[2]) - 2.0 * (c[0] * p1[0] + c[1] * p1[1] + c[2] * p1[2]) - elevar(R))

    i = b * b - 4.0 * a * d

    if i < 0.0:
        print False
    else: 
        if i == 0.0:
        
            p[0] = 1.0

            x1 = (p1[0] + (-b / (2.0 * a)) * (p2[0] - p1[0]), p1[1] + (-b / (2.0 * a))* (p2[1] - p1[1]), p1[2] + (-b / (2.0 * a))* (p2[2] - p1[2]),)
        elif i > 0.0:
        
        
            x1 = (p1[0] + (-b + np.sqrt(i)) / (2.0 * a) * (p2[0] - p1[0]),p1[1] + (-b + np.sqrt(i)) / (2.0 * a) * (p2[1] - p1[1]),p1[2] + (-b + np.sqrt(i)) / (2.0 * a) * (p2[2] - p1[2]))
            
            x2 = (p1[0] + (-b - np.sqrt(i)) / (2.0 * a) * (p2[0] - p1[0]),p1[1] + (-b - np.sqrt(i)) / (2.0 * a) * (p2[1] - p1[1]),p1[2] + (-b - np.sqrt(i)) / (2.0 * a) * (p2[2] - p1[2]),)

    return x1, x2
print (intersection([1,2,3],[2,3,4],[3,3,3],5))