# Generated by Django 5.0.3 on 2024-04-05 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_stage_user_remove_subject_user_stage_owner_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='дата')),
                ('sum', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('pay_approach', models.CharField(max_length=100, verbose_name='способ оплаты')),
                ('payed_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.stage', verbose_name='оплаченный курс')),
                ('payed_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject', verbose_name='оплаченный предмет')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]