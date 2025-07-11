from datetime import datetime
from media import MediaFile
from storage import LocalStorage, S3Storage

file = MediaFile(
    name="test_photo.jpg",
    size=1024,
    created_at=datetime.now(),
    owner="admin"
)

local = LocalStorage()
local.save(file)
local.delete(file)

s3 = S3Storage()
s3.save(file)
s3.delete(file)
