caractere=input()
frase=input()
frase=frase[:101]

letras=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
indice_letras=len(letras)
indice_frase=len(frase)
frase_nova= ''
for i in range(indice_frase):
    for j in range(indice_letras):
        if caractere=='R' and frase[i]==letras[j]:
            if frase[i]==letras[0]:
                frase1=frase[:i]
                frase2=frase[i+1:]
                frase_nova= frase_nova + "p"
            else:    
                frase1=frase[:i]
                frase2=frase[i+1:]
                frase_nova= frase_nova + letras[j-1]
        if caractere=='L' and frase[i]==letras[j]:
            if frase[i]==letras[-1]:
                frase1=frase[:i]
                frase2=frase[i+1:]
                frase_nova= frase_nova + letras[j+1]
            else:
                frase1=frase[:i]
                frase2=frase[i+1:]
                frase_nova= frase_nova + letras[j+1]

print(frase_nova)            

    