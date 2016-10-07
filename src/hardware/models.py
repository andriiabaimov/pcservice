from django.db import models
from model_utils.models import TimeStampedModel


class SpareType(TimeStampedModel):
    NAME_MAX_LENGTH = 30

    name = models.CharField(max_length=NAME_MAX_LENGTH)


class Spare(TimeStampedModel):
    NAME_MAX_LENGTH = 30
    COMMENT_MAX_LENGTH = 100

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    spare_type = models.ForeignKey(SpareType, related_name='spares')
    comment = models.CharField(max_length=COMMENT_MAX_LENGTH)
