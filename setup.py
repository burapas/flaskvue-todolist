from setuptools import setup, find_packages

setup(
    version="0.1.0",
    name="tiny_flask", 
    description="",
    packages=find_packages(),
    install_requires=["flask", "peewee"],
    tests_require=["pytest"],
)