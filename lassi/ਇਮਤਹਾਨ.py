from lassi.ਕੂਟਨ.ਪੈਧਾਨ import ਕੂਟਨ_ਪੈਧਾਨ
import pprint


ਨਮੁਨਹ = ਕੂਟਨ_ਪੈਧਾਨ(ਕੂਟਨ_ਨਾਮ='tinamit', ਖੁਦ_ਜ਼ਬਾਨ='español', ਰਾਸ੍ਤਾ='C:\\Users\\USERS1\PycharmProjects\Tinamit',
                   ign=['Interfaz', 'NuevoInterfaz', 'Incertidumbre', 'Ejemplos', 'Stella.py'],
                   ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼='trads')


pprint.pprint(ਨਮੁਨਹ.ਕੋਸ਼, indent=2)

ਨਮੁਨਹ.gén_dict_trads()

ਨਮੁਨਹ.ajouter_langue('தமிழ்')
ਨਮੁਨਹ.ajouter_langue('اردو')
ਨਮੁਨਹ.écire_dic_pour_trad()

for x, d in ਨਮੁਨਹ.ਕੋਸ਼_ਅਨੁ.items():
    if d['español'] == 'símismo':
        d['தமிழ்'] = 'தாங்கள்'
        d['اردو'] = 'خود'

ਨਮੁਨਹ.ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਜ਼ਬਾਨ='தமிழ்')
ਨਮੁਨਹ.ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਜ਼ਬਾਨ='اردو')