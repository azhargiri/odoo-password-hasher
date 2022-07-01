#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import sys
import passlib
from odoo.addons.base.models.res_users import DEFAULT_CRYPT_CONTEXT, Users

from odoo.cli.command import Command

class Hasher(Command):
    """Password hasher"""
    def __init__(self):
        super(Hasher, self).__init__()
        # self.session = requests.session()
        # ctx = passlib.context.CryptContext(DEFAULT_CRYPT_CONTEXT)
        ctx = DEFAULT_CRYPT_CONTEXT
        self.hasher = ctx.hash if getattr(ctx, 'hash') else ctx.encrypt

    def hash(self, plaintext):
        return self.hasher(plaintext)

    def run(self, cmdargs):
        parser = argparse.ArgumentParser(
            prog="%s deploy" % sys.argv[0].split(os.path.sep)[-1],
            description=self.__doc__
        )
        parser.add_argument('plaintext', help="Plain text to be hashed")

        if not cmdargs:
            sys.exit(parser.print_help())

        args = parser.parse_args(args=cmdargs)

        try:
            result = self.hash(args.plaintext)

            print(result)
        except Exception as e:
            sys.exit("ERROR: %s" % e)
