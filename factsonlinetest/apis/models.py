from django.db import models

class LangModel(models.Model):
    lang_name = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.lang_name
