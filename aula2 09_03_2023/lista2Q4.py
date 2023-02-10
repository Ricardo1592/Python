# Ler o nome completo do usuário e mostrar o primeiro e último de forma maiúscula

nomeCompleto=input("Digite seu nome completo:")
print(nomeCompleto)
nomeLista= nomeCompleto.split(" ")
nome=nomeLista[0]
sobrenome=nomeLista[-1]
print(nome.upper(), sobrenome.upper())