from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс BaseProduct для классов наследников для продуктов"""

    @abstractmethod
    def __add__(self):
        """абстрактный метод для сложения экземпляров продуктов"""
        pass

    @abstractmethod
    def __str__(self):
        """абстрактный метод для предоставления текстовой информации продукта пользователю"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls):
        """абстрактный метод для создания экземпляров продуктов"""
        pass
