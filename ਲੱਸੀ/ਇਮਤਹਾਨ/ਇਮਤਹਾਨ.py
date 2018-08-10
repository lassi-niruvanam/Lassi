from ਲੱਸੀ.ਵਾਧਾ.ਪੈਧਾਨ_੩ import ਪੈਧਾਨ_੩_ਵਿਆ

ਵਿਆ = ਪੈਧਾਨ_੩_ਵਿਆ()
ਵਿਆ.actualizar_trads(['த', 'ગુ', 'ਪੰ', 'हिं', 'fr', 'kaq', 'ار', 'فا', '汉'])
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


fr = ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c, 'fr', 'en')
print(fr)
# exec(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(fr, 'en', 'fr'))
print(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c, 'ار', 'en'))
print(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c, 'த', 'en'))
print(ਵਿਆ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(c, '汉', 'en'))
# ਪੈਧਾਨ_੩_ਵਿਆ().traduire_document('c.py', 'ار', 'en')