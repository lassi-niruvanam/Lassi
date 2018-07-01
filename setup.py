import os

from setuptools import setup, find_packages

ਰਾਸ੍ਤਾ = os.path.split(os.path.realpath(__file__))[0]

with open(os.path.join(ਰਾਸ੍ਤਾ, 'ਲੱਸੀ', 'ਸੰਸਕਰਣ.txt')) as ਸੰਸਕਰਣ_ਦਸ੍ਤਾਵੇਜ਼:
    ਸੰਸਕਰਣ = ਸੰਸਕਰਣ_ਦਸ੍ਤਾਵੇਜ਼.read().strip()

setup(
    name='lassi',
    version=ਸੰਸਕਰਣ,
    packages=find_packages('ਲੱਸੀ'),
    url='https://lassi.readthedocs.io',
    download_url='https://github.com/julienmalard/Lassi',
    license='GNU GPL 3',
    author='Julien Malard',
    author_email='julien.malard@mail.mcgill.ca',
    description='ਕੂਟਨ ਦੀ ਅਨੁਵਾਦ।',
    long_description='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    package_data={

        '': ['*.txt', '*.json'],
    }
)
