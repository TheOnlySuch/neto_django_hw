import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for row in phones:
            print(row)
            phone = Phone(
                name=row['name'],
                price=float(row['price']),
                image=row['image'],
                release_date=datetime.strptime(row['release_date'], '%Y-%m-%d'),
                lte_exists=bool(row['lte_exists'])
            )
            phone.save()