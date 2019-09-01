import os

from ਲੱਸੀ.ਵਾਧਾ.ਪੈਧਾਨ_੩ import ਪੈਧਾਨ_੩_ਵਿਆ

ਵਿਆ = ਪੈਧਾਨ_੩_ਵਿਆ()
ਵਿਆ.actualizar_trads(['த', 'ગુ', 'ਪੰ', 'हिं', 'fr', 'kaq', 'ار', 'فا', '汉', 'ml', "tz'u"])
c = """

a = [1, 2, 3, 4, 5, 6, 7, 12587]
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
c2 = """

a = 123.4
b = 10

def c(x, y):
    print(x, y)
    if x > y:
        return x * y
    else:
        return False

print(c(a, b))

"""

# ਪੈਧਾਨ_੩_ਵਿਆ().ਦਸਤਾਵੇਜ਼_ਅਨੁਵਾਦ(os.path.join(os.path.split(__file__)[0], 'test.汉.py'), 'ار', '汉')

fr = ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c2, "tz'u", 'en')
print(fr)
# exec(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(fr, 'en', 'fr'))
print(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c2, 'ار', 'en'))
print(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c2, 'த', 'en'))
print(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c2, 'हिं', 'en'))
print(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c2, '汉', 'en'))


