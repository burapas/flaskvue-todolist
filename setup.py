from setuptools import setup, find_packages

setup(
    version="0.1.0",
    name="tiny_flask", 
    description="",
    packages=find_packages(),
    install_requires=["flask", "peewee", "flask-cors"],
    tests_require=["pytest"],
)