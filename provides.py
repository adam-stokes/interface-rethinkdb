# Copyright (c) 2015 Adam Stokes <adam.stokes@ubuntu.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

from charms.reactive import RelationBase
from charms.reactive import scopes
from charms.reactive import hook
from charms.reactive import not_unless


class RethinkDB(RelationBase):
    scope = scopes.SERVICE

    @hook('{provides:rethinkdb}-relation-joined')
    def joined(self):
        """
        Handles relation-joined hook.

        Triggers:

        * ``{relation_name}.database.requested``
        """
        conversation = self.conversation()
        conversation.set_state('{relation_name}.database.requested')

    @hook('{provides:rethinkdb}-relation-{broken,departed}')
    def departed(self):
        conversation = self.conversation()
        conversation.remove_state('{relation_name}.database.requested')
