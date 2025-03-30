Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2 ** 16
65536
2 / 5, 2 / 5.0
(0.4, 0.4)
"spam" + "eggs"
'spameggs'
>>> S = "ham"
>>> "eggs " + S
'eggs ham'
>>> S * 5
'hamhamhamhamham'
>>> S[:0]
''
>>> "green %s and %s" % ("eggs", S)
'green eggs and ham'
>>> "green {0} and {1}".format("eggs", S)
'green eggs and ham'
>>> ('x',) [0]
'x'
>>> ('x', 'y') [1]
'y'
>>> L = [1,2,3] + [4,5,6]
>>> L, L[:], L[:0], L[-2], L[-2:]
([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [], 5, [5, 6])
>>> ([1,2,3] + [4,5,6]) [2:4]
[3, 4]
>>> [L[2], L[3]]
[3, 4]
>>> L.reverse(); L
[6, 5, 4, 3, 2, 1]
>>> L.sort(); L
[1, 2, 3, 4, 5, 6]
>>> L.index(4)
3
>>> {"a":1, "b":2}["b"]
2
>>> D = {'x':1, 'y':2, 'z': 3}
>>> D [" w " ] = 0
>>> D["x"] + D[" w "]
1
>>> D[(1,2,3)] = 4
>>> list(D.keys()), list(D.values ()) , (1,2,3) in D
(['x', 'y', 'z', ' w ', (1, 2, 3)], [1, 2, 3, 0, 4], True)
>>> [[]], ["", (),{},None]
([[]], ['', (), {}, None])
