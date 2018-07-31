#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Leef class"""
from formatter import Formatter
import os


class Leef(Formatter):
    """Leef class"""
    event_reference_file = os.path.join(os.path.dirname(__file__),
                                        '../configs/leef.yml')

    def constants(self, event):
        """build leef constants"""
        evt = ("LEEF:%s|%s|%s|%s|%s|" %
               (self.event_reference['leefFormatVersion'],
                self.event_reference['leefVendor'],
                self.event_reference['leefProduct'],
                self.event_reference['leefProductVersion'],
                event['name']))
        return evt

    def event_category(self, event):
        """determine event category"""
        for key, value in self.event_reference['leefCategoriesByName'].items():
            if event['type'] in value:
                return key

    def build_leef_outliers(self, mapping, event):
        """build leef outliers"""
        category = self.event_category(event)
        mapping['cat'] = category if category else "unknown"
        mapping['leefDateFormat'] = self.event_reference['leefDateFormat']
        mapping['sev'] = 9 if event['critical'] else 3
        mapping['isLoginEvent'] = True if event['type'] in self.event_reference['leefLoginEventNames'] else False
        mapping['isLogoutEvent'] = True if event['type'] in self.event_reference['leefLogoutEventNames'] else False

    def build_leef_mapping(self, event):
        """build leef mapping"""
        mapping = {}
        self.build_leef_outliers(mapping, event)
        for key, value in self.event_reference['leefFieldMapping'].items():
            if key in event:
                mapping[value] = event[key]
                del event[key]
        if event:
            for ekey, evalue in event.items():
                mapping[ekey] = evalue
        return mapping

    def format_event(self, event):
        """Format event for LEEF.

        This is called by the format_events() function in the parent class.

        Args:
            event(dict): This is a single Halo event.

        Returns:
            str: LEEF-formatted event.
        """
        retval = self.constants(event)
        schema = self.build_leef_mapping(event)
        for key, value in schema.items():
            retval += "%s=%s     " % (key, value)
        return retval
