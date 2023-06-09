from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=50)),
                ('programme_title', models.CharField(max_length=100)),
                ('programme_details', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('num_of_participants', models.PositiveIntegerField()),
                ('contact_person', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_tel', models.CharField(max_length=15)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('reason', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
