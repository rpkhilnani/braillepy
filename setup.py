from setuptools import setup, find_packages

setup(
    name="Roshan Khilnani",
    version="202407-1",
    description="A library to convert text to Braille",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Roshan Khilnani",
    author_email="rpkhilnani@yahoo.in",
    url="https://github.com/rpkhilnani/braillepy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL Version 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
