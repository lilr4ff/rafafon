'''
Estrutura do código:
- Coletar o nome do jogador
- Lista com: perguntas, alternativas e respostas
- Estrutura de como será exibido: Pergunta \ alternativa \ Campo para digitar a resposta
- Formula para verificar se a resposta está correta ou incorreta e devolver para o usuário. Além de analisar se o usuário está digitando os dados corretos (Números de 1 a 4)
- Devolver resultado, quantidade de acertos e a porcentagem
- Verificar se o resultado é maior ou menor que 85% e indicar se o usuário ganhou ou perder o jogo
'''

import os
os.system('cls')

nome_jogador = input("Insira seu nickname: ")

# Aqui temos uma lista geral "lista_perguntas", aberta com [] dentro dela temos, {} separadas por virgulas. Dentro de cada {} temos 3 valores = pergunta, alternativas(Que possui uma lista) e a resposta
lista_perguntas = [
    {
        "pergunta": "1 - Qual destes passwords foi o mais usado na internet?",
        "alternativas": ["a1b2c3", "abcdef", "123456", "123456789"],
        "resposta": 2
    },
    {
        "pergunta": "2 - O que significa a sigla 'www' na internet?",
        "alternativas": ["World Wide Web", "Web Wide World", "Web wide World", "Wide Web World"],
        "resposta": 0
    },
    {
        "pergunta": "3 - Qual foi o primeiro tweet da história?",
        "alternativas": ["Olá, twitter", "Olá mundo", "Olá, mundo", "Estou preparando meu twitter"],
        "resposta": 3
    },
    {
        "pergunta": "4 - Qual foi a duração do primeiro vídeo do Youtube?",
        "alternativas": ["5 minutos", "3 minutos", "1 minuto", "18 segundos"],
        "resposta": 2
    },
    {
        "pergunta": "5 - Em média, quantas pesquisas totalmente novas são feitas no Google por dia?",
        "alternativas": ["350 bilhões", "1 bilhão", "450 bilhões", "280 milhões"],
        "resposta": 2
    },
    {
        "pergunta": "6 - Qual foi a primeira rede social da história da internet?",
        "alternativas": ["Classmate", "My Space", "Orkut", "X"],
        "resposta": 0
    },
    {
        "pergunta": "7 - Quando foi criado o primeiro smartphone da história?",
        "alternativas": ["1994", "2000", "1998", "1978"],
        "resposta": 0
    },
    {
        "pergunta": "8 - Qual o nome do ataque cibernético que atingiu computadores no mundo todo este ano?",
        "alternativas": ["WannaSpy", "WannaFly", "WannaCry", "WannaDry"],
        "resposta": 2
    },
    {
        "pergunta": "9 - Qual a resolução de uma imagem Full HD?",
        "alternativas": ["1920x1080", "1280x720", "2560x1440", "3840x2160"],
        "resposta": 0
    },
    {
        "pergunta": "10 - Quantos bits cabem em um byte?",
        "alternativas": ["1 bit", "8 bits", "12 bits", "16 bits"],
        "resposta": 1
    },
    {
        "pergunta": "11 - Qual destes dispositivos é usado para armazenar dados permanentemente?",
        "alternativas": ["RAM", "HDD", "CPU", "GPU"],
        "resposta": 1
    },
    {
        "pergunta": "12 - Qual é o sistema operacional mais utilizado no mundo?",
        "alternativas": ["Windows", "Linux", "macOS", "Android"],
        "resposta": 0
    },
    {
        "pergunta": "13 - Qual destes é um protocolo de comunicação utilizado para enviar e receber e-mails?",
        "alternativas": ["HTTP", "SMTP", "FTP", "DNS"],
        "resposta": 1
    },
    {
        "pergunta": "14 - Qual é o principal objetivo de um firewall em um sistema de computador?",
        "alternativas": ["Acelerar a conexão de internet", "Proteger contra vírus", "Proteger contra ataques de hackers", "Aumentar o desempenho do processador"],
        "resposta": 2
    },
    {
        "pergunta": "15 - Qual destes não é um tipo de cabo de rede?",
        "alternativas": ["HDMI", "Ethernet", "Coaxial", "Fibra óptica"],
        "resposta": 0
    }
]

# Aqui função recebe uma lista contendo a pergunta e suas alternativas e printa na tela, e da a opção para o jogador responder
def mostrar_pergunta(perguntas):
    print(perguntas["pergunta"])
    for i, alternativa in enumerate(perguntas["alternativas"]): 
        print(f"{i + 1}: {alternativa}")
    print("Digite sua resposta (Responda com 1 a 4) ou digite 'desisto' para sair do jogo.")

resultado = 0

# Para cada pergunta, a função mostrar_pergunta(pergunta) mostra a pergunta e suas alternativas, while True: é usado para solicitar ao jogador uma resposta válida, após receber uma resposta, ela é comparada com a resposta correta da pergunta
for perguntas in lista_perguntas:
    mostrar_pergunta(perguntas)
    while True:
        resposta_jogador = input("Insira sua resposta: ")
        if resposta_jogador.lower() == "desisto":
            print(f"Você desistiu do jogo {nome_jogador}")
            exit()
        elif not resposta_jogador.isdigit() or int(resposta_jogador) < 1 or int(resposta_jogador) > 4:
            print("Por favor, insira um número entre 1 e 4.")
        else:
            resposta_jogador = int(resposta_jogador)
            if resposta_jogador == perguntas["resposta"] + 1:
                print("Resposta correta!")
                resultado += 1
            else:
                print("Resposta incorreta!")
            break

# Exibe o resultado do jogador, mostrando quantas perguntas ele acertou e qual a porcentagem de acerto
print(f"{nome_jogador}, você chegou ao final do Show do centavo! \n- Sua pontuação foi de {resultado} respostas corretas")
porcentagem = round((resultado / len(lista_perguntas)) * 100, 2)
print(f"- Você acertou {porcentagem}% das questões")

if porcentagem >= 85:
    print("Parabéns! Você ganhou 1 centavo!")
else:
    print("You lose! Tente novamente")