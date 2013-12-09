srpp-travel
===========

example:
`time pypy src/__main__.py data_pro/1000_k\=50`

`for i in $(ls data_pro/ -type f); do (pypy src/__main__.py data_pro/$i > score/$i)&; done`