import sys
sys.setrecursionlimit(10010)
#Cambiamos el limite de recursion.


def fibonacciRecursivo(n):
    if ( n == 0 ) or ( n == 1 ):
        return 1
    
    return fibonacciRecursivo( n - 1 ) + fibonacciRecursivo( n - 2 )


def fibonacciDinamico( n, memo = {} ):
    
    if ( n == 0 ) or ( n == 1 ):
        return 1
    
    try: 
        return memo[n]
    except KeyError:
        res = fibonacciDinamico( n - 1, memo ) + fibonacciDinamico( n - 2, memo )   
        memo[n] = res
        return res    

    
    


if __name__ == '__main__':
    
    n = int(input('Escoge un numero: '))
    
    res = fibonacciDinamico(n)
    
    print(res)