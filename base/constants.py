from enum import Enum
from django.db.models import Func

class Type(Enum):
    VEG = "Veg"
    NONVEG = "Non-Veg"
    EGG = "Eggitarian"

    @classmethod
    def choices(cls):
        return tuple((type.name, type.value) for type in cls)


class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'