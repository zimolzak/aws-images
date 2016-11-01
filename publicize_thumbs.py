from subprocess import check_output

base = "aws s3api put-object-acl --bucket poland-card1 --key XXXX --acl public-read"

J = open('thumb_in_prog.txt').read().splitlines()

for f in J:
    fnew = f.replace('.JPG', '_t.JPG')
    S = base.replace("XXXX", fnew)
    print(S)
    print(check_output(S.split()))
