# Generated by Django 4.2.11 on 2024-05-08 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='burger_image/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('is_available', models.BooleanField()),
                ('is_main', models.BooleanField()),
                ('is_president', models.BooleanField()),
                ('is_new', models.BooleanField()),
                ('compound', models.JSONField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Burger',
                'verbose_name_plural': 'Burgers',
                'db_table': 'burger',
                'ordering': ['is_new', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('fats', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('saturated_fats', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('carbohydrates', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('sugar', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('cellulose', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('squirrels', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('salt', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('energy_value', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('allergen', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
                'db_table': 'ingredient',
            },
        ),
        migrations.CreateModel(
            name='Proportion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField()),
                ('burger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.burger')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ingredient')),
            ],
            options={
                'verbose_name': 'Proportion',
                'verbose_name_plural': 'Proportions',
                'db_table': 'proportion',
            },
        ),
        migrations.AddField(
            model_name='burger',
            name='ingredients',
            field=models.ManyToManyField(related_name='burgers', through='menu.Proportion', to='menu.ingredient'),
        ),
        migrations.AddIndex(
            model_name='burger',
            index=models.Index(fields=['is_available'], name='burger_is_avai_d8eeb8_idx'),
        ),
        migrations.AddIndex(
            model_name='burger',
            index=models.Index(fields=['id', 'slug'], name='burger_id_584fdd_idx'),
        ),
    ]
