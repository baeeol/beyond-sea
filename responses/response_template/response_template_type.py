from typing import TypedDict


class ItemcardItem(TypedDict):
    title: str
    description: str


class Itemcard(TypedDict):
    title: str
    items: list[ItemcardItem]
