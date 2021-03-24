import pathlib
import pkg_resources

from setuptools import setup

# https://stackoverflow.com/a/59971469
with pathlib.Path('requirements.txt').open() as requirements_txt:
    content = '\n'.join(filter(lambda line: not line.startswith('-i '), requirements_txt.read().split('\n')))
    install_requires = [
        str(requirement) for requirement in pkg_resources.parse_requirements(content)
    ]

setup(
    name='Flask-Boto3',
    version='0.3.2k',
    url='https://github.com/Ketouem/flask-boto3',
    license='MIT',
    author='Cyril "Ketouem" Thomas',
    author_email='ketouem@gmail.com',
    description='Flask extension that ties boto3 to the application',
    packages=['flask_boto3'],
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
    install_requires=install_requires,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
