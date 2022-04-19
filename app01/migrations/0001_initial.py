# Generated by Django 3.2 on 2022-02-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene_Dis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gene', models.CharField(max_length=32)),
                ('Dis', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Gene_Gene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gene1', models.CharField(max_length=32)),
                ('Gene2', models.CharField(max_length=32)),
                ('num', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gene_Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gene', models.CharField(max_length=32)),
                ('Node', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Herb_Gene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Herb', models.CharField(max_length=32)),
                ('Gene', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Herb_Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Herb', models.CharField(max_length=32)),
                ('Node', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='symmap3_herb_herb_cosine_jiaoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('herb', models.CharField(max_length=32)),
                ('num', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='symmap3_herb_mm_symp_jiaoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Herb', models.CharField(max_length=32)),
                ('Gene', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='symmap3_herb_target_jiaoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Herb', models.CharField(max_length=32)),
                ('Gene', models.CharField(max_length=32)),
            ],
        ),
    ]