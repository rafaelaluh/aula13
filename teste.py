from bs4 import BeautifulSoup

html_exemplo = """
<head>Title</head>
<div class="loja">

    <ul>
    <li class="item1">Notebook</li>
    <li class="item2">Smartphone</li>
    </ul>
</div>



"""

soup = BeautifulSoup(html_exemplo,'html.parser')

itens = soup.find('head')
print(itens.text)
itens1 = soup.find_all('li', class_=['item1','item2'])

lista = [x for x in itens1]

print(lista[0].text, lista[1].text)