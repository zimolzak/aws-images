Make a website of images
========================

Very ad-hoc things for manipulating photos among a group of AWS EC3
instances, and/or generating stuff (list of files, index.html)
locally. Expects to have the JPG files in same directory so it can
list them (don't assume they're all numbered sequentially or whatever,
just get their filenames).

Usage
--------

1. _locally:_ `python3 publicize.py`
2. _locally:_ `make`
3. _remotely (for example):_ `python3 resizer.py 2 4`
4. _locally:_ whatever it takes to make index.html
