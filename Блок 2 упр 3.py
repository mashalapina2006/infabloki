Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = [0, 1, 2, 3]
>>> L[2] = []
>>> L
[0, 1, [], 3]
>>> L[2:3] = []
>>> L
[0, 1, 3]
>>> del L[0]
>>> L
[1, 3]
>>> del L[1:]
>>> L
[1]
>>> L = [0, 1, 2, 3]
>>> L[1:2] = 1
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    L[1:2] = 1
TypeError: must assign iterable to extended slice
>>> L[1:2] = [1]
>>> L
[0, 1, 2, 3]
