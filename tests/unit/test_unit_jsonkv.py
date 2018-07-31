import imp
import json
import os
import sys

module_name = 'lib'

here_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(here_dir, '../../')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
lib = imp.load_module(module_name, fp, pathname, description)


class TestUnitJsonkv:
    def event_stub(self):
        stub = [{u"id": u"fabc32206f0811e6ade117257b3d2b69",
                 u"type": u"fim_scan_requested",
                 u"name": u"File Integrity scan requested",
                 u"message": u"A file integrity monitoring scan was requested for Linux server <strong>ip-172-31-16-240</strong> (52.8.42.37) by Halo API key <strong>2f08af31 (Beagle-MTG)</strong> from IP address 52.8.10.254 (USA).",  # NOQA
                 u"server_id": u"1528ec8803db11e5ab872fd6dc843290",
                 u"created_at": u"2016-08-30T23:25:03.850Z",
                 u"critical": False,
                 u"actor_key_id": u"2f08af31",
                 u"actor_key_label": u"Beagle-MTG",
                 u"actor_ip_address": u"52.8.10.254",
                 u"actor_country": u"USA",
                 u"server_platform": u"Linux",
                 u"server_hostname": u"ip-172-31-16-240",
                 u"server_group_name": u"Canary",
                 u"server_ip_address": u"52.8.42.37",
                 u"server_reported_fqdn": u"ip-172-31-16-240.us-west-1.compute.internal",  # NOQA
                 u"server_label": None,
                 u"server_primary_ip_address": u"172.31.16.240",
                 u"server_display_name": u"ip-172-31-16-240"}]
        return stub

    def test_format_json(self):
        json_formatter = lib.FormatJson({"whatever": None})
        formatted_event = json_formatter.format_events(self.event_stub())[0]
        json_data = json.loads(formatted_event)
        assert self.event_stub()[0] == json_data

    def test_format_kv(self):
        kv_formatter = lib.FormatKv({"whatever": None})
        kv_data = kv_formatter.format_events(self.event_stub())
        for k, v in self.event_stub()[0].items():
            string = "%s=\"%s\" " % (k, v)
            assert string in kv_data[0]
