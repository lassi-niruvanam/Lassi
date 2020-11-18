import லஸ்ஸி as ல


உரை_அடிமானம் = '''
a உடன்:
    விடு

'''
'''
x.y = "இலிருந்து"
x = "இலிருந்து"
தொகுப்பு அடிமானம் (இடஞ்சார்):
    நிரல்பாகம் __init__ (தன், பெயர், ஒருங்குறி, அடிமானங்கள், குறிகள், பிரிப்பு, அடுக்குக்குறி):
        super ( ) . __init__ ( பெயர் , ஒருங்குறி , குறிகள் = குறிகள் , பிரிப்பு=பிரிப்பு , அடுக்குக்குறி = அடுக்குக்குறி )

        தன்.அடிமானங்கள் = OrderedDict(sorted(அடிமானங்கள்.items(), key=lambda விசை: (விசை[௧] , விசை [ ௦ ] ) ) )
        தன் . அடிமானம் = len ( தன் . குறிகள் ) 

'''
உரை_௧ = """
import re
import regex as re
from lark import Lark
from lark import Lark as லார்க்
[x for x in z]

x == 1
y += 2
x in [1,2,3]
f = fr'{[123]}'
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

இனங்காட்டி_மொழியாக்கம் = [
            {
                'fr': 'fonction',
                'த': "செயலி",
                'en': 'function'
            },
            {
                'fr': 'soimême',
                'த': "தன்",
                'en': 'self'
            },
            {
                'fr': 'Cercle',
                'த': "வட்டம்_தொகுப்பு",
                'en': 'Circle'
            },
            {
                'fr': 'cercle',
                'த': "வட்டம்",
                'en': 'circle'
            },
            {
                'fr': '__init__',
                'த': "__துவக்கம்__",
                'en': '__init__'
            },
            {
                'fr': 'rayon',
                'த': "ஆரம்",
                'en': 'radius'
            },
            {
                'fr': 'circonférence',
                'த': "சுற்றளவு",
                'en': 'circumference'
            },
            {
                'fr': 'pi',
                'த': "பை",
                'en': 'pi'
            }
            ,
            {
                'fr': 'rayons',
                'த': "ஆரங்கள்",
                'en': 'radii'
            }
            ,
            {
                'fr': 'gamme',
                'த': "சரகம்",
                'en': 'range'
            }
            ,
            {
                'fr': 'cercles',
                'த': "வட்டங்கள்",
                'en': 'circles'
            }
            ,
            {
                'fr': 'r',
                'த': "ஆ",
                'en': 'r'
            },
            {
                'fr': 'objet',
                'த': "பொருள்",
                'en': 'object'
            },
            {
                'fr': 'affiche',
                'த': "பதிப்பி",
                'en': 'print'
            },
            {
                'fr': 'superficie',
                'த': "பரப்பளவு",
                'en': 'area'
            },
            {
                'fr': 'x',
                'த': "இ",
                'en': 'x'
            },
            {
                'fr': 'y',
                'த': "ஈ",
                'en': 'y'
            },
            {
                'fr': 'z',
                'த': "ஊ",
                'en': 'z'
            },
            {
                'fr': 'w',
                'த': "ஏ",
                'en': 'w'
            },
            {
                'fr': 'c',
                'த': "வ",
                'en': 'c'
            }
        ]

முன்_மொழி = 'en'
for உரை in [உரை_௧, உரை_௨, உரை_௩]:
    for மொழி in ['த', 'fr', 'ار', 'हिं', '汉', 'kaq', முன்_மொழி]:
        # p = ல.பகுப்பாய்வி_பெறு('python', மொழி=முன்_மொழி)
        # print(p.parse(உரை, 'file_input').pretty())
        உரை = ல.மொழியாக்கம்(உரை, 'python', மொழி=மொழி, மூல்மொழி=முன்_மொழி, இனங்காட்டிகள்=இனங்காட்டி_மொழியாக்கம்)
        முன்_மொழி = மொழி
        print(f'******{மொழி}******')
        print('=' * (12 + len(மொழி)))
        print(உரை)
