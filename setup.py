import os
import sys

from distutils.core import setup
from distutils import util

if __name__ == "__main__":
    path_to_parser = util.convert_path('reelay/parser')
    path_to_pandas = util.convert_path('reelay/parser')
    setup ( name = 'reelay',
            version='0.0.2',
            author='Dogan Ulus',
            author_email='doganulus@gmail.com',
            url='http://github.com/doganulus/reelay/',
            package_dir = {
                'reelay': 'reelay',
                'reelay.parser': path_to_parser,
                'reelay.parser': path_to_pandas},
            packages=[
                "reelay",
                "reelay.parser",
                "reelay.pandas" 
            ],
            scripts=['bin/re2cpp'],
            license='GPLv3+',
            classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'Topic :: Scientific/Engineering',
                'Topic :: Scientific/Engineering :: Mathematics',
                'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                'Programming Language :: Python :: 3',
            ],
            description = 'An experimental package to generate sequential machines from formal specifications such as regular expressions',
            # url='http://pypi.python.org/pypi/reelay/',
            # py_modules = ["reelay.classical"],
            python_requires='>=3',
            install_requires=[
                'pandas',
                'antlr4-python3-runtime'
            ],
            include_package_data=True,
    )

