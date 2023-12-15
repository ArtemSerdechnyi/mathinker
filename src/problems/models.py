from django.contrib.auth.models import User  # todo mb create custom user model?
from django.utils import timezone
from django.db import models

from taggit.managers import TaggableManager


class Theme(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80)

    # image = models.ImageField()  # todo add image for each theme?

    class Meta:
        ordering = ["name", ]

    def __str__(self):
        return self.name


class ProblemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Problem(models.Model):
    class DifficultyChoices(models.IntegerChoices):
        EASY = 1, "Easy"
        MEDIUM = 2, "Medium"
        HARD = 3, "Hard"

    theme = models.ForeignKey(Theme, related_name="problems", on_delete=models.PROTECT)
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    is_published = models.BooleanField(default=True)
    description = models.TextField(max_length=3000)
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

    tags = TaggableManager(related_name="problems")

    objects = models.Manager()
    published_objects = ProblemManager()

    class Meta:
        ordering = ["difficulty", "-pk"]

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    # def get_absolut_url(self):  # todo


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
                                   related_name="liked_comments",
                                   blank=True)
    dislike = models.ManyToManyField(User,
                                     related_name="disliked_comments",
                                     blank=True)
    replay = models.ForeignKey("self",
                               on_delete=models.CASCADE,
                               related_name="replay_comments",
                               blank=True,
                               null=True)

    class Meta:
        ordering = ["-created_at", ]

    def __str__(self):
        return f"{self.user} - {self.problem}"
