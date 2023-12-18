Atleta = input("Nome do Atleta: ")


saltos = []


for i in range(5):
    salto = float(input("Insira o valor do salto: "))

    saltos.append(salto)

lista = ["Primeiro Salto: ", "Segundo salto: ", "Teceiro Salto: ", "Quarto Salto: ", "Quinto Salto: "]

print(f"Nome do Atleta: {Atleta} ")
for i in range(len(lista)):
    print(f" {lista[i]} {saltos[i]}")

# Convertendo os saltos para strings e formatando-os
saltos_formatados = [f"{salto:.1f}" for salto in saltos]

# Criando a string final
resultado = "Saltos: " + " - ".join(saltos_formatados)

media = sum(saltos) / len(saltos)
media_arredondada = round(media, 2)
print( "\n" "Resultado Final: ")
print(f"Atleta: {Atleta} \n  {resultado} \n Média: {media_arredondada}")