from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data in correct order, per-object
        for obj in Activity.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.pk:
                obj.delete()
        for obj in User.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Team.objects.all():
            if obj.pk:
                obj.delete()

        # Create teams


        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team_id=str(marvel.id))
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team_id=str(marvel.id))
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team_id=str(dc.id))
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team_id=str(dc.id))

        # Create activities
        Activity.objects.create(user_id=str(tony.id), type='Running', duration=30)
        Activity.objects.create(user_id=str(steve.id), type='Cycling', duration=45)
        Activity.objects.create(user_id=str(bruce.id), type='Swimming', duration=60)
        Activity.objects.create(user_id=str(clark.id), type='Yoga', duration=20)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Lifting', description='Strength for DC', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(team_id=str(marvel.id), points=100)
        Leaderboard.objects.create(team_id=str(dc.id), points=90)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
