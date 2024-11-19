from renderer import HTMLRenderer, JsonRenderer, XmlRenderer
from page import SimplePage, ProductPage
from product import Product


def main():
    html_renderer = HTMLRenderer()
    json_renderer = JsonRenderer()
    xml_renderer = XmlRenderer()

    simple_page = SimplePage(
        html_renderer,
        "Всііім привіііт :D",
        "Це ну дуууже проста сторінка з текстом"
    )
    print("Проста сторінка HTML:")
    print(simple_page.render())

    simple_page = SimplePage(
        json_renderer,
        "Всііім хай :D",
        "А це... також проста сторінка з текстом"
    )
    print("\nПроста сторінка JSON:")
    print(simple_page.render())

    product = Product(
        "1",
        "Телефон",
        "Чудовий смартфон з великим екраном",
        "phone.jpg"
    )

    product_page = ProductPage(xml_renderer, product)
    print("\nСторінка продукту XML:")
    print(product_page.render())

    product_page = ProductPage(html_renderer, product)
    print("\nСторінка продукту HTML:")
    print(product_page.render())

if __name__ == "__main__":
    main()