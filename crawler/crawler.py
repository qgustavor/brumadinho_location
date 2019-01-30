import re
import csv
import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_raw_data():
    url = "http://brumadinho.vale.com/listagem-pessoas-sem-contato.html"
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.content


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.text
    ultima_atualizacao = re.search('(?<=atualização em ).+(?=\.)'.decode('utf-8'), text).group()
    ultima_atualizacao = datetime.strptime(ultima_atualizacao.encode('utf-8'), '%d/%m/%Y às %H:%M')
    nomes = [i.text.strip() for i in soup.find_all('li')]
    return (ultima_atualizacao, nomes)


if __name__ == "__main__":
    html = get_raw_data()
    dt, pessoas = parse_html(html)
    dt = dt.strftime('%d/%m/%Y - %H:%M')

    with open('data.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        with open('data_compare.csv', 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(('Nome', 'Última Atualização', 'Status'))
            for row in spamreader:
                t = 'Encontrado'
                for pessoa in pessoas:
                    if row[0] == pessoa.encode('utf-8'):
                        t = ' - '
                csv_writer.writerow((row[0], dt, t))
