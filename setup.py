from setuptools import setup, find_packages
import os

import pagepermissions


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author="Eric Brelsford",
    author_email="ebrelsford@gmail.com",
    name='feincms-pagepermissions',
    version=pagepermissions.__version__,
    description=('A simple FeinCMS extension that adds permission-checking to '
                 'a model.'),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/ebrelsford/feincms-pagepermissions/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.6.0',
        'FeinCMS>=1.9.0',
    ],
    packages=find_packages(),
    include_package_data=True,
)
