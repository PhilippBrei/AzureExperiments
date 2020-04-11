import logging
from datetime import date

from aab.konfiguration.gwi_konfiguration import IntegrationsFluss

class IntegrationsLauf:

    def __init__ (self, stichtag, laufnummer):
        self.__stichtag = stichtag
        self.__laufnummer = laufnummer

    @property
    def stichtag(self):
        return self.__stichtag
    
    @property
    def laufnummer (self):
        return self.__laufnummer



class AABFachlicherFilter(logging.Filter):

    def filter(self, record):
        integrationsfluss:IntegrationsFluss = record.args[0]
        integrationslauf:IntegrationsLauf = record.args[1]
        if not isinstance(integrationsfluss, IntegrationsFluss):
            raise ValueError("Arg[0] muss vom typ " + str(type(IntegrationsFluss)) + " sein, ist aber" + str(type(integrationsfluss)))

        if not isinstance(integrationslauf, IntegrationsLauf):
            raise ValueError("Arg[1] muss vom typ date sein, ist aber" + str(type(integrationslauf)))

        record.integrations_fluss = integrationsfluss.name
        record.integrationslauf_stichtag = integrationslauf.stichtag
        record.integrationslauf_laufnummer = integrationslauf.laufnummer

        record.args = []
        return True
