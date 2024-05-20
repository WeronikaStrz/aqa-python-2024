from abc import ABC, abstractmethod


class WorkerInterface(ABC):
    @abstractmethod
    def go_to_page(self, url: str): ...

    @abstractmethod
    def find_element_by_id(self, elem_id: str): ...

    @abstractmethod
    def find_element_by_class(self, elem_class: str): ...

    @abstractmethod
    def type_text(self, box, text): ...

    @abstractmethod
    def click(self, button): ...
