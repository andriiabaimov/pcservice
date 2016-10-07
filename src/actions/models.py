from django.db import models
from model_utils import Choices
from model_utils.managers import QueryManager
from model_utils.models import StatusModel, TimeStampedModel

from hardware.models import Spare
from .behaviors import Addressable, Commentable, Phonable, Pricable
from .constants import MARKUP_DEFAULT, NAME_MAX_LENGTH


class Partner(Addressable, Phonable, TimeStampedModel):
    name = models.CharField(max_length=NAME_MAX_LENGTH)

    def __str__(self):
        return self.name


class Purchase(TimeStampedModel):
    pass


class PurchaseItem(Commentable, Pricable, TimeStampedModel):
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
