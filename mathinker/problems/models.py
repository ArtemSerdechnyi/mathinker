from django.contrib.auth.models import User  # todo mb create custom user model?
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Problem(models.Model):
    class DifficultyChoices(models.IntegerChoices):
        EASY = 1
        MEDIUM = 2
        HARD = 3

    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="problems")
    difficulty = models.CharField(max_length=1, choices=DifficultyChoices)
    created_by = models.ForeignKey(User,
                                   on_delete=models.PROTECT,
                                   related_name="problems")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,
                                   related_name="liked_problems")
    dislike = models.ManyToManyField(User,
                                     related_name="disliked_problems")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["difficulty", ]


class Comment(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="comments")
    problem = models.ForeignKey(Problem,
                                on_delete=models.CASCADE,
                                related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,
                                   related_name="liked_comments")
    dislike = models.ManyToManyField(User,
                                     related_name="disliked_comments")

    def __str__(self):
        return f"{self.user} - {self.problem}"

    class Meta:
        ordering = ["created_at", ]
