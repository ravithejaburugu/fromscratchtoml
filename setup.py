''' Installation script for python fromscratchtoml package'''

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

linux_testenv = [
    'pytest-cov',
    'python-coveralls',
]

setup(
    name='fromscratchtoml',
    version='0.0.1',
    description=' An intuitive machine learning library for python.',

    install_requires=install_requires,
    extras_require={
        'test': linux_testenv,
        'docs': ['jupyter', 'Flask>=0.10.1', 'Jinja2>=2.7', 'MarkupSafe>=0.18', 'Werkzeug>=0.9.1',
'               itsdangerous>=0.22', 'flask-flatpages', 'frozen-flask', 'flask-assets']
    },
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/jellAIfish/fromscratchtoml',
    license='GPL-3.0',
    packages=find_packages(),
)
