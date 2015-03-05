from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ninfo-plugin-mhr',
    version=version,
    description="CYMRU Malware Hash Registry",
    keywords='cymru mhr',
    author='Justin Azoff',
    author_email='jazoff@illinois.edu',
    url='',
    license='',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo",
    ],
    entry_points = {
        'ninfo.plugin': [
            'mhr    =   ninfo_plugin_mhr'
        ]
    }
) 
