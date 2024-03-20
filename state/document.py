# from "Arjan codes" youtube channel: https://www.youtube.com/watch?v=5OzLrbk82zY
from dataclasses import dataclass
from typing import Protocol


class DocumentState(Protocol):
    def edit(self): ...

    def review(self): ...

    def finalize(self): ...


class DocumentContext(Protocol):
    content: list[str]

    def set_state(self, state: DocumentState) -> None: ...

    def edit(self): ...

    def review(self): ...

    def finalize(self): ...

    def show_content(self): ...


@dataclass
class Draft:
    document: DocumentContext

    def edit(self):
        print("Editing the document...")
        self.document.content.append("Edited content.")

    def review(self):
        print("The document is now under review.")
        self.document.set_state(Reviewed(self.document))

    def finalize(self):
        print("You need to review the document before finalizing")


@dataclass
class Reviewed:
    document: DocumentContext

    def edit(self):
        print("Document is under review, cannot edit now.")

    def review(self):
        print("The document is already reviewed.")

    def finalize(self):
        print("Finalizing the document")
        self.document.set_state(Finalized(self.document))


@dataclass
class Finalized:
    document: DocumentContext

    def edit(self):
        print("Document is finalized. Editing is not allowed.")

    def review(self):
        print("Document is finalized. Reviewing is not allowed.")

    def finalize(self):
        print("Document is already finalized.")


class Document:
    def __init__(self):
        self.state: DocumentState = Draft(self)
        self.content: list[str] = []

    def set_state(self, state: DocumentState) -> None:
        self.state = state

    def edit(self):
        self.state.edit()

    def review(self):
        self.state.review()

    def finalize(self):
        self.state.finalize()

    def show_content(self):
        print("Document content:", " ".join(self.content))


def main() -> None:
    document = Document()
    document.edit()
    document.show_content()
    document.finalize()
    document.review()
    document.edit()
    document.finalize()
    document.edit()


if __name__ == "__main__":
    main()
