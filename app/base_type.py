from abc import abstractmethod, ABCMeta
from enum import Enum, EnumMeta

class BaseType(Enum):

    @abstractmethod
    def describe(self):
        pass
    
    @classmethod
    def all_describe(cls, arr:list):
        for i in arr:
            yield cls(int(i)).describe()

    @classmethod
    def all_describe_as_list(cls, arr:list):
        return list(cls.all_describe(arr))

    @classmethod
    def all_names(cls, arr:list):
        for i in arr:
            yield cls(int(i)).name

    @classmethod
    def all_names_as_list(cls, arr:list):
        return list(cls.all_names(arr))

    def __str__(self):
        return self.describe()