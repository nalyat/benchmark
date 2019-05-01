from setuptools import setup

from benchmark import __VERSION__, __URL__, __maintainer__, __email__

setup(
    name='benchmark',
    version=__VERSION__,
    url=__URL__,
    license='LICENSE.txt',
    author=__maintainer__,
    author_email=__email__,
    description='Python benchmarker / benchmarking framework',
    long_description=open('README.md').read(),
    packages=['benchmark'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Benchmark",
    ]
)
