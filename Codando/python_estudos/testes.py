import streamlit as st

nome_jogador = st.text_input("Insira seu nickname:", key="nickname")
resultado = 0

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
]

def mostrar_pergunta(pergunta):
    st.write(pergunta["pergunta"])
    for i, alternativa in enumerate(pergunta["alternativas"]):
        st.write(f"{i + 1}: {alternativa}")

st.title("Show do Centavo")

for idx, pergunta in enumerate(lista_perguntas):
    mostrar_pergunta(pergunta)
    resposta_jogador = st.text_input(f"Insira sua resposta para a pergunta {idx + 1}:", key=f"resposta_{idx}")
    if resposta_jogador.lower() == "desisto":
        st.write(f"Você desistiu do jogo, {nome_jogador}!")
        break
    elif not resposta_jogador.isdigit() or int(resposta_jogador) < 1 or int(resposta_jogador) > 4:
        st.write("Por favor, insira um número entre 1 e 4.")
    else:
        resposta_jogador = int(resposta_jogador)
        if resposta_jogador == pergunta["resposta"] + 1:
            st.write("Resposta correta!")
            resultado += 1
        else:
            st.write("Resposta incorreta!")

if resultado > 0:
    st.write(f"{nome_jogador}, você chegou ao final do Show do Centavo! \n- Sua pontuação foi de {resultado} respostas corretas")
    porcentagem = round((resultado / len(lista_perguntas)) * 100, 2)
    st.write(f"- Você acertou {porcentagem}% das questões")

    if porcentagem >= 85:
        st.write("Parabéns! Você ganhou 1 centavo!")
    else:
        st.write("Você perdeu! Tente novamente.")