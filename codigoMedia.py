nome = input("Digite o nome do aluno: ") #escolhemos o nome do aluno

nota1 = float(input("Digite a primeira nota do aluno: ")) #colocamos a nota1 do aluno
nota2 = float(input("Digite a segunda nota do aluno: ")) #colocamos a nota2 do aluno
nota3 = float(input("Digite a terceira nota do aluno: ")) #colocamos a nota3 do aluno

media = (nota1 + nota2 + nota3)/3 #o  calculo que será feito

print(f"A média do aluno é: {media:.2f}") #f serve para inserir a variavel no programa
#o segundo e f e para andar as casas de vírgula



if media >= 9:    print("Aluno aprovado!")

elif media >= 7: print("Passou raspando")

else:    print("Aluno reprovado!") #feito com ajuda
