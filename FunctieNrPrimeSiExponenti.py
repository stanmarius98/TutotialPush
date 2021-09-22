import math
def nrprim(n):
    print("Numarul",n,"este compus din urmatoarele numere prime:")

    # in p salvam valoarea exponentilor factorilor primi din care este compus numarul
    p = 0
    #incercam prima oara cu 2
    while (n > 0 and n % 2 ==0):
        p+=1
        n=n/2
    if p>0:
        print("2 ^" , p , end=" * ")
    #reinitializam p cu 0 ca sa incercam si cu alte numere prime
    p=0
    #dupa impartirile la 2 numarul trebuie sa fie impar, deci pornim de la 3 cu un pas de 2
    for i in range(3 , int(math.sqrt(n))+1 , 2):
        while n>0 and n % i==0:
            p+=1
            n = n/i
            #daca gasim un divizor prim al lui n atunci p o sa creasca cu 1
            #daca p este mai mare ca 1 afisam divizorul prim si exponentul acestuia
        if (p > 0):
            print(i , "^" , p , end=" * ")
        p=0
    #daca  n este mai mare ca 2 inseamna ca este numar prim si se divize doar prin el si il afisam
    if n > 2 :
        print (n,"^ 1")
    print()
nrprim(131)
nrprim(574)
nrprim(2880)
