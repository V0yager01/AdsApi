import csv

from django.core.management.base import BaseCommand

from adapi.models import Ad


path_csv = {
    'data/ads.csv': Ad,
}


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for path, model in path_csv.items():
            try:
                with open(
                    path,
                    'r', encoding='utf-8'
                ) as csv_file:
                    data_list = []
                    data = csv.DictReader(csv_file)
                    for row in data:
                        data_list.append(model(**row))
                    model.objects.bulk_create(data_list)
            except Exception as err:
                self.stdout.write(self.style.ERROR(f'{err}'))
        self.stdout.write(self.style.SUCCESS('Upload Complete!'))