from multiprocessing import Pool

def f(x):
    print 'cal ', x
    return x * x
def callback1(arg):
    print arg
    print 'result ready, in callback'

if __name__ == '__main__':
    pool = Pool (processes =4)
    result = pool.apply_async(f, [10], callback=callback1)
    #result = pool.apply_async(f, [10])
    print 'go on with sth else'
    print result.get(timeout=1)
    print pool.map(f, range(10))
