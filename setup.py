from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ariad",
    version="0.0.1",
    author="Daniel Alves Rosel",
    author_email="daniel@alves.world",
    description="A short description of your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/velocitatem/ariad",
    py_modules=["ariad"],  # Use py_modules instead of packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'ariad=ariad:main',  # Point to the main function in ariad.py
        ],
    },
)