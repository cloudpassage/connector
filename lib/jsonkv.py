"""Json and key-value formatter"""
import json
from formatter import Formatter


class FormatJson(Formatter):
    def format_event(self, event):
        """Format raw data into json format"""
        formatted_event = "%s\n" % json.dumps(event)
        return formatted_event


class FormatKv(Formatter):
    def format_event(self, event):
        """Format raw data into key-value format"""
        formatted_event = ""
        for key, value in event.items():
            formatted_event += "%s=\"%s\" " % (key, value)
        formatted_event += "\n"
        return formatted_event
