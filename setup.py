import os
import sys

from setuptools import setup

if __name__ == "__main__":

    setup ( name = 'reelay',
            version='0.1.0',
            author='Dogan Ulus',
            author_email='doganulus@gmail.com',
            url='http://github.com/doganulus/reelay/',
            packages=[
                "reelay",
                "reelay.parser",
                "reelay.target",
                "reelay.machine",
                "reelay.formal" 
            ],
            scripts=['scripts/re2cpp', 'scripts/tl2cpp'],
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
            description = 'Reelay is a code generator from high-level patterns for monitoring, inspecting, and analyzing sequential data.',
            # url='http://pypi.python.org/pypi/reelay/',
            python_requires='>=3',
            install_requires=[
                'antlr4-python3-runtime'
            ],
            include_package_data=True,
            package_data={
                '': ['cpp/*.h'],
                '': ['cpp/*.hpp']
            },
            eager_resources = ['cpp/common.hpp', 'cpp/discrete_time.hpp']
    )

