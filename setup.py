# -*- coding: utf-8 -*-

"""
Zenity setup script.
"""
__doc__="""zenity - display dialogs with python
DESCRIPTION
zenity  is a Python library that will display GTK+ dialogs using zanity 
tool, and return (eitherin the return code, or on standard output) the 
users input. This allows you to present information, and ask for infor
mation from the user.

For example, zenity.show(zenity.question) will return either 0, 1 or 5,  depending
on  whether  the  user  pressed OK, Cancel or timeout has been reached.
zenity.show(zenity.entry) will output on standard output what the user typed  into
the text entry field.
Comprehensive documentation is coming soon.

ENVIRONMENT
Normally, zenity detects the window from which it was launched
and keeps itself above that window.  This behavior can be  disabled  by
unsetting the WINDOWID environment variable.

AUTHOR
Original Zenity was written by Glynn Foster <glynn.foster@sun.com>.
This tool is written by Kavindu Santhusa <kavindusanthusa@gmail.com>
"""

try:
    from setuptools import setup # noqa, analysis:ignore
except ImportError:
    print("please install setuptools\npython -m pip install setuptools\nor\npython -m pip install setuptools")
    raise ImportError()


# Define name and description
name = 'Zenity'
description = "lightweight and full featured library to display dialogs with python."

## Setup

setup(
    name=name,
    version='1.0.0',
    author='Kavindu Santhusa',
    author_email='kavindusanthusa@gmail.com',
    license='MIT',
    url='https://github.com/Ksengine/Zenity',
    download_url='https://pypi.python.org/pypi/Zenity',
    keywords="GUI, dialog, lightweight, full, featured, full-featured," 
             +"library, to,display dialogs, display dialog, dialogs, python",
    description=description,
    long_description=__doc__,
    platforms='any',
    provides=[name],
    install_requires=[],
    py_modules=['zenity'],
    scripts=['zenity.py'],
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3',
        
    ],
)
