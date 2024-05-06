from setuptools import setup, find_packages

# bitte ändern ♥

setup(
    name="hsmm",
    version="0.0.0.1",
    author="Tim16-sys - Kartoffel096 - HilkopterBob",
    description="Wer das ließt kann lesen,",
    packages=find_packages(),
    #data_files=[('conf', ['.conf/items.json', 'entities,json', "levels.json", "effects.json"])]
    include_package_data=True,
    package_data={'hsmm': ['conf/*.json']}
)
