# Generated by Django 4.2.6 on 2024-01-12 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("flashcard_api", "0003_alter_flashcard_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChapterNumber",
            fields=[
                (
                    "chapter",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False),
                ),
                ("maxNum", models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="flashcard",
            name="chapter",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="flashcard",
            name="chapterWordOrder",
            field=models.CharField(default="00001", max_length=5),
        ),
        migrations.AlterField(
            model_name="flashcard",
            name="id",
            field=models.PositiveIntegerField(
                primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("current_chapter", models.IntegerField(default=1)),
                ("last_word_id", models.IntegerField(default=1)),
                ("previous_chapter", models.IntegerField(default=1)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]