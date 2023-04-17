# posts/models.py
from django.db import models

# Create your models here.


class Post(models.Model):
    DEVELOPMENT = 'DEV'
    COMPUTER_SCIENCE = 'CS'
    NEW_TECHNOLOGY = 'NEW_TECH'
    CATEGORY = [
        (DEVELOPMENT, '개발'),
        (COMPUTER_SCIENCE, 'CS'),
        (NEW_TECHNOLOGY, '신기술'),
    ]

    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    category = models.CharField(
        max_length=20, choices=CATEGORY, default=DEVELOPMENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_categories():
        DEVELOPMENT = 'DEV'
        COMPUTER_SCIENCE = 'CS'
        NEW_TECHNOLOGY = 'NEW_TECH'
        CATEGORY = [
            (DEVELOPMENT, '개발'),
            (COMPUTER_SCIENCE, 'CS'),
            (NEW_TECHNOLOGY, '신기술'),
        ]
        categories = [item[0] for item in CATEGORY]
        return categories
