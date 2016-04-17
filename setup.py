# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

REQUIREMENTS = [i.strip() for i in open("REQUIREMENTS").readlines()]
# LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
LONG_DESCRIPTION = ''

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache 2.0',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Telepenin Nikolay",
    author_email="telepenin.nikolay@gmail.com",
    maintainer='Telepenin Nikolay',
    maintainer_email="telepenin.nikolay@gmail.com",
    name='todomvc-django',
    version='0.1',
    description='TODO samples',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/prefer/todomvc-django',
    license='Apache 2.0',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=False
)
