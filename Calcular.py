nome = input("Digite seu nome: ")

print("Olá, %s! Vamos calcular quanto você precisa tirar no 4º bimestre para passar de ano direto." %(nome))

def nota_prim():
    while True:
        nota_pri = input("Qual foi sua média no 1º bimestre? ")
        if nota_pri.replace(".", "", 1).isdigit():
            nota_pri = float(nota_pri)
            if nota_pri >= 0 and nota_pri <= 10:
                break
            else:
                print("A nota deve ser entre 0 e 10. Se necessário, utilize um . (ponto) para separar casas decimais.")
        else:
            print("Por favor digite um número.")
    return nota_pri

def nota_segu():
    while True:
        nota_seg = input("Qual foi sua média no 2º bimestre? ")
        if nota_seg.replace(".", "", 1).isdigit():
            nota_seg = float(nota_seg)
            if nota_seg >= 0 and nota_seg <= 10:
                break
            else:
                print("A nota deve ser entre 0 e 10. Se necessário, utilize um . (ponto) para separar casas decimais.")
        else:
            print("Por favor digite um número.")
    return nota_seg

def nota_terc():
    while True:
        nota_ter = input("Qual foi sua média no 3º bimestre? ")
        if nota_ter.replace(".", "", 1).isdigit():
            nota_ter = float(nota_ter)
            if nota_ter >= 0 and nota_ter <= 10:
                break
            else:
                print("A nota deve ser entre 0 e 10. Se necessário, utilize um . (ponto) para separar casas decimais.")
        else:
            print("Por favor digite um número.")
    return nota_ter

primeiro = nota_prim()
segundo = nota_segu()
terceiro = nota_terc()

def soma():
  somei = primeiro + segundo + terceiro
  x = round(somei, 2)
  return x

total = soma() 

def diminuir():
  tirar = 28 - total
  y = round(tirar, 2)
  return y

precisa = diminuir()

def resulta():
  if 0 >= precisa:
    print(f"A soma de suas médias é de {total}. É necessário ter 28 pontos. Você já passou direto.")
  elif 10 < precisa:
    print(f"A soma de suas médias é de {total}. É necessário ter 28 pontos. Você precisaria tirar {precisa} no 4º bimestre. Você fará a prova final.")
  else:
    print(f"A soma de suas médias é de {total}. É necessário ter 28 pontos. Você precisa tirar {precisa} no 4º bimestre para passar direto.")
    
final = resulta()
