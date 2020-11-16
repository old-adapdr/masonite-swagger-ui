from setuptools import setup, find_packages

setup(
    name='masonite-swagger-ui',
    version='0.0.2',
    package_dir={'': 'src/'},
    description='Swagger-UI package for Masonite',
    long_description='Swagger-UI package for Masonite',
    url='https://github.com/alexpdr/masonite-swagger-ui',
    author='Alex Pedersen',
    author_email='me@alexpdr.dev',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='masonie api openapi swagger swagger-ui',
    packages=find_packages(
        where='src/'
    ),
    extras_require={
        'test': ['coverage', 'pytest'],
    },
)
