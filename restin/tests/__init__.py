import os
import sys
from unittest import TestCase

here_dir = os.path.dirname(os.path.abspath(__file__))
conf_dir = os.path.dirname(os.path.dirname(here_dir))

sys.path.insert(0, conf_dir)

import pkg_resources

pkg_resources.working_set.add_entry(conf_dir)

pkg_resources.require('Paste')
pkg_resources.require('PasteScript')

from paste.deploy import loadapp
import paste.fixture
import paste.script.appinstall

from restin.config.routing import *
from routes import request_config, url_for

test_file = os.path.join(conf_dir, 'test.ini')
cmd = paste.script.appinstall.SetupCommand('setup-app')
cmd.run([test_file])

class TestController(TestCase):
    def __init__(self, *args):
        wsgiapp = loadapp('config:test.ini', relative_to=conf_dir)
        self.app = paste.fixture.TestApp(wsgiapp)
        TestCase.__init__(self, *args)

__all__ = ['url_for', 'TestController']
