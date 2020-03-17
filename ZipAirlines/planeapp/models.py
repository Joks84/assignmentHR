from django.db import models

# Create your models here.
class Airplane(models.Model):
    """
    Based on input of plane_id and pass_no(number of passangers), different properties
    will be calculated
    """
    plane_id = models.CharField(max_length = 3)
    pass_no = models.CharField(max_length = 3)

    @property
    def tank_capacity(self):
        """
        Calculatating tank capacity based on plane_id
        """
        return int(self.plane_id) * 200

    @property
    def pass_consuption(self):
        """
        Calculating passanger consuption based on pass_no
        """
        return int(self.pass_no) * 0.002

    @property
    def fuel_consuption_min(self):
        """
        Calculationg total fuel consuption per minute based on plane_id and pass_no
        """
        return int(self.plane_id) * 0.80 + self.pass_consuption

    @property
    def fly_time(self):
        """
        Calculating possible fly time in minutes
        """
        return int(self.tank_capacity) / self.fuel_consuption_min
