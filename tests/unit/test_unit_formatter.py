import datetime
import imp
import os
import pytest
import sys

module_name = 'lib'

here_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(here_dir, '../../')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
lib = imp.load_module(module_name, fp, pathname, description)


class TestUnitFormatter:
    def instantiate_formatter(self):
        formatter = lib.Formatter({'cefsyslog': None})
        return formatter

    def test_unit_formatter_instantiate(self):
        """Confirm that we can instantiate a formatter object."""
        assert self.instantiate_formatter()

    def test_unit_format_events_not_implemented(self):
        """Ensure that the format_events() function is not implemented here."""
        fmt = self.instantiate_formatter()
        with pytest.raises(NotImplementedError):
            fmt.format_events([{"event": "noexist"}])

    def test_unit_formatter_format_date_none(self):
        """Ensure that since there is no format string definedby default,
        the timestamp returned is ``None``.
        """
        fmt = self.instantiate_formatter()
        dt = datetime.datetime.now()
        assert fmt.format_timestamp(dt) is None

    def test_unit_formatter_format_date_string(self):
        """Ensure that since there is no format string definedby default,
        the timestamp returned is ``None``.
        """
        fmt = lib.Formatter
        date = '2018-01-01T12:31:01.3Z'
        tstamp_in = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
        fmt.datetime_format = '%b %d %Y %H:%M:%S UTC'
        expected = 'Jan 01 2018 12:31:01 UTC'
        assert fmt.format_timestamp(tstamp_in) == expected
