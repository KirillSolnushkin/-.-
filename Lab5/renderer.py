class Renderer:
    # Базовий клас для різних типів відображення
    def render_title(self, title: str) -> str:
        pass

    def render_text(self, text: str) -> str:
        pass

    def render_image(self, url: str) -> str:
        pass

    def render_id(self, id: str) -> str:
        pass


class HTMLRenderer(Renderer):
    def render_title(self, title: str) -> str:
        return f"<h1>{title}</h1>"

    def render_text(self, text: str) -> str:
        return f"<p>{text}</p>"

    def render_image(self, url: str) -> str:
        return f"<img src='{url}' />"

    def render_id(self, id: str) -> str:
        return f"<div class='id'>{id}</div>"


class JsonRenderer(Renderer):
    def render_title(self, title: str) -> str:
        return f'{{"title": "{title}"}}'

    def render_text(self, text: str) -> str:
        return f'{{"text": "{text}"}}'

    def render_image(self, url: str) -> str:
        return f'{{"image": "{url}"}}'

    def render_id(self, id: str) -> str:
        return f'{{"id": "{id}"}}'


class XmlRenderer(Renderer):
    def render_title(self, title: str) -> str:
        return f"<title>{title}</title>"

    def render_text(self, text: str) -> str:
        return f"<text>{text}</text>"

    def render_image(self, url: str) -> str:
        return f"<image>{url}</image>"

    def render_id(self, id: str) -> str:
        return f"<id>{id}</id>"