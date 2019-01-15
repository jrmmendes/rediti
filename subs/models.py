from django.db import models
from common.models import IndexedTimeStampedModel
from users.models import User


class Subrediti(IndexedTimeStampedModel):
    """ Model que define um subrediti, que agrega várias threads. """
    name = models.CharField(max_length=50, default='New post')
    creator = models.ForeignKey(User, related_name='subreditis',
                                on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return self.name


class Thread(IndexedTimeStampedModel):
    """ Model que define um thread, que agrega vários posts. """
    author = models.ForeignKey(User, related_name='threads',
                               on_delete=models.CASCADE)

    title = models.TextField()
    subrediti = models.ForeignKey(Subrediti, related_name='threads',
                                  on_delete=models.CASCADE)

    vote_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Post(IndexedTimeStampedModel):
    """ Model que define um thread, que agrega vários posts. """
    vote_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='posts',
                               on_delete=models.CASCADE)

    content = models.TextField()

    thread = models.ForeignKey(Thread, related_name='posts',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Subscription(IndexedTimeStampedModel):
    """ Model que define uma inscrição em um subrediti.
        (o usuário visualizará as últimas postagens de suas
        inscrições) """

    user = models.ForeignKey(User, related_name="subscription",
                             on_delete=models.CASCADE)

    sub = models.ForeignKey(Subrediti, related_name="subscription",
                            on_delete=models.CASCADE)

    Subscription = models.BooleanField(default=False)

    class Meta:
        unique_together = [('user', 'sub')]
