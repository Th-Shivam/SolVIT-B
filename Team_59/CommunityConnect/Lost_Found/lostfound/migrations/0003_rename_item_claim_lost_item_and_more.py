# Generated by Django 5.1.7 on 2025-03-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfound', '0002_remove_lostitem_image_itemimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='item',
            new_name='lost_item',
        ),
        migrations.RenameField(
            model_name='claim',
            old_name='created_at',
            new_name='submitted_at',
        ),
        migrations.AddField(
            model_name='lostitem',
            name='founder_email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='claim',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='proof',
            field=models.FileField(upload_to='claim_proofs/'),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='brand_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='colors',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='time_found',
            field=models.CharField(max_length=8),
        ),
    ]
