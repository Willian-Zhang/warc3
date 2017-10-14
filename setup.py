#! /usr/bin/env python

from setuptools import setup

setup(
    name="warc3-wet",
    version="0.2.2-wet",
    description="Python library to work with ARC and WARC files",
    long_description=open('Readme.rst').read(),
    license='GPLv2',
    author="Internet Archive",
    author_email="info@archive.org",
    url="https://github.com/Willian-Zhang/warc3",
    download_url = 'https://github.com/Willian-Zhang/warc3/archive/0.2.2-wet.tar.gz', 
    packages=["warc"],
    platforms=["any"],
    package_data={'': ["LICENSE", "Readme.rst"]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
