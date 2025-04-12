from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = "Populate the octofit_db database with test data"

    def handle(self, *args, **kwargs):
        # MongoDB connection
        client = MongoClient("mongodb://127.0.0.1:27017/")
        db = client["octofit_db"]

        # Test data
        users = [
            {"email": "user1@example.com", "name": "User One"},
            {"email": "user2@example.com", "name": "User Two"},
        ]

        teams = [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
        ]

        activities = [
            {"user": "user1@example.com", "description": "Ran 5km"},
            {"user": "user2@example.com", "description": "Cycled 10km"},
        ]

        leaderboard = [
            {"user": "user1@example.com", "score": 100},
            {"user": "user2@example.com", "score": 80},
        ]

        workouts = [
            {"user": "user1@example.com", "duration": 30},
            {"user": "user2@example.com", "duration": 45},
        ]

        # Populate collections
        db["users"].delete_many({})
        db["users"].insert_many(users)

        db["teams"].delete_many({})
        db["teams"].insert_many(teams)

        db["activities"].delete_many({})
        db["activities"].insert_many(activities)

        db["leaderboard"].delete_many({})
        db["leaderboard"].insert_many(leaderboard)

        db["workouts"].delete_many({})
        db["workouts"].insert_many(workouts)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with test data"))