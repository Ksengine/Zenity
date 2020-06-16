# Zenity

zenity  is a Python library that will display GTK+ dialogs using zanity
 tool, and return (eitherin the return code, or on standard output) the
 users input. This allows you to present information, and ask for infor
mation from the user.

For example, zenity.show(zenity.question) will return either 0, 1 or 5,  depending
on  whether  the  user  pressed OK, Cancel or timeout has been reached.
zenity.show(zenity.entry) will output on standard output what the user typed  into
the text entry field.


## Example:
    
```py
import zenity

res,_ = zenity.show(zenity.question,text="Is it ok?")

if res:
    print("it's ok")
```


## Installation


`pip install zenity`


## License

MIT. See LICENSE for details.
