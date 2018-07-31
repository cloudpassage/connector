"""Formatter class definition."""
import yaml
from config_helper import ConfigHelper
from datetime import datetime
from options import Options


class Formatter(object):
    event_reference_file = None
    datetime_format = None

    def __init__(self, options=None):
        self.options = options or Options()
        self.product_version = ConfigHelper.get_product_version()
        self.event_reference = self.load_yaml_file(self.event_reference_file)

    def format_event(self, event):
        """This method is implemented in sub-classes."""
        raise NotImplementedError

    @classmethod
    def format_timestamp(cls, dt):
        """Return a formatted time stamp.

        In the parent ``Formatter`` class, this returns ``None`` because no
        datetime format is set.  Subclasses may set ``self.datetime_format``
        to format timestamps for different output requirements.

        Args:
            fmt(str): Format which describes the desired output format for
                time stamp

        Returns:
            str: Formatted ``dt``.
        """
        if cls.datetime_format is None:
            return None
        return dt.strftime(cls.datetime_format)

    @classmethod
    def load_yaml_file(cls, event_reference_file):
        """Return Python dict for contents of yaml file."""
        if event_reference_file is None:
            return None
        else:
            with open(event_reference_file, 'r') as e_r_file:
                return yaml.load(e_r_file)

    @classmethod
    def halo_timestamp_to_datetime(cls, halo_timestamp):
        return datetime.strptime(halo_timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')

    def format_events(self, events):
        """This is an iterating wrapper for format_event."""
        formatted_events = []
        for event in events:
            formatted_events.append(self.format_event(event))
        return formatted_events
