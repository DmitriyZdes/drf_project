from django.core.management import BaseCommand
from users.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):

            Payment.objects.all().delete()

            payment_content = [

                {
                    'пользователь': 'Дмитрий',
                    'дата': '04/04/2024',
                    'оплаченный курс': 'Программирование',
                    'оплаченный урок': 'Высшая математика',
                    'сумма оплаты': '10000',
                    'cпособ оплаты': 'наличными',
                }
            ]

            payment_list = []
            for payment in payment_content:
                payment_list.append((Payment(**payment)))

            Payment.objects.bulk_create(payment_list)
