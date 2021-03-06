# Generated by Django 3.1.4 on 2020-12-20 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('amount', models.IntegerField(default=100)),
                ('status', models.CharField(choices=[('Order Recieved', 'Order Recieved'), ('Baking', 'Baking'), ('Baked', 'Baked'), ('Out for delivery', 'Out for delivery'), ('Order recived', 'Order recived')], default='Order Recived', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
