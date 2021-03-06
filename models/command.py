from database import BaseModel
from peewee import *
import sys
import importlib
import logging
import asyncio
import settings

logger = logging.getLogger(__name__)


class Command(BaseModel):
    name = CharField()
    admin_required = BooleanField()

    @asyncio.coroutine
    def run(self, bot, conversation, user, args):
        if "commands.{}".format(self.name) not in sys.modules:
            raise KeyError("Command with name {} not imported!".format(self.name))
        run = True
        if self.admin_required and not user.is_admin:
            run = False
        if run:
            yield from sys.modules["commands.{}".format(self.name)].command.run(bot, conversation, user, args)
        else:
            yield from bot.send_message(conversation, "You're not an admin!")

    def __str__(self):
        return self.name


class BaseCommand(object):

    def __init__(self, name, parser=None, admin_required=False):
        self.name = name
        self.parser = parser
        self.admin_required = admin_required

    @asyncio.coroutine
    def run(self, bot, conversation, user, args):
        raise NotImplementedError("The `run` method must be implemented.")
