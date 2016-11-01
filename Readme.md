Make a website of images
========================

Very ad-hoc things for manipulating photos among a group of AWS EC3
instances, and/or generating stuff (list of files, index.html)
locally. Expects to have the JPG files in same directory so it can
list them (don't assume they're all numbered sequentially or whatever,
just get their filenames). Because I don't know a ton about DevOps.

Usage
--------

All commands are run locally (not on the EC2 instances) unless
specified.

1. `python3 publicize.py` (this is unrelated ad-hoc stuff to fix some
   file permissions).
2. `make jpgs.txt`
3. commit jpgs.txt & push to git repo
4. _remotely:_ clone the git repo
5. _remotely:_ `aws configure` and enter keys w/ S3 permissions.
6. _remotely (for example):_ `sudo python3 resizer.py 2 4`
7. `make public_thumbnails`
8. whatever it takes to make index.html
