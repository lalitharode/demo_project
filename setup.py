from setuptools import setup, find_packages

setup(
    name="census-income",
    version="0.0.1",
    author="lalit",
    author_email="lalitharode20141996@gmail.com",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "flask"]
)
