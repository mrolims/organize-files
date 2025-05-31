from setuptools import setup, find_packages

setup(
    name='organize_files',
    version='0.1.0',
    description='Organize files in directories into categorized folders',
    author='Matheus Rolim Sales',
    author_email='rolim.sales.m@gmail.com',
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'organize-files=organize_files.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
