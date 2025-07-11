from datetime import datetime

class MediaFile:
    def __init__(self, name, size, created_at, owner):
        self.name = name
        self.size = size
        self.created_at = created_at  # datetime
        self.owner = owner

    def save(self):
        """Сохранить файл (реализация зависит от типа хранилища)."""
        raise NotImplementedError

    def delete(self):
        """Удалить файл."""
        raise NotImplementedError

    def update(self, **kwargs):
        """Обновить метаданные файла."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def info(self):
        """Вернуть общую информацию о файле."""
        return {
            "name": self.name,
            "size": self.size,
            "created_at": self.created_at,
            "owner": self.owner
        }
