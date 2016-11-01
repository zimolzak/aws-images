Make a website of images
========================

Ad-hoc scripts for using a group of AWS EC3 instances to resize photos
in parallel. Also for some local operations (change S3 file
permissions, generate index.html). This exists because I don't know a
ton about DevOps. The makefile expects to have IMG_1234.JPG files in
the same directory as itself, so it can list them (doesn't assume
they're all numbered sequentially, just gets their filenames).

Usage
--------

All commands are run locally (not on the EC2 instances) unless
specified. If it says _Remotely:_, that means run that command on
_each_ EC2 instance, where `resizer.py 2 4` means "You are EC2
instance 2 of 4."

1. `python3 publicize.py` (this is unrelated ad-hoc stuff to fix some
   file permissions).
2. `make jpgs.txt`
3. Commit jpgs.txt & push to git repo.
4. _Remotely:_ clone the git repo
5. _Remotely:_ `aws configure` and enter keys w/ S3 permissions.
6. _Remotely (for example):_ `sudo python3 resizer.py 2 4`
7. `make thumbnails_public`
8. `make index.html`
9. Upload index.html to AWS S3 bucket and setup static Web hosting as
   per usual.
