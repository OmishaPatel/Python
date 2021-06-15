import time
def scheduler(f,n):
    time.sleep(n)
    f()

def hello_world():
    print('helloworld')

scheduler(hello_world, 2)