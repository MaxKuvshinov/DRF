import re

from rest_framework.exceptions import ValidationError


class YouTubeValidator:

    def __init__(self, field=None):
        self.field = field

    def __call__(self, value):

        youtube_pattern = (
            r"^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[a-zA-Z0-9_-]+$"
        )
        if not re.match(youtube_pattern, value):
            if self.field:
                raise ValidationError(
                    {self.field: "Доступны только ссылки с youtube.com"}
                )
            raise ValidationError("Доступны только ссылки с youtube.com")
