from django.db import models

class NoteModel(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	dt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
