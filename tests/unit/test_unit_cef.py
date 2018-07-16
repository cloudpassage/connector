# import cloudpassage
import pprint
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../', 'lib'))
from cef import Cef


class TestUnitCef:
    def create_cef_object(self):
        cef = Cef({'cefsyslog': None})
        return cef

    def event_stub(self):
        stub = [
            {
                "id": "e750d982688411e6b7b32f750f990d28",
                "type": "fim_target_integrity_changed",
                "name": "File Integrity change detected",
                "message": "A change was detected in file integrity target"
                           "/opt/cloudpassage/*/* on Linux server"
                           "Jlee-Chef-Node1 (54.183.177.195) (source: Scan)",
                "server_id": "5b1d73b63e3711e68ead7f4b70b6c2b8",
                "created_at": "2016-08-22T16:24:30.726Z",
                "critical": True,
                "server_platform": "Linux",
                "server_hostname": "ip-10-2-20-76",
                "server_group_name": "old_smoke",
                "server_ip_address": "54.183.177.195",
                "server_reported_fqdn": "localhost",
                "server_label": "Jlee-Chef-Node1",
                "server_primary_ip_address": "10.2.20.76",
                "scan_id": "e730037e688411e6b7b32f750f990d28",
                "finding_id": "e748d9c6688411e6b7b32f750f990d28",
                "policy_name": "FIM halo"
            }
        ]
        return stub

    def test_cef_constants(self):
        cef = self.create_cef_object()
        cef_constants = cef.cef_constants(self.event_stub()[0])
        expected = "CEF:0|CloudPassage|CPHalo|1.0|" \
                   "130|File Integrity change detected|9|"
        assert expected == cef_constants

    def test_cef_outliers(self):
        cef = self.create_cef_object()
        mapping = {}
        cef.build_cef_outliers(mapping, self.event_stub()[0])
        assert {"deviceDirection": 0} == mapping

    def test_build_cef_mapping(self):
        cef = self.create_cef_object()
        cef_mapping = cef.build_cef_mapping(self.event_stub()[0])
        expected = {'cs1': 'FIM halo',
                    'cs1Label': 'policy_name',
                    'cs2': 'Linux',
                    'cs2Label': 'server_platform',
                    'cs3': '5b1d73b63e3711e68ead7f4b70b6c2b8',
                    'cs3Label': 'server_id',
                    'cs4': 'old_smoke',
                    'cs4Label': 'server_group_name',
                    'cs5': {'critical': True,
                            'finding_id': 'e748d9c6688411e6b7b32f750f990d28',
                            'name': 'File Integrity change detected',
                            'scan_id': 'e730037e688411e6b7b32f750f990d28',
                            'server_hostname': 'ip-10-2-20-76',
                            'server_label': 'Jlee-Chef-Node1',
                            'type': 'fim_target_integrity_changed'},
                    'cs5Label': 'extras',
                    'destinationTranslatedAddress': '54.183.177.195',
                    'deviceDirection': 0,
                    'dst': '10.2.20.76',
                    'dvchost': 'localhost',
                    'externalid': 'e750d982688411e6b7b32f750f990d28',
                    'msg': 'A change was detected in file integrity target'
                           '/opt/cloudpassage/*/* on Linux '
                           'serverJlee-Chef-Node1 (54.183.177.195) '
                           '(source: Scan)',
                    'rt': 'Aug 22 2016 16:24:30 UTC'}
        pprint.pprint(cef_mapping)
        assert expected == cef_mapping

    def test_format_cef(self):
        cef = self.create_cef_object()
        cef_format = cef.format_cef(self.event_stub())[0]
        expected = ("CEF:0|CloudPassage|CPHalo|1.0|130|"
                    "File Integrity change detected|9|"
                    "rt=Aug 22 2016 16:24:30 UTC cs4Label=server_group_name "
                    "destinationTranslatedAddress=54.183.177.195 dst=10.2.20.76"  # NOQA
                    " cs5Label=extras dvchost=localhost "
                    "cs2Label=server_platform cs1Label=policy_name "
                    "cs5={'server_hostname': 'ip-10-2-20-76', "
                    "'finding_id': 'e748d9c6688411e6b7b32f750f990d28', "
                    "'name': 'File Integrity change detected', "
                    "'scan_id': 'e730037e688411e6b7b32f750f990d28', "
                    "'server_label': 'Jlee-Chef-Node1', 'critical': True, "
                    "'type': 'fim_target_integrity_changed'} "
                    "externalid=e750d982688411e6b7b32f750f990d28 "
                    "msg=A change was detected in file integrity "
                    "target/opt/cloudpassage/*/* on Linux serverJlee-Chef-Node1"  # NOQA
                    " (54.183.177.195) (source: Scan) cs4=old_smoke "
                    "deviceDirection=0 cs1=FIM halo cs3Label=server_id "
                    "cs3=5b1d73b63e3711e68ead7f4b70b6c2b8 cs2=Linux ")
        assert expected == cef_format
