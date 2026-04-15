
nome=input('qual o seu nome:\n')
print(f'Seja Bem Vindo(a): {nome}')
print(f'hoje faremos um quiz sobre Informatica')
print(f'o resultado so sera dado ao final do quiz')
erros=[]
acertos=[]
contador_acertos=0
contador_erros=0
p1=input('1.O que significa CPU?\n a) Central Process Unit \n b) Central Processing Unit \n c) Computer Personal Unit \n d) Control Process Unit\n').lower()
if p1=='b':
    contador_acertos+=1
    acertos.append(f'1.{p1}')
    print('vamos para a proxima pergunta.')
else:
    contador_erros+=1
    erros.append(f'1.{p1}')
    print('vamos para a proxima pergunta:')

p2=input('2.Qual desses é um sistema operacional? \n a) Google \n b) Windows \n c) Intel \n d) Python\n').lower()
if p2=='b':
    contador_acertos+=1
    acertos.append(f'2.{p2}')
    print('vamos para a proxima questao.')
else:
    contador_erros+=1
    erros.append(f'2.{p2}')
    print('vamos para a proxima questao.')
p3=input('Qual dispositivo é usado para apontar na tela?\n a) Teclado \n b) Monitor \n c) Mouse \n d) Impressora\n').lower()
if p3=='c':
    contador_acertos+=1
    acertos.append(f'3.{p3}')
else:
    contador_erros+=1
    erros.append(f'3.{p3}')
p4=input('4.O que é um arquivo?\n a) Um programa\n b) Um conjunto de dados\n c) Um vírus\n d) Um hardware\n').lower()
if p4=='b':
    contador_acertos+=1
    acertos.append(f'4.{p4}')
else:
    contador_erros+=1
    erros.append(f'4.{p4}')
p5=input('5.O que significa RAM?\n a) Read Access Memory\n b) Random Access Memory\n c) Run Access Memory\n d) Real Access Memory\n').lower()
if p5=='b':
    contador_acertos+=1
    acertos.append(f'5.{p5}')
else:
    contador_erros+=1
    erros.append(f'5.{p5}')
p6=input('6.Qual linguagem é usada para criar sites?\na) Python\nb) HTML\nc) C++\nd) Java\n').lower()
if p6=='b':
    contador_acertos+=1
    acertos.append(f'6.{p6}')
else:
    contador_erros+=1
    erros.append(f'6.{p6}')
p7=input('7.O que faz o sistema operacional?\na) Cria jogos\nb) Controla o hardware e software\nc) Só abre arquivos\nd) Faz internet funcionar\n').lower()
if p7=='b':
    contador_acertos+=1
    acertos.append(f'7.{p7}')
else:
    contador_erros+=1
    erros.append(f'7.{p7}')
p8=input('8.O que é um algoritmo?\na) Um programa pronto\nb) Um conjunto de passos para resolver um problema\nc) Um vírus\nd) Um hardware\n').lower()
if p8=='b':
    contador_acertos+=1
    acertos.append(f'8.{p8}')
else:
    contador_erros+=1
    erros.append(f'8.{p8}')
p9=input('9.O que é um loop?\n a) Uma variável\n b) Um erro\n c) Repetição de código\n d) Um tipo de arquivo\n').lower()
if p9=='c':
    contador_acertos+=1
    acertos.append(f'9.{p9}')
else:
    contador_erros+=1
    erros.append(f'9.{p9}')
p10=input('10.O que faz o comando if?\n a) Repete código\n b) Cria variável\n c) Faz uma condição\n d) Imprime na tela\n').lower()
if p10=='c':
    contador_acertos+=1
    acertos.append(f'10.{p10}')
else:
    contador_erros+=1
    erros.append(f'10.{p10}')
porcentagem= (contador_acertos/10)*100
print('TESTE FINALIZADO')
print(f'RESULTADO:\n voce obteve: {contador_acertos} acertos e {contador_erros} erros\nseus acertos: {acertos} \n seus erros: {erros}')
print(f'aproveitamento: {porcentagem}%')
