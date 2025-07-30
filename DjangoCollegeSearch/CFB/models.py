from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    established_date = models.DateField()
    location = models.CharField(max_length=100)
    website = models.URLField()
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    contact_email = models.EmailField()
    history = models.TextField()

    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    established_date = models.DateField()
    description = models.TextField()
    logo = models.ImageField(upload_to='division_logos/', null=True, blank=True)
    contact_email = models.EmailField()
    history = models.TextField()
    home_page = models.URLField()


    def __str__(self):
        return self.name
    
class Conference(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    established_date = models.DateField()
    description = models.TextField()
    logo = models.ImageField(upload_to='conference_logos/', null=True, blank=True)  
    contact_email = models.EmailField()
    history = models.TextField()
    home_page = models.URLField()
    teams_count = models.PositiveIntegerField(default=0)
    championships_count = models.PositiveIntegerField(default=0)
    rivalries_count = models.PositiveIntegerField(default=0)
    championships = models.TextField(null=True, blank=True)  # List of championships won
    rivalries = models.TextField(null=True, blank=True)  # List of rivalries
    home_stadium = models.CharField(max_length=100, null=True, blank=True)  # Optional field for home stadium
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    home_stadium = models.CharField(max_length=100,)
    home_city = models.CharField(max_length=100)
    home_state = models.CharField(max_length=50)
    home_country = models.CharField(max_length=50, default='USA')
    team_color = models.CharField(max_length=50, null=True, blank=True)  # Optional field for team color
    mascot = models.CharField(max_length=100, null=True, blank=True)  
    team_website = models.URLField(null=True, blank=True)  # Optional field for team website
    slug = models.SlugField(unique=True)
    description = models.TextField()
    founded_date = models.DateField(null=True, blank=True)  # Optional field for founding
    university = models.CharField(max_length=100, null=True, blank=True)  # Optional field for university affiliation
    home_stadium_capacity = models.PositiveIntegerField(null=True, blank=True)
    home_stadium_location = models.CharField(max_length=100, null=True, blank=True)  # Optional field for stadium location
    home_stadium_image = models.ImageField(upload_to='stadium_images/', null=True,)
    established_date = models.DateField()
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)
    contact_email = models.EmailField()
    history = models.TextField()
    championships = models.TextField(null=True, blank=True)  # List of championships won
    rivalries = models.TextField(null=True, blank=True)  # List of rivalries
    home_page = models.URLField()
    championships_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Bowl(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    history = models.TextField()
    established_date = models.DateField()
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='bowl_logos/', null=True, blank=True)
    stadium = models.CharField(max_length=100)
    stadium_capacity = models.PositiveIntegerField(null=True, blank=True)
    stadium_location = models.CharField(max_length=100, null=True, blank=True)  # Optional field for stadium location
    stadium_image = models.ImageField(upload_to='stadium_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.team.name} vs {self.opponent} on {self.date}"

class Rivalry(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    rivalry_name = models.CharField(max_length=100)
    history = models.TextField()

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} - {self.rivalry_name}"
