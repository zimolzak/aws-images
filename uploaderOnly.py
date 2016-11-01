from subprocess import check_output
from sys import argv
from time import time

for a in argv:
    if a == 'dry':
        def check_output(x):
            print(x)

ts = time()

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

print('\nUploading...')
for f in Js:
    fnew = f.replace('.JPG', '_t.JPG')
    S = 'aws s3 cp FILE s3://poland-card1/FILE'
    S = S.replace('FILE', fnew)
    check_output(S.split())

te = time()

print()
print('Whole thing took', te - ts, 'sec =',
      round((te - ts) / 60.0, 1), 'min.')
