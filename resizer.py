# usage: sudo python resizer.py 3 4
#        sudo python resider.py 3 4 dry
# (for worker node 3 of 4)

from subprocess import check_output
from sys import argv
from time import time

for a in argv:
    if a == 'dry':
        def check_output(x):
            print(x)

ts = time()

## install needed things
image = 'apt-get -y install imagemagick'
cli = 'apt -y install awscli'
check_output(image.split())
check_output(cli.split())

## setup which jpgs to operate on
myid = int(argv[1])
maxid = int(argv[2])
J = open('jpgs.txt').read().splitlines()
n = len(J)
n_per_worker = n / float(maxid)
offset = (myid - 1) * n_per_worker

start = int(round(offset))
end = int(round(offset + n_per_worker))
Js = J[start:end]


## Operate on each file.

print('\nDownloading...')
for f in Js:
    check_output(['curl', '-O',
                  'https://s3.amazonaws.com/poland-card1/' + f])

print('\nResizing...')
t0 = time()
for f in Js:
    fnew = f.replace('.JPG', '_t.JPG')
    check_output(['convert', f, '-resize', '4%', fnew])
t1 = time()
print()
print('Resize took', t1 - t0, 'sec =',
      round((t1 - t0) / 60.0, 1), 'min.')

print('\nUploading...')
for f in Js:
    fnew = f.replace('.JPG', '_t.JPG')
    S = 'aws s3 cp FILE s3://poland-card1/FILE'
    S = S.replace('FILE', fnew)
    check_output(S.split())

te = time()

print()
print('Again, resize took', t1 - t0, 'sec =',
      round((t1 - t0) / 60.0, 1), 'min.')
print('Whole thing took', te - ts, 'sec =',
      round((te - ts) / 60.0, 1), 'min.')
