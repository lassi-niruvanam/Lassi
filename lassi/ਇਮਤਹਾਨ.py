from lassi.ਕਾਰ੍ਯਕ੍ਰਮ import ਕਰ੍ਯਕ੍ਰਮ_ਬਣਾਊ, ਕਾਰ੍ਯਕ੍ਰਮ
# import pprint
import os
import tinamit

chemin0 = os.path.split(tinamit.__file__)[0]
chemin2 = os.path.join(chemin0, 'trads', '.config.json')
if os.path.isfile(chemin2):
    ਨਮੁਨਹ = ਕਾਰ੍ਯਕ੍ਰਮ(chemin2)
else:
    ਨਮੁਨਹ = ਕਰ੍ਯਕ੍ਰਮ_ਬਣਾਊ(tinamit, ਖੁਦ_ਜ਼ਬਾਨ='español', langues_cibles=['தமிழ்', 'اردو'], chemin_trads='trads',
                          ign=['Interfaz', 'NuevoInterfaz', 'Incertidumbre', 'Ejemplos', 'Stella.py'])

    # print.pprint(ਨਮੁਨਹ.struct, indent=2)

ਨਮੁਨਹ.actualiser()


ਨਮੁਨਹ.sauvegarder()

ਨਮੁਨਹ.ਅਨੁਵਾਦ_ਲਿਖਣਾ()
