from django.contrib.auth.models import User  # todo mb create custom user model?
from django.utils import timezone
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80)
    # image = models.ImageField()  # todo add image for each theme?

    class Meta:
        ordering = ["name", ]

    def __str__(self):
        return self.na



class Problem(models.Model):
    class DifficultyChoices(models.IntegerChoices):
        EASY = 1
        MEDIUM = 2
        HARD = 3

    theme = models.ForeignKey(Theme, related_name="problems", on_delete=models.PROTECT, unique=True)
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="problems")
    difficulty = models.CharField(max_length=1, choices=DifficultyChoices)
    created_by = models.ForeignKey(User,
                                   on_delete=models.SET_NULL,
                                   related_name="problems",
                                   default=None,
                                   blank=True,
                                   null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,
                                   related_name="liked_problems")
    dislike = models.ManyToManyField(User,
                                     related_name="disliked_problems")

    class Meta:
        ordering = ["difficulty", ]

    def __str__(self):
        return self.title


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

    class Meta:
        ordering = ["created_at", ]

    def __str__(self):
        return f"{self.user} - {self.problem}"
