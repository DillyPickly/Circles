import numpy as np
import matplotlib.pyplot as plt

# 3 seed circles

circle1 = [(0,0),1]
circle2 = [(2/3,0),1/3]
circle3 = [(0,-.5),.5]

def new_circle(circle1, circle2, circle3):
    (a1,b1), r1 = [*circle1]
    (a2,b2), r2 = [*circle2]
    (a3,b3), r3 = [*circle3]
    
    A = 2*np.array([[ a2-a1 ,  b2-b1 ,   r2+r1 ],
                    [ a3-a2 ,  b3-b2 ,   r3-r2 ],
                    [ a1-a3 ,  b1-b3 ,  -r1-r3 ]])

    B = np.array(  [a2**2-a1**2 + b2**2-b1**2 + r1**2-r2**2,
                    a3**2-a2**2 + b3**2-b2**2 + r2**2-r3**2,
                    a1**2-a3**2 + b1**2-b3**2 + r3**2-r1**2])

    print(A,'\n')
    print(B)

    A_inv = np.linalg.pinv(A)
    a, b, r = [*np.matmul(A_inv, B)]
    return [(a,b), r]

circle4 = new_circle(circle1,circle2,circle3)

fig, ax = plt.subplots(figsize=(6,6))

ax.add_artist(plt.Circle(*circle1, alpha=0.7))
ax.add_artist(plt.Circle(*circle2, alpha=0.7))
ax.add_artist(plt.Circle(*circle3, alpha=0.7))
ax.add_artist(plt.Circle(*circle4, alpha=0.7))

# print(circle4)

ax.set_ylim((-1,1))
ax.set_xlim((-1,1))


plt.savefig("temp.png", bbox_inches="tight")
# plt.show()