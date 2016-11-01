stub = open('stub.html').read().splitlines()
jpgs = open('jpgs.txt').read().splitlines()

def num_only(s):
    return s.replace('IMG_', '').replace('.JPG', '')

jpgs = [num_only(f) for f in jpgs]

for L in stub:
    if not 'XXXX' in L:
        print(L)
    else:
        for n in jpgs:
            print(L.replace('XXXX', n))
