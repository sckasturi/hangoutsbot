from database import BaseModel
from peewee import *
from playhouse.fields import *

from .user import User

import settings

import logging
import os


class Conversation(BaseModel):
    id = CharField(primary_key=True)
    members = ManyToManyField(User, related_name='conversations')
    group = BooleanField()

    @property
    def logger(self):
        message_formatter = logging.Formatter('[%(message_time)s] <%(username)s> %(message)s')
        file_handler = logging.FileHandler(os.path.join(settings.LOGGING_DIRECTORY, '{}.log'.format(self.id)))
        file_handler.setFormatter(message_formatter)
        message_logger = logging.getLogger(self.id)
        message_logger.setLevel(logging.INFO)
        message_logger.addHandler(file_handler)
        return message_logger

    def __str__(self):
        return self.id