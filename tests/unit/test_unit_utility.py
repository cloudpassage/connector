import sys
import os
import pytest
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '../../', 'lib'))
from utility import Utility
import settings

auth_file_name = "keys.auth"
tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
auth_file = os.path.join(tests_dir, "configs/", auth_file_name)
configdir = os.path.join(tests_dir, "tests/data/")


class TestUnitUtility:
    def create_utility_object(self, options):
        return Utility(options)

    # def create_settings_object(self):
    #    return Settings()

    def test_parse_auth(self):
        options = {
            'auth': auth_file,
        }
        utility = self.create_utility_object(options)
        resp = utility.parse_auth()
        assert 'key_id' in resp[0]
        assert 'secret_key' in resp[0]

    def test_parse_pagination_limit_batchsize_none(self):
        options = {
            'batchsize': None
        }
        utility = self.create_utility_object(options)
        # setting = self.create_settings_object()
        resp = utility.parse_pagination_limit()
        assert resp == settings.pagination_limit()

    def test_parse_pagination_limit_batchsize_commandline(self):
        options = {
            'batchsize': 4
        }
        utility = self.create_utility_object(options)
        resp = utility.parse_pagination_limit()
        assert resp == 4

    def test_parse_pagination_limit_batchsize_str(self):
        options = {
            'batchsize': "cat"
        }
        utility = self.create_utility_object(options)
        try:
            utility.parse_pagination_limit()
        except ValueError as e:
            assert "is not an integer" in str(e)

    def test_parse_pagination_limit_batchsize_exceed(self):
        options = {
            'batchsize': 60
        }
        utility = self.create_utility_object(options)
        try:
            utility.parse_pagination_limit()
        except ValueError as e:
            assert "you have exceeded the batchsize limitation" in str(e)

    def test_parse_threads_none(self):
        options = {
            'threads': None
        }
        utility = self.create_utility_object(options)
        # setting = self.create_settings_object()
        resp = utility.parse_threads()
        assert resp == settings.threads()

    def test_parse_threads_str(self):
        options = {
            'threads': "cat"
        }
        utility = self.create_utility_object(options)
        try:
            utility.parse_threads()
        except ValueError as e:
            assert "is not an integer" in str(e)

    def test_parse_threads_exceed(self):
        options = {
            'threads': 6
        }
        utility = self.create_utility_object(options)
        try:
            utility.parse_threads()
        except ValueError as e:
            assert "you have exceeded the thread limitation" in str(e)

    def test_check_starting_none(self):
        options = {
            'starting': None,
            'configdir': configdir
        }
        utility = self.create_utility_object(options)
        resp = utility.check_starting()
        assert resp is not None
        assert re.match(r'^\d{4}-\d{2}-\d{2}$', resp)

    def test_check_configdir_none(self):
        options = {
            'starting': '2018-06-30',
            'configdir': None
        }
        utility = self.create_utility_object(options)
        resp = utility.check_starting()
        assert resp is not None

    def test_check_starting_configdir_none(self):
        options = {
            'starting': None,
            'configdir': None
        }
        utility = self.create_utility_object(options)
        assert utility.check_starting() is None
