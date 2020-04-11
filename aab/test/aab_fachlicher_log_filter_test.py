import unittest
from logging import LogRecord

from aab.logging.AABFilter import AABFachlicherFilter
from aab.konfiguration.gwi_konfiguration import IntegrationsFluss
from aab.logging.AABFilter import IntegrationsLauf
from datetime import datetime

class MyTestCase(unittest.TestCase):

    def test_invalid_paramter(self):
        fl = AABFachlicherFilter()
        log = LogRecord(name=None, level=None, lineno=None, exc_info=None, args="Hallo", msg="Nachricht", pathname="Pfad")
        valueError_raised  = None
        try:
            fl.filter(fl.filter(log))
            valueError_raised = None
        except ValueError as err:
            valueError_raised = err
        self.assertIsInstance(valueError_raised, ValueError)
        return None

    def test_valid_paramter (self):
        fl = AABFachlicherFilter()
        log = LogRecord(name=None, level=None, lineno=None, exc_info=None, args=[IntegrationsFluss.A360_ENTLADE_DARLEHEN, IntegrationsLauf(datetime(2020, 4, 1), 1)], msg="Nachricht", pathname="Pfad")
        valueError_raised  = None
        try:
            fl.filter(fl.filter(log))
            valueError_raised = None
        except ValueError as err:
            valueError_raised = err
        self.assertIsNone(valueError_raised)
        return None



if __name__ == '__main__':
    unittest.main()
