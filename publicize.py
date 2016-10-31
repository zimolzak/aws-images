from subprocess import check_output

base = "aws s3api put-object-acl --bucket poland-card1 --key IMG_XXXX.JPG --acl public-read"

#for i in range(2333, 3407):
#for i in range(2584, 3407):
#for i in range(2799, 3407):
#for i in range(3108, 3407):
#for i in range(3165, 3407):
for i in range(3170, 3407):
    S = base.replace("XXXX", str(i))
    print(S)
    check_output(S.split())
