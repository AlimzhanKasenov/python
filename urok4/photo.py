from base import MediaFile

class PhotoFile(MediaFile):
    def __init__(self, name, size, created_at, owner, resolution, camera_model):
        super().__init__(name, size, created_at, owner)
        self.resolution = resolution
        self.camera_model = camera_model

    def apply_filter(self, filter_type):
        """Применить фильтр к фотографии."""
        pass

    def extract_metadata(self):
        """Извлечь EXIF-метаданные."""
        pass
