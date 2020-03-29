import os

cnt = 0

for f in os.listdir("datasets/dataset"):
    cnt += 1

print(cnt)