import setuptools

with open('README', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='bomradarloop',
    version='0.1.0',
    author='Paul Madden',
    author_email='maddenp@colorado.edu',
    description='Create animated GIFs from BOM radar imagery',
    install_requires=['Pillow', 'requests'],
    long_description=long_description,
    url='https://github.com/maddenp/bomradarloop',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
