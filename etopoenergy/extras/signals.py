from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from etopoenergy.extras.models import NoticeBoard, Services

from etopoenergy.utils.logger import LOGGER
from etopoenergy.utils.emails import plain_email
from etopoenergy.utils.unique_generators import unique_slug_generator

# @receiver(pre_save, sender=NoticeBoard)
# def notice_board_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)

@receiver(pre_save, sender=Services)
def services_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)




