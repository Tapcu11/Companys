import openpyxl
import pandas as pd
path = r"/content/drive/MyDrive/FILES_FOR_COLAB/SNG.xlsx"
wb = openpyxl.load_workbook(path)

wbsheet = wb.active

#get exchange_rate from csv file (nbg.gov.ge link)
csv_url = r"https://nbg.gov.ge/fm/%E1%83%A1%E1%83%A2%E1%83%90%E1%83%A2%E1%83%98%E1%83%A1%E1%83%A2%E1%83%98%E1%83%99%E1%83%90/exchange_rates/geo/official-daily-exchange-ratesgeo.xlsx?v=o0wcq"
df = pd.read_excel(csv_url)


df.head(10)