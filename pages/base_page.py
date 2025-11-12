
class BasePage:
    def __init__(self, page):
        self.page = page

    # открываем страницу
    def visit(self, url):
        self.page.goto(url, wait_until="networkidle") # ждем, пока элементы подгрузятся

    # перезагружаем страницу
    def reload(self):
        self.page.reload(wait_until="networkidle")