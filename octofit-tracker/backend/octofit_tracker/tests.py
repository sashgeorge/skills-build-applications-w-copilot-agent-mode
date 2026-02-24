from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Tony Stark', email='tony@stark.com', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Do 50 pushups')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity(self):
        self.assertEqual(self.activity.activity_type, 'Running')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 100)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Pushups')
