
from django.core.mail import send_mail

from .models import Order


def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ номер {}'.format(order.id)
    message = ' {},\n\n заказ успешно оформлен.\
                Номер заказа {}.'.format(order.first_name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'sabirova.elvira.g@gmail.com',
                          [order.email])
    return mail_sent