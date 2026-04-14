from typing import List, TypedDict


class Page(TypedDict):
    name: str
    description: str
    href: str

class Category(TypedDict):
    category: str
    pages: List[Page]

CATEGORIES: List[Category] = [
    {
        "category": "fun",
        "pages": [
            {
                "name": "Counter",
                "description": "customizable counter hehe",
                "href": "/fun/counter"
            }
        ]
    }
]

TOTAL_PAGES: int = sum(len(item["pages"]) for item in CATEGORIES)