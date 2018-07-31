from django.db import models

class User(models.Model):
	"""用户模型  """

	name = models.CharField(max_length=128, unique=True)
	password = models.CharField(max_length=256)
	#email = models.EmailField(unique=True)
	logup_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta(object):
		"""docstring for Meta"""
		ordering = ["logup_time"]
		#verbose

	
