import csv
import urllib.request
import os
import random

def baixar_dicionario_portugues():
    """Baixa um dicionário de palavras em português do LibreOffice."""
    url = "https://raw.githubusercontent.com/LibreOffice/dictionaries/master/pt_BR/pt_BR.dic"
    print("Baixando dicionário de português...")
    
    filename = "dicionario_pt_br.dic"
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
        print(f"Dicionário baixado como '{filename}'")
    else:
        print(f"Usando dicionário existente: '{filename}'")
    
    return filename

def extrair_palavras(arquivo_dic):
    """Extrai palavras do arquivo de dicionário."""
    palavras = []
    
    with open(arquivo_dic, 'r', encoding='utf-8', errors='ignore') as arquivo:
        # Pular a primeira linha (contagem de palavras)
        next(arquivo)
        
        for linha in arquivo:
            # No formato do dicionário, a palavra vem antes de '/'
            if '/' in linha:
                palavra = linha.split('/')[0].strip()
            else:
                palavra = linha.strip()
            
            # Filtrar palavras vazias ou muito curtas
            if palavra and len(palavra) > 2:
                palavras.append(palavra)
    
    return palavras

def criar_arquivo_csv(palavras, nome_arquivo, quantidade=None):
    """Cria um arquivo CSV com as palavras."""
    # Se quantidade não for especificada, usar todas as palavras
    if quantidade is None:
        quantidade = len(palavras)
    else:
        quantidade = min(quantidade, len(palavras))
    
    # Embaralhar as palavras e selecionar a quantidade desejada
    palavras_selecionadas = random.sample(palavras, quantidade)
    
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        for palavra in palavras_selecionadas:
            escritor.writerow([palavra])
    
    print(f"Arquivo '{nome_arquivo}' com {quantidade} palavras criado com sucesso!")
    return nome_arquivo

def main():
    # Baixar o dicionário
    arquivo_dic = baixar_dicionario_portugues()
    
    # Extrair palavras
    print("Extraindo palavras do dicionário...")
    palavras = extrair_palavras(arquivo_dic)
    print(f"Total de {len(palavras)} palavras extraídas.")
    
    # Criar diferentes arquivos CSV para benchmark
    criar_arquivo_csv(palavras, 'palavras_10k.csv', 10000)
    criar_arquivo_csv(palavras, 'palavras_100k.csv', 100000)
    criar_arquivo_csv(palavras, 'palavras_1m.csv', 1000000)
    
    print("Todos os arquivos CSV foram criados!")

if __name__ == "__main__":
    main()