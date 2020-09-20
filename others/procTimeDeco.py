from collections import deque
import time

def proc_time(main):
    def deco(*args, **kwargs):
        ts = time.time()
        result = main(*args, **kwargs)
        elapsed = time.time() - ts
        print("Running time : {}".format(elapsed))
        return result
    return deco

@proc_time
def main(d):
    d.popleft()

n = int(input("Enter: "))
a = [k for k in range(n)]
d = deque(a)
print(id(d), id(d[0]))
d.popleft()
print(id(d), id(d[0]))

    