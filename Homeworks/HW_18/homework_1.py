#1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y.
# კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ  ვექტორების დამატება და __str__ მეთოდი, 
#რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".

#მაგალითად:
#v1 = Vector(2, 3)
#v2 = Vector(3, 4)
#v3 = v1 + v2
#print(v3)  # Output: (5, 7)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # ასე ჯობია
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

#---------------------#
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3) 


