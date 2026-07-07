from django.db import models

class book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.CharField()

    def _str_(self):
        return f"(sell.title) by (self.author)"