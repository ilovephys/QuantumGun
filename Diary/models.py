from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ("Python", "Python"),
    ("Django", "Django"),
    ("DataScience", "DataScience"),
    ("FIRE", "FIRE"),
    ("Education", "Education"),
    ("PythonHuck", "PythonHuck"),
    ("MathPhys", "MathPhys"),
    ("Other", "Other"),
)
class Advertising(models.Model):
    category = models.CharField(
        max_length=50,
        choices=CATEGORY
    )
    advertising = models.TextField()
    def __str__(self):
        return self.category

class BlogModel6(models.Model):
    title = models.CharField(max_length=100)
    advertising = models.ForeignKey(
        Advertising,
        verbose_name="Advertising",
        on_delete=models.PROTECT,
        null=True
    )
    contentDescription = models.TextField(max_length=150)
    postdate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY
    )
    eyeCatch = models.ImageField(
        verbose_name="アイキャッチ画像",
        blank=True,
        null=True,
        upload_to="static/img"
    )
    pageView = models.PositiveIntegerField(default=0)
    introduction = models.TextField(
        blank=False,
        null=False,
                                    )
    content = models.TextField()
    link = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content2 = models.TextField(
        blank=True,
        null=True
    )
    link2 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content3 = models.TextField(
        blank=True,
        null=True
    )
    link3 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content4 = models.TextField(
        blank=True,
        null=True
    )
    link4 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content5 = models.TextField(
        blank=True,
        null=True
    )
    link5 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    """
    以下を拡充する際は、先にmanagement.commands.backup_diary.pyに
    バックアップが残るように変形させてください
    """

    """
    content6 = models.TextField()
    link6 = models.PositiveIntegerField(default=0)
    content7 = models.TextField()
    link7 = models.PositiveIntegerField(default=0)
    content8 = models.TextField()
    link8 = models.PositiveIntegerField(default=0)
    content9 = models.TextField()
    link9 = models.PositiveIntegerField(default=0)
    content10 = models.TextField()
    link10 = models.PositiveIntegerField(default=0)
    """
    def __str__(self):
        return self.title

class aboutModel(models.Model):
    title = models.CharField(max_length=100)
    contentDescription = models.TextField(max_length=150)
    postdate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    eyeCatch = models.ImageField(
        verbose_name="アイキャッチ画像",
        blank=True,
        null=True,
        upload_to="static/img"
    )
    pageView = models.PositiveIntegerField(default=0)
    content = models.TextField()
    link = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content2 = models.TextField(
        blank=True,
        null=True
    )
    link2 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content3 = models.TextField(
        blank=True,
        null=True
    )
    link3 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content4 = models.TextField(
        blank=True,
        null=True
    )
    link4 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content5 = models.TextField(
        blank=True,
        null=True
    )
    link5 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    """
    content6 = models.TextField()
    link6 = models.PositiveIntegerField(default=0)
    content7 = models.TextField()
    link7 = models.PositiveIntegerField(default=0)
    content8 = models.TextField()
    link8 = models.PositiveIntegerField(default=0)
    content9 = models.TextField()
    link9 = models.PositiveIntegerField(default=0)
    content10 = models.TextField()
    link10 = models.PositiveIntegerField(default=0)
    """

    def __str__(self):
        return self.title

class aboutQGModel(models.Model):
    title = models.CharField(max_length=100)
    contentDescription = models.TextField(max_length=150)
    postdate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    eyeCatch = models.ImageField(
        verbose_name="アイキャッチ画像",
        blank=True,
        null=True,
        upload_to="static/img"
    )
    pageView = models.PositiveIntegerField(default=0)
    content = models.TextField()
    link = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content2 = models.TextField(
        blank=True,
        null=True
    )
    link2 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content3 = models.TextField(
        blank=True,
        null=True
    )
    link3 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content4 = models.TextField(
        blank=True,
        null=True
    )
    link4 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content5 = models.TextField(
        blank=True,
        null=True
    )
    link5 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    """
    content6 = models.TextField()
    link6 = models.PositiveIntegerField(default=0)
    content7 = models.TextField()
    link7 = models.PositiveIntegerField(default=0)
    content8 = models.TextField()
    link8 = models.PositiveIntegerField(default=0)
    content9 = models.TextField()
    link9 = models.PositiveIntegerField(default=0)
    content10 = models.TextField()
    link10 = models.PositiveIntegerField(default=0)
    """

    def __str__(self):
        return self.title