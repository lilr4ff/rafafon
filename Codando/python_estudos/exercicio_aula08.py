import requests

def consultar_NCM(NCMs):
    url = f"https://brasilapi.com.br/api/ncm/v1/{NCMs}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        print("Erro ao consultar API")
        return None
    