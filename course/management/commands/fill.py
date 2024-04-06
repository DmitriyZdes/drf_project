from django.core.management import BaseCommand
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):

            Payment.objects.all().delete()

            payment_content = [

                {
                    'user': User.objects.get_or_create(email='test1@sky.pro'),
                    'date': '04/04/2024',
                    'payed_stage': 'Программирование',
                    'payed_subject': 'Высшая математика',
                    'sum': '10000',
                    'pay_approach': 'наличными',
                }
            ]

            payment_list = []
            for payment in payment_content:
                payment_list.append((Payment(**payment)))

            Payment.objects.bulk_create(payment_list)
