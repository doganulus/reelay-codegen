import os
import sys

from os.path import join

from distutils.core import setup
from distutils import util

# class build_ext(build_ext):

#     def build_extension(self, ext):
#         self._ctypes = isinstance(ext, CTypes)
#         return super().build_extension(ext)

#     def get_export_symbols(self, ext):
#         if self._ctypes:
#             return ext.export_symbols
#         return super().get_export_symbols(ext)

#     def get_ext_filename(self, ext_name):
#         if self._ctypes:
#             return ext_name + '.so'
#         return super().get_ext_filename(ext_name)

# class CTypes(Extension): pass

# module1 = CTypes('libmontre',
#             define_macros = [ ('MAJOR_VERSION', '0'),
#                               ('MINOR_VERSION', '6')],
#             sources = [ join("src", "libmontre", "zone2.cpp"),
#                         join("src", "libmontre", "zoneset.cpp"),
#                         join("src", "libmontre", "boolean.cpp"),
#                         join("src", "libmontre", "interval.cpp"),
#                         join("src", "libmontre", "temporal.cpp")
# ],
#             depends = [ join("src", "libmontre", "zone2.h"),
#                         join("src", "libmontre", "zoneset.h"),
#                         join("src", "libmontre", "boolean.h"),
#                         join("src", "libmontre", "interval.h"),
#                         join("src", "libmontre", "temporal.h")
# ],
#             include_dirs=[join("src", "libmontre")],
#             extra_compile_args=['-std=c++11'])
if __name__ == "__main__":
    path_to_grammar = util.convert_path('reelay/parser')
    setup ( name = 'reelay',
            version='0.0.1',
            author='Dogan Ulus',
            author_email='doganulus@gmail.com',
            url='http://github.com/doganulus/reelay/',
            package_dir = {
                'reelay': 'reelay',
                'reelay.parser': path_to_grammar},
            packages=[
                "reelay",
                "reelay.parser" 
            ],
            scripts=['bin/reelay'],
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
            description = 'A package to generate sequential machines from regular expressions',
            # url='http://pypi.python.org/pypi/reelay/',
            # py_modules = ["reelay.classical"],
            python_requires='>=3',
            install_requires=[
                'antlr4-python3-runtime',
            ],
            include_package_data=True,
    )

