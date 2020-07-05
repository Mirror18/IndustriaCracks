# Generated by Django 3.0.8 on 2020-07-05 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200705_0808'),
    ]

    operations = [
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
    ]
