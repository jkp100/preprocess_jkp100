import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='preprocess_jkp100',
    version='0.0.1',
    author='Johnny Panasy',
    author_email='johnnypanasy@gmail.com',  # Enclose the email in single or double quotes
    description='This is a complete preprocessing package',  # Added 'a' before 'complete'
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',  # Corrected the syntax error
    ],
    python_requires='>=3.5',  # Removed the trailing comma
)

