import os, re

from setuptools import setup, find_packages

VERSION_RE = re.compile(r'^(\d+\.\d+\.\d+)$')

with file('CHANGELOG') as changelog:
    for line in changelog.readlines():
        match = VERSION_RE.search(line)
        if match:
            version = match.group(1)
            break
    else:
        raise RuntimeError('Could not determine a valid version from changelog.')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='flv',
    version=version,
    description="Simple class-based view to enable querystring filtering for ListViews.",
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
    ],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['flv'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django>=1.3']
)
