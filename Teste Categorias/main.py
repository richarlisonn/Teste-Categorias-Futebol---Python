nome = input ("Digite seu nome: ")
print ("Olá",nome)
idade = int (input ("Digite sua idade: "))
print ("Prazer",nome, "Você tem", idade,"anos")


if idade == 17:
    print ("Sua Categoria é Sub 17")
elif idade == 18:
    print ("Sua categoria é Sub 18")
elif idade == 19:
    print ("Sua categoria é Sub 19")
elif idade == 20:
    print ("Sua categoria é Profissional")