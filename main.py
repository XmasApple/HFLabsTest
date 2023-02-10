# https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999
# Необходимо написать скрипт, который парсит эту табличку и переносит ее в гуглодоку.
# Предусмотреть, что в будущем необходимо будет синхронизировать данные в гуглодоке,
# если что-то изменится в базе знаний.
import requests
from bs4 import BeautifulSoup
import gspread

# Получаем страницу
url = 'https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Получаем таблицу
table = soup.find('table', class_='confluenceTable')

# получаем заголовки таблицы
headers = table.find_all('th')
header_data = []
for header in headers:
    header_data.append(header.text)

# Получаем ячейки таблицы по строкам
rows = table.find_all('tr')
data = []
for row in rows[1:]:
    cells = row.find_all('td')
    # print(cells)
    row_data = []
    for cell in cells:
        # print(cell.text)
        row_data.append(cell.text)
    data.append(row_data)

# Подключаемся к гуглодоке
gc = gspread.service_account(filename='credentials.json')

TABLE_NAME = 'HFLabsTest'

try:
    # Получаем таблицу
    sh = gc.open(TABLE_NAME)
except gspread.exceptions.SpreadsheetNotFound:
    # Создаем таблицу
    sh = gc.create(TABLE_NAME)

# Получаем лист
worksheet = sh.sheet1

# Удаляем все данные
worksheet.clear()

# изменяем количество строк оставляя 10 пустых строк
worksheet.resize(rows=len(data) + 11, cols=20)

# Записываем заголовки
worksheet.append_row(header_data)

# Записываем данные
for row in data:
    worksheet.append_row(row)

# Уставливаем визуальную ширину второй колонки с описанием по максимальной ширине

# Получаем максимальную ширину
# max_width = max(data, key=lambda x: len(x[1]))
#
# print(max_width)
# 1/0

# Проверяем
print(worksheet.get_all_values())

# Открываем доступ на чтение всем
sh.share(None, perm_type='anyone', role='reader')

# Получаем ссылку на таблицу
print(sh.url)

