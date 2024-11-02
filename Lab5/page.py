from renderer import Renderer
from product import Product

class Page:
    # Базовий клас для сторінок
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def render(self) -> str:
        pass


class SimplePage(Page):
    def __init__(self, renderer: Renderer, title: str, content: str):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def render(self) -> str:
        return (
                self.renderer.render_title(self.title) +
                self.renderer.render_text(self.content)
        )


class ProductPage(Page):
    def __init__(self, renderer: Renderer, product: Product):
        super().__init__(renderer)
        self.product = product

    def render(self) -> str:
        return (
                self.renderer.render_title(self.product.name) +
                self.renderer.render_text(self.product.description) +
                self.renderer.render_image(self.product.image) +
                self.renderer.render_id(self.product.id)
        )