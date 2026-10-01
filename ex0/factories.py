import abc
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon

class CreatureFactory(abc.ABC):
    @abc.abstractmethod
