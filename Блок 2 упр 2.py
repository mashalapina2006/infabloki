Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = [0, 1, 2, 3]
>>> L[4]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    L[4]
IndexError: list index out of range
>>> L[-1000:100]
[0, 1, 2, 3]
>>> L[3:1]
[]
>>> L[3:1] = ['?']
>>> L
[0, 1, 2, '?', 3]
>>> L[10:] = [5]
