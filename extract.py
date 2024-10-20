import requests as rq

link = "https://knihi.com/Dzordz_Oruel/1984.html"
file_name = "book.html"

req = rq.get(link)
req.encoding = "utf-8"
html_text = req.text

with open(file_name, "w", encoding="utf-8") as file:
    file.write(html_text)
