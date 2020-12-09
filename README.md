# Chase

Chase appliaction.

### Description

The program implements simulations in which the wolf catches sheep.

### Authors
- Bartłomiej Małkowski
- Michał Bitnerowski

### TUL

This task is implemented for 'Python programming' subject.

### Academic year

2020/2021

### License

MIT License

#### Instruction to task three.

##### Create package:

- Create setup.py file with configuration of package
- Run setuptool command: 
```python setup.py sdist bdist_wheel```

##### Create virtual environment

- Run command to create venv: 
```python -m venv venv_name```
- Activate venv: 
```.\venv_name\Scripts\activate```

##### Install package in virtual environment

- Install our package: 
```pip install dist\package_name.whl --force-reinstall```
- Use --force-reinstall option if you install new package with the same version.
- Import package: 
```import package_name```

##### Run console application in virtual environment.

- Run command: 
```python -m chase [ARGS]```
