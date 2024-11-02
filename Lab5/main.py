from renderer import HTMLRenderer, JsonRenderer, XmlRenderer
from page import SimplePage, ProductPage
from product import Product


def main():
    # Створюємо різні типи рендерерів
    html_renderer = HTMLRenderer()
    json_renderer = JsonRenderer()
    xml_renderer = XmlRenderer()

    # Створюємо просту сторінку з різними рендерерами
    simple_page = SimplePage(
        html_renderer,
        "Привіт світ",
        "Це проста сторінка з текстом"
    )
    print("HTML Simple Page:")
    print(simple_page.render())

    # Змінюємо рендерер для тієї ж сторінки
    simple_page = SimplePage(
        json_renderer,
        "Привіт світ",
        "Це проста сторінка з текстом"
    )
    print("\nJSON Simple Page:")
    print(simple_page.render())

    # Створюємо продукт
    product = Product(
        "1",
        "Телефон",
        "Чудовий смартфон з великим екраном",
        "phone.jpg"
    )

    # Створюємо сторінку продукту з різними рендерерами
    product_page = ProductPage(xml_renderer, product)
    print("\nXML Product Page:")
    print(product_page.render())

    # Змінюємо рендерер для сторінки продукту
    product_page = ProductPage(html_renderer, product)
    print("\nHTML Product Page:")
    print(product_page.render())


if __name__ == "__main__":
    main()