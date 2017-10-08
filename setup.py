from __future__ import print_function
''' Setup / installation script '''

try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.command.install import install

import os
import subprocess


def abspath(path):
    """A method to determine absolute path
    for a relative path inside project's directory."""

    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))


class recrep_install(install):

    def run(self):

        install.run(self)

        man_dir = abspath("./man_pages/")

        cmd = subprocess.Popen([os.path.join(man_dir, "install.sh")],
                               stdout=subprocess.PIPE,
                               cwd=man_dir,
                               universal_newlines=True,
                               env=dict({"PREFIX": self.prefix},
                                        **dict(os.environ)))
        output = cmd.communicate()[0]
        print(output)


setup(
    # metadata
    name='recrep',
    description='Recursively replace text',
    license='MIT',
    version='0.1',
    author='James Powell',
    author_email='james@webscalability.com',
    url='https://github.com/jamespo/recrep',
    platforms='Cross Platform',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
        'setuptools',
    ],
    python_requires='>=3.3.*, <4',
    keywords=['searching', 'file system', 'text replacement'],
    packages=['recrep'],
    entry_points={
        'console_scripts': ['recrep = recrep.recrep:main'],
    },
    cmdclass={"install": recrep_install}
)
