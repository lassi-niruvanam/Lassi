import லஸ்ஸி as ல

உரை_௧ = """

a = [1, 2, 3, 4, 5, 6, 7, 12587.]
x = True
if not x:
    print(10)
print(a)
b = [100, 200, 300, 450, 1234567890, 1000000000, 123.0456]

class b(object):
    def test(x, y):
        if x:
            return True
        else:
            return False

"""
உரை_௨ = """

a = 123.4
b = 10

def c(x, y):
    print(x, y)
    if x > y:
        return x * y
    else:
        return False

print(c(a, b))

for i in range(1, 100):
    print("Hello, World!")

"""
உரை_௩ = """
y
x = function()
class Circle(object):
    pi = 3.141592653
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2 * self.pi * self.radius
    def area(self):
        return self.pi ** 2 * self.radius

radii = range(5)
circles = [Circle(radius=r) for r in radii]

for c in circles:
    print(c.circumference(), c.area())

if True:
    pass
elif False:
    pass
else:
    pass

while c:
    pass
with x as y, z as a, w:
    with y:
        pass

"""

முன்_மொழி = 'en'
for உரை in [உரை_௧, உரை_௨, உரை_௩]:
    for மொழி in ['த', 'fr', 'ار', 'हिं', '汉', 'kaq', முன்_மொழி]:
        உரை = ல.மொழியாக்கம்(உரை, 'python', மொழி=மொழி, மூல்மொழி=முன்_மொழி)
        முன்_மொழி = மொழி
        print(f'******{மொழி}******')
        print('=' * (12 + len(மொழி)))
        print(உரை)
