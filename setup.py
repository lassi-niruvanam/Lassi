import os

from setuptools import setup, find_packages

directorio = os.path.split(os.path.realpath(__file__))[0]

with open(os.path.join(directorio, 'lassi', 'ਸੰਸਕਰਣ.txt')) as archivo_versión:
    versión = archivo_versión.read().strip()

setup(
    name='lassi',
    version=versión,
    packages=find_packages(),
    url='https://lassi.readthedocs.io',
    download_url='https://github.com/julienmalard/Tinamit',
    license='GNU GPL 3',
    author='Julien Malard',
    author_email='julien.malard@mail.mcgill.ca',
    description='ਕੂਟਨ ਦੀ ਅਨੁਵਾਦ।',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    package_data={
        # Incluir estos documentos de los paquetes:
        '': ['*.txt', '*.json'],
    }
)
