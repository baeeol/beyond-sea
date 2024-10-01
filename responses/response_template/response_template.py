from .response_template_type import *


class ResponseTemplate:
    def __init__(self):
        self.data = {"outputs": []}

    def __call__(self) -> dict:
        return self.data

    def add_text_output(self, text: str):
        text_output = {"simpleText": {"text": text}}
        self.data['outputs'].append(text_output)

    def add_itemcard_carousel_output(self, itemcards: list[Itemcard]):
        itemcard_carousel_output = {
            "carousel": {"type": "itemCard", "items": []}}

        for itemcard in itemcards:
            card = {"imageTitle": {"title": itemcard["title"]}, "itemList": []}
            for item in itemcard["items"]:
                card["itemList"].append(
                    {"title": item["title"], "description": item["description"]})
            itemcard_carousel_output["carousel"]["items"].append(card)

        self.data['outputs'].append(itemcard_carousel_output)
