import os
import sys
from typing import Union
from bs4 import BeautifulSoup, Tag


class Document:
    def __init__(
        self,
        title: str,
        body: str,
        authors: Union[list[str], None] = None,
        date: Union[str, None] = None,
    ):
        self.title = title
        self.body = body
        self.authors = authors
        self.date = date

    def __repr__(self):
        header = ["---"]
        header.append(f"title: {self.title}")

        if self.date is not None:
            header.append(f"date: {self.date}")

        if self.authors is not None:
            header.append("authors:")
            for author in self.authors:
                header.append(f"  - {author}")
        header.append("---")

        return str.join("\n", header) + "\n\n" + self.body


def process_file(path: str):
    with open(path, mode="r", encoding="utf8") as f:
        soup = BeautifulSoup(f.read(), "xml")

    dirname = os.path.dirname(path)
    filename = os.path.basename(path)[:-8]

    title = None
    title_elements = soup("title")

    for title_element in title_elements:
        if title_element.text is not None and title_element.text != "":
            title = title_element.text

    if title is None:
        title = filename

    date = None
    date_element = soup.find(date, type="published")
    if isinstance(date_element, Tag):
        if date_element.has_attr("when"):
            date = str(date_element.get("when"))
        else:
            date = date_element.text

    authors = []
    author_elements = soup("author")
    for author_element in author_elements:
        if author_element.find("persName"):
            author_element = author_element.find("persName")
        author = str.join(" ", (map(lambda el: el.text, author_element.children)))
        authors.append(author)

    body = ""
    body_element = soup.find("text")
    if body_element is not None:
        body_element = body_element.find("body")
    if body_element is not None and isinstance(body_element, Tag):
        body = str.join("\n\n", map(lambda el: el.text, body_element.children)).strip()

    document = Document(title, body, authors, date)
    path_out = os.path.join(dirname, filename + ".txt")

    with open(path_out, mode="w", encoding="utf8") as f:
        f.write(str(document))


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        path = "d:/Synced/Work/BDSI/lexis-nexis-scepsis/downloads/run 3/grobid"

    if os.path.isdir(path):
        for file in os.listdir(path):
            if file.endswith(".xml"):
                process_file(os.path.join(path, file))
                print(".", end="")
    elif os.path.isfile(path):
        process_file(path)
    else:
        print(f"path '{path}' not found")
