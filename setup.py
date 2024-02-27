from setuptools import setup, find_packages

setup(
    name='axiom-logger',
    version='0.1',
    packages=find_packages(),
    description='Axiom logging wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mark Zakelj',
    author_email='markzakelj@gmail.com',
    url='https://github.com/katalist-ai/axiom-logger',
    install_requires=[
        'axiom-py==0.3.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
