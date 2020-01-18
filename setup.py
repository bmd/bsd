import pip
from setuptools import setup, find_packages
from setuptools.command.install import install


package = 'bsdetector'
version = '0.1'


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        import nltk
        nltk.download('punkt')
        install.run(self)


setup(
    name=package,
    version=version,
    package_dir={'bsdetector': 'bsdetector'},
    package_data={'bsdetector': ['*.json', '*.txt']},
    packages=find_packages(),
    install_requires=[
        'pytest',
        'requests',
        'numpy',
        'scipy',
        'scikit-learn',
        'textstat',
        'future',
        'decorator',
        'decorators',
        'pattern @ https://github.com/NicolasBizzozzero/pattern/tarball/master#egg=pattern',
        'vaderSentiment',
    ],
    include_package_data=True,
    description="Detects biased statements in online media documents",
    url='url',
    cmdclass={
        'install': PostInstallCommand
    },
    entry_points={
        'console_scripts': [
            'bsdetector = bsdetector.__main__:main'
        ]
    }
)
