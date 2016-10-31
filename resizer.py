# usage: python resizer.py 3 4
# (for worker node 3 of 4)

from subprocess import check_output
from sys import argv

## install mogrify

aptget = 'apt-get install imagemagick'
#check_output(aptget.split())

## setup which jpgs to operate on

myid = int(argv[1])
maxid = int(argv[2])
J = open('jpgs.txt').readlines()
n = len(J)
n_per_worker = n / float(maxid)
offset = (myid - 1) * n_per_worker

start = int(round(offset))
end = int(round(offset + n_per_worker))
print(J[start:end])

## download files from s3



## resize using mogrify & output new



## upload to s3


