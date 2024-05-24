from django.db import models

class ExamDetail(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    exam_board = models.CharField(max_length=100)
    notes = models.TextField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
