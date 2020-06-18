'''
Created on 28 Dec 2019

@author: Nathan
'''

def gen123():
    yield 1
    yield 2
    yield 3
    

def gen246():
    print("about to yeild 2")
    yield 2
    print("about to yeild 4")
    yield 4
    print("about to yeild 6")
    yield 6
    print("about to return")
    
    
def main():
    for v in gen123():
        print(v)
        
    g = gen246()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
      
if __name__ == '__main__':
    main()