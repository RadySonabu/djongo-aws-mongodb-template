from djongo import models

class Card(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name
    

