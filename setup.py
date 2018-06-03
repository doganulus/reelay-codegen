import os
import sys

from distutils.core import setup
from distutils import util

if __name__ == "__main__":

    setup ( name = 'reelay',
            version='0.1.0',
            author='Dogan Ulus',
            author_email='doganulus@gmail.com',
            url='http://github.com/doganulus/reelay/',
            package_dir = {
                'reelay': 'reelay',
                'reelay.parser': util.convert_path('reelay/parser'),
                'reelay.target': util.convert_path('reelay/target'),
                'reelay.machine': util.convert_path('reelay/machine')
                'reelay.formal': util.convert_path('reelay/formal')},
            packages=[
                "reelay",
                "reelay.parser",
                "reelay.target",
                "reelay.machine",
                "reelay.formal" 
            ],
            scripts=['scripts/reg2cpp', 'scripts/ptl2cpp'],
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
            description = 'Reelay is an online monitor generator from regular expressions and temporal logic based on sequential networks.',
            # url='http://pypi.python.org/pypi/reelay/',
            python_requires='>=3',
            install_requires=[
                'antlr4-python3-runtime'
            ],
            include_package_data=True,
    )

