import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    name="timer",

    version="1.0.0",

    author="Dylan Ngo",

    author_email="it.tinhngo@gmail.com",

    description="Help people get away from the computer",

    url="https://github.com/dylanops/timer.git",

    license_files='LICENSE.txt',

    packages=setuptools.find_packages(),

    install_requires=[
        'setuptools',
        'build==0.10.0',
        'rich==13.4.2'
    ],

    python_requires='>=3.6',

    py_modules=['timer'],

    entry_points={
        'console_scripts': [
            "timer=timer:main",
        ],
    },
)
