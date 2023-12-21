from abc import ABC, abstractmethod

class DbInterface(ABC):
    @abstractmethod
    def connection(self) -> None:
        """Execute a database connection"""