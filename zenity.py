"""Zenity - display dialogs with python

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
from __future__ import absolute_import, division
import subprocess
import os
import time
from sys import version_info
__version__ = '2.0.0'


#Application Options:
calendar       ="calendar"            #Display calendar dialog
entry          ="entry"               #Display text entry dialog
error          ="error"               #Display error dialog
info           ="info"                #Display info dialog
file_selection ="file-selection"      #Display file selection dialog
list           ="list"                #Display list dialog
notification   ="notification"        #Display notification
progress       ="progress"            #Display progress indication dialog
question       ="question"            #Display question dialog
warning        ="warning"             #Display warning dialog
scale          ="scale"               #Display scale dialog
text_info      ="text-info"           #Display text information dialog
color_selection="color-selection"     #Display color selection dialog
password       ="password"            #Display password dialog
forms          ="forms"               #Display forms dialog

class ZenityException(Exception):pass



def test_call(*args, **kwargs):
    """ Test whether a subprocess call succeeds.
    """
    try:
        subprocess.check_output(*args, **kwargs)
        return True
    except Exception:
        return False

def _message(args, writeable=False):
    def write(message=''):
        try:
            p.stdin.write(str(message) + '\n')
        except IOError as e:
            print(e)
            exit()
            return p.returncode
    env = os.environ.copy()
    env['WINDOWID'] = ''
    if writeable:
        p = subprocess.Popen(['zenity'] + args,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE,env=env)
        return write
    else:
        p = subprocess.Popen(['zenity'] + args,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE,env=env)
        try:
            while p.poll() is None:
                time.sleep(0.002)
            return not p.poll(), p.stdout.read().decode('utf-8', 'ignore')
        finally:
            if p.poll() is None:  # pragma: no cover
                p.kill()


def works():
    t = test_call(['zenity', '--version'])
    if t:
        return True
    try:
        from os import system
        system("sudo apt-get install zenity")
    except Exception as e:
        raise ZenityException("Zenity Not Working\nlog:\n"+e)
    return test_call(['zenity', 'def version'])

def show(*args,**kwargs):
    """show dialog"""
    w=False
    if works():
        flags_list=[]
        if "writeable" in kwargs:
            w=True
            del kwargs["writeable"]
        for kwarg in kwargs:
            flags_list.append("--"+kwarg+"=\""+str(kwargs[kwarg])+"\"")
        for arg in args:
            flags_list.append("--"+str(arg))
        if w:
            return _message(flags_list,writeable=True)
        return _message(flags_list)
    else:
        return False

def cli():
    import sys
    from os import system
    if works():
        system('zenity '+' '.join(sys.argv[1:]))

  
if __name__=='__main__':
    cli()
