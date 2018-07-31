#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Cef class"""
from formatter import Formatter
import os


class Cef(Formatter):
    """Cef class"""
    datetime_format = '%b %d %Y %H:%M:%S UTC'
    event_reference_file = os.path.join(os.path.dirname(__file__),
                                        '../configs/cef.yml')

    def cef_constants(self, event):
        """build cef constants"""
        severity = 9 if event["critical"] else 3
        try:
            event_type_id = self.event_reference["eventIdMap"][event["type"]]
        except KeyError:
            event_type_id = 999
        evt = ("CEF:%s|%s|%s|%s|%s|%s|%s|" %
               (self.event_reference["cefVersion"],
                self.event_reference["cefVendor"],
                self.event_reference["cefProduct"],
                self.product_version,
                event_type_id, event["name"], severity))
        return evt

    def build_cef_outliers(self, mapping, event):
        """Determine directinoality for event."""
        mapping['deviceDirection'] = 1 if 'actor_username' in event else 0

    def build_cef_mapping(self, event):
        """build cef mapping"""
        mapping = {}
        self.build_cef_outliers(mapping, event)
        for key, value in self.event_reference['cefFieldMapping'].items():
            if key in event:
                if key == "created_at":
                    event_dt = self.halo_timestamp_to_datetime(event[key])
                    mapping[value] = self.format_timestamp(event_dt)
                else:
                    mapping[value] = event[key]
                    if value in ['cs1', 'cs2', 'cs3', 'cs4']:
                        label = "%sLabel" % value
                        mapping[label] = self.event_reference['cefCsLabels'][label]  # NOQA
                del event[key]
        if event:
            mapping["cs5Label"] = self.event_reference['cefCsLabels']['cs5Label']  # NOQA
            mapping["cs5"] = event
        return mapping

    def format_event(self, event):
        """Format event for CEF.

        This is called by the format_events() function in the parent class.

        Args:
            event(dict): This is a single Halo event.

        Returns:
            str: CEF-formatted event.
        """
        retval = self.cef_constants(event)
        schema = self.build_cef_mapping(event)
        for key, value in schema.items():
            retval += "%s=%s " % (key, value)
        return retval
