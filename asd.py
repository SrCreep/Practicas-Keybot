lista=[]
lista_2=[]
def friend(x):
    for nombre in lista:
    	if len(nombre) == 4:
    		lista_2.append(nombre)
    return lista_2
            

friend(lista)