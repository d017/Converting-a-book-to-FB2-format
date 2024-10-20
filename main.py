import FB2 as fb
from bs4 import BeautifulSoup

# Parse
file_name = "book.html"
book_name = "1984.fb2"

# Parse
def extract_data(filename):
    with open(filename, "r", encoding="utf-8") as html_file:
        soup = BeautifulSoup(html_file, "lxml")
        data = soup.find_all(("p", "h4"))
        return data[3:]

# Reformat
def get_chapters(content: list):
    chapters = list()
    part = 1
    header = content[0].text
    header_pars = list()
    for el in content[1:]:
        if el.name == "p":
            header_pars.append(el.text.strip())
        elif el.name == "h4":
            chapters.append((f"{part}.{header}", header_pars))
            header_pars = list()
            if el.text == "1":
                part += 1
            header = el.text
    return chapters

# Write
def write_book(filename, chapters):
    book = fb.FictionBook2()
    book.title = "Title"
    book.chapters = chapters
    book.write(filename)

# Main
info = extract_data(file_name)
cont = get_chapters(info)
write_book(book_name, cont)
