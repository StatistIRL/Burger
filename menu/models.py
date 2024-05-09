from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    fats = models.PositiveSmallIntegerField(default=0, blank=True)
    saturated_fats = models.PositiveSmallIntegerField(default=0, blank=True)
    carbohydrates = models.PositiveSmallIntegerField(default=0, blank=True)
    sugar = models.PositiveSmallIntegerField(default=0, blank=True)
    cellulose = models.PositiveSmallIntegerField(default=0, blank=True)
    squirrels = models.PositiveSmallIntegerField(default=0, blank=True)
    salt = models.PositiveSmallIntegerField(default=0, blank=True)
    energy_value = models.PositiveSmallIntegerField(default=0, blank=True)
    allergen = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "ingredient"
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name


# TODO всё вроде норм посмотреть сохранение в JSON сделать сигнал на изменение m2m и также добавить проверку в метод save burger что при создании объекта всё сразу же просчитывалось; Так же подумать над тем что если из бургера удалили что-то то пропорция должна автоматически удоляться


class AvailableManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_available=True)


class Burger(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="burger_image/")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0, blank=True)
    is_available = models.BooleanField()
    is_main = models.BooleanField()
    is_president = models.BooleanField()
    is_new = models.BooleanField()
    ingredients = models.ManyToManyField(
        "menu.Ingredient", through="menu.Proportion", related_name="burgers"
    )
    compound = models.JSONField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        db_table = "burger"
        ordering = ["is_new", "id"]
        indexes = [
            models.Index(fields=["is_available"]),
            models.Index(fields=["id", "slug"]),
        ]
        verbose_name = "Burger"
        verbose_name_plural = "Burgers"

    def __str__(self):
        return self.name


class Proportion(models.Model):
    burger = models.ForeignKey(Burger, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "proportion"
        verbose_name = "Proportion"
        verbose_name_plural = "Proportions"
