from django.db import models


class Asset(models.Model):
	name = models.CharField(max_length=255, default='')
	created = ''
	updated = ''
	image = ''
	status = ''
	tags = ''
	versions = ''  # Will contain a list of associated versions

	def __str__(self):
		return self.name

class Versions(models.Model):
	# Will contain the id of the associated asset
	asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE)
	number = models.IntegerField(default=0)

	def __str__(self):
		return str(self.number)
