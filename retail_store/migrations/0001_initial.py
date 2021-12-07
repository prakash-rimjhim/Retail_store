# Generated by Django 2.2.24 on 2021-12-04 02:02

from django.db import migrations, models
import django.db.models.deletion
import uuid
from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200, null=True)),
                ('productId', models.UUIDField(default=uuid.uuid4, null=True)),
                ('availableQuantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('customerId', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail_store.Product')),
            ],
        ),
    ]
