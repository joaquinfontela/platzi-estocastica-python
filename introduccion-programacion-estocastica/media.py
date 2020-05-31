import random

def media(X):
    # Calcula la media de los valores de X.
    return ( sum(X) / len(X) )


if __name__ == "__main__":

    X = [ random.randint( 1, 20+1 ) for i in range(20) ]
    #genera un array con 20 valores entre el 1 y el 20
    mu = media(X)
    
    print(X)
    print(mu)
