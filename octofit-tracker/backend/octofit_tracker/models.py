from djongo import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=24)  # Store ObjectId as string
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    user_id = models.CharField(max_length=24)  # Store ObjectId as string
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    team_id = models.CharField(max_length=24)  # Store ObjectId as string
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
