#calculadora de Aprovação Escolar 

nome = input("Digite o nome do estudante: ")

soma_notas = 0

quantidade_trimestre = 3

media_aprovacao = 180

#coleta as notas dos trimestres

for i in range (1, quantidade_trimestre + 1):
    nota = float (input("Informe a nota{i}º período: "))
    soma_notas += nota 

print("-" * 30)

print(f"Estudante: {nome}")

print(f"Pontuação Total: {soma_notas}")

#Verificação a Status de aprovação

if soma_notas >= media_aprovacao:
    print("Status: APROVADO! Parabens!!")
else:
    pontos_faltantes = media_aprovacao - soma_notas
    print("Status: TENTE OUTRA VEZ!! ")
    print(f"Faltaram {pontos_faltantes} pontos para atingir o mínimo de {media_aprovacao}.")
