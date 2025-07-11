from base import MediaFile

class AudioFile(MediaFile):
    def __init__(self, name, size, created_at, owner, duration, bitrate, codec):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.bitrate = bitrate
        self.codec = codec

    def convert(self, target_codec):
        """Конвертировать аудиофайл в другой кодек."""
        pass

    def extract_features(self):
        """Извлечь аудио-фичи (например, спектрограмму)."""
        pass
