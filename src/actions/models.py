from django.db import models
from django.urls import reverse
from model_utils import Choices
from model_utils.managers import QueryManager
from model_utils.models import StatusModel, TimeStampedModel

from hardware.models import Spare
from .behaviors import Addressable, Commentable, Phonable, Pricable


class Partner(Addressable, Phonable, TimeStampedModel):
    NAME_MAX_LENGTH = 50

    name = models.CharField(max_length=NAME_MAX_LENGTH)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actions:partner_detail', args=[str(self.id)])


class Purchase(TimeStampedModel):
    pass


class PurchaseItem(Commentable, Pricable, TimeStampedModel):
    MARKUP_DEFAULT = 20

    spare = models.ForeignKey(Spare, related_name='purchases')
    amount = models.IntegerField()
    markup = models.IntegerField(default=MARKUP_DEFAULT)


class Repair(StatusModel, TimeStampedModel):
    STATUS = Choices('new', 'done')

    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

    latest_status_change_attempt = models.DateTimeField(null=True)
    latest_status_change_success = models.DateTimeField(null=True)

    objects = models.Manager()
    done = QueryManager(status=STATUS.done).order_by('-modified')

    @classmethod
    def create_repair(cls, status):
        repair = cls(status=status)
        repair.save()
        return repair
