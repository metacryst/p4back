# Generated by Django 3.0.7 on 2020-06-11 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import q4back.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('information', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('artist_website', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtworkMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_url', models.ImageField(upload_to=q4back.models.upload_media)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworkmedias', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('primary_palette', models.CharField(choices=[('none', 'none'), ('light', 'light'), ('dark', 'dark'), ('blue', 'blue'), ('yellow', 'yellow'), ('red', 'red')], default='none', max_length=6)),
                ('secondary_palette', models.CharField(choices=[('none', 'none'), ('light', 'light'), ('dark', 'dark'), ('blue', 'blue'), ('yellow', 'yellow'), ('red', 'red')], default='none', max_length=6)),
                ('medium', models.CharField(choices=[('none', 'none'), ('sculpture', 'sculpture'), ('flat art', 'flat art'), ('audio', 'audio'), ('none', 'none')], default='none', max_length=9)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artwork', to='q4back.Artist')),
                ('artwork_media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artwork_media', to='q4back.ArtworkMedia')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_url', models.ImageField(upload_to=q4back.models.upload_media)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artistmedias', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist_media', to='q4back.ArtistMedia'),
        ),
        migrations.AddField(
            model_name='artist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists', to=settings.AUTH_USER_MODEL),
        ),
    ]
