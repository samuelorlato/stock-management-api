from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Entity = TypeVar("Entity")
Presenter = TypeVar("Presenter")
Payload = TypeVar("Payload")

class ApiMapperInterface(ABC, Generic[Entity, Presenter, Payload]):
    @abstractmethod
    def to_api(self, entity: Entity) -> Presenter:
        """Entity to Presenter"""

    @abstractmethod
    def to_entity(self, payload: Payload) -> Entity:
        """Payload to Entity"""