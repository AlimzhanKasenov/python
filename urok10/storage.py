class StorageBackend:
    def save(self, file):
        raise NotImplementedError

    def delete(self, file):
        raise NotImplementedError

class LocalStorage(StorageBackend):
    def save(self, file):
        print(f"Сохраняем файл '{file.name}' на локальном диске.")

    def delete(self, file):
        print(f"Удаляем файл '{file.name}' с локального диска.")

class S3Storage(StorageBackend):
    def save(self, file):
        print(f"Сохраняем файл '{file.name}' в облаке (S3, Minio и т.п.).")

    def delete(self, file):
        print(f"Удаляем файл '{file.name}' из облака.")
