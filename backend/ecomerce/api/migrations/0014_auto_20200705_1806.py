# Generated by Django 3.0.4 on 2020-07-06 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200705_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puntuation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(verbose_name='Puntos')),
                ('comment', models.TextField(null=True, verbose_name='Comentario')),
                ('follow_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('evaluated_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluated_user_id', to=settings.AUTH_USER_MODEL, verbose_name='Evaluado')),
                ('evaluator_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluator_user_id', to=settings.AUTH_USER_MODEL, verbose_name='Evaluador')),
            ],
            options={
                'verbose_name': 'Puntuation',
                'verbose_name_plural': 'Puntuations',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categoríes'},
        ),
        migrations.AlterModelOptions(
            name='complaints',
            options={'verbose_name': 'Complaint', 'verbose_name_plural': 'Complaints'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='date',
        ),
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_icon_class',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='comment',
            field=models.TextField(null=True, verbose_name='Comentario'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='problem',
            field=models.CharField(max_length=20, null=True, verbose_name='Problema'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='accuser_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accuser_user_id', to=settings.AUTH_USER_MODEL, verbose_name='Denunciante'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='denounced_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='denounced_user_id', to=settings.AUTH_USER_MODEL, verbose_name='Denunciado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Payment_method_order', to='api.Payment_method'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_method_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shipping_method_order', to='api.Shipping_method'),
        ),
        migrations.AlterField(
            model_name='payment_data',
            name='payment_method_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Payment_method', to='api.Payment_method'),
        ),
        migrations.DeleteModel(
            name='User_puntuation',
        ),
    ]
