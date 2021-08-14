from setuptools import setup

setup(
    name='dashboard',
    version='0.1.0',
    description='OBD2 Honda dashboard.',
    url='https://github.com/shuds13/pyexample',
    author='Todor Todorov',
    author_email='todstoychev@gmail.com',
    license='BSD 2-clause',
    packages=['dashboard'],
    install_requires=['qtawesome',
                      'pyqt5',
                      'obd'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Car/Automotive',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)