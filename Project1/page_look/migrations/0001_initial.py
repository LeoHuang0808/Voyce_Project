# Generated by Django 2.1.7 on 2020-05-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('purpose', models.CharField(choices=[('IN', 'Inquiry'), ('CO', 'Complaint'), ('FB', 'Feedback')], max_length=2)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('Facility_Name', models.CharField(max_length=45, primary_key=True, serialize=False, unique=True)),
                ('As_of', models.DateField()),
                ('Open_Female_Medicaid_Beds', models.IntegerField()),
                ('Open_Male_Medicaid_Beds', models.IntegerField()),
                ('Open_Female_Medicare_Beds', models.IntegerField()),
                ('Open_Male_Medicare_Beds', models.IntegerField()),
                ('Open_Female_Private_Pay_Beds', models.IntegerField()),
                ('Open_Male_Private_Pay_Beds', models.IntegerField()),
                ('Open_Female_Dementia_Beds', models.IntegerField()),
                ('Open_Male_Dementia_Beds', models.IntegerField()),
                ('Notes', models.CharField(max_length=200)),
            ],
        ),
    ]
