from setuptools import setup, find_packages


def readme():
    with open('README.md') as r:
        return r.read()


setup(
    name="chase",
    version="0.7",
    description="Chase simulation with wolf and sheep.",
    long_description=readme(),
    author="Bartłomiej Małkowski and Michał Bitnerowski",
    packages=find_packages(),
    install_requires=[],
    license="MIT",
    include_package_data=True,
    url="https://github.com/maalekkk/Wolf-and-sheep-simulation"
)
