from setuptools import setup, find_packages


def requirements() -> list:
    return [
        'click==6.7',
        'curio==0.8',
    ]


setup(
    name='udptest',
    version='0.1.0',
    description='UDP benchmarking/testing tool.',
    long_description=open('README.rst').read(),
    url='https://github.com/povilasb/httpmeter',
    author='Povilas Balciunas',
    author_email='balciunas90@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests')),
    entry_points={
        'console_scripts': [
            'udptestd = udptest.server:main',
            'udptest = udptest.client:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Development Status :: 3 - Alpha',
        'Topic :: System :: Networking',
        'Topic :: Internet :: UDP',
    ],
    install_requires=requirements(),
)
