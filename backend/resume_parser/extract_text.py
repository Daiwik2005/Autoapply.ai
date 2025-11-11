import pymupdf
# path=""#path to be inserted here


def resume(path):
    d=pymupdf.open(path)
    full_text=""
    for page_num in range(d.page_count):
       page=d.load_page(page_num)
       text=page.get_text()
       full_text+=text
    print(full_text)
    print(d.metadata)
    

