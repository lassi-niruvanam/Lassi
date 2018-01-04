from lassi.ਕਾਰ੍ਯਕ੍ਰਮ import créer_projet, ਕਾਰ੍ਯਕ੍ਰਮ
# import pprint
import os

chemin0 = 'C:\\Users\\USERS1\\PycharmProjects\\tinamit'
chemin = os.path.join(chemin0, '.config.json')
if os.path.isfile(chemin):
    ਨਮੁਨਹ = ਕਾਰ੍ਯਕ੍ਰਮ(chemin)
else:
    ਨਮੁਨਹ = créer_projet(chemin0, ਖੁਦ_ਜ਼ਬਾਨ='español', langues_cibles=['தமிழ்', 'اردو'], chemin_trads='trads',
                         ign=['Interfaz', 'NuevoInterfaz', 'Incertidumbre', 'Ejemplos', 'Stella.py'])

    # print.pprint(ਨਮੁਨਹ.struct, indent=2)

ਨਮੁਨਹ.actualiser()

ਨਮੁਨਹ.ajouter_langue('தமிழ்')
ਨਮੁਨਹ.ajouter_langue('اردو')

ਨਮੁਨਹ.sauvegarder()

ਨਮੁਨਹ.ਅਨੁਵਾਦ_ਲਿਖਣਾ()
