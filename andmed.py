




raamatud = list()

def menu():
    print("""

    1.Sisesta
    2.Märksõna
    3.Korv
    4.Eemalda
    
    """)

    kasutaja = input("Sisesta valikud:")
    user = kasutaja
    while True:
        if kasutaja == 'Sisesta':
            lisama()
            
        while kasutaja == 'Märksõna':
            märksõna()
            
        if kasutaja == 'Korv':
            korvis()
        while kasutaja == 'Eemalda':
            kustutama()                                       
        menu()

def kustutama():
    kasutaja = input("Kustutage raamat: ")
    raamatud.remove(kasutaja)
    menu()    

        

def märksõna():
    
    kasutaja = input("Sisesta raamatu märksõna: ")
    print(raamatud.keyword.kwlist)
    menu()

def lisama():
    
    while len(raamatud) + 6:
        raamat = input("Sisesta raamat:")
        raamatud.append(raamat)
        print("Lisasite korvi",raamatud)
        print("Teie korvis {}".format(raamatud))
        menu()
    if '' in raamatud:
            print("See raamat on juba olemas")

    menu()
             
    
def korvis():
    print("Sinu korvis on - ",raamatud)
    
menu()





        
    







    


       

