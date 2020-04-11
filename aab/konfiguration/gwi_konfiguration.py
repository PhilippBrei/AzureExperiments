from enum import Enum


class Systeme(Enum):
    C24 = 'C24'
    KGS = 'KGS'
    OBP = 'OBP'
    CPU = 'CPU'
    A360 = 'A360'


class Modus(Enum):
    BELADUNG = 'BELADUNG'
    ENTLADUNG = 'ENTLADUNG'
    FACHLICHER_FILTER = "FACHLICHER_FILTER"


class IntegrationsFluss(Enum):
    C24_BELADE_DARLEHEN = (Systeme.C24, Modus.BELADUNG, "DARLEHEN")
    C24_BELADE_KONTOKORRENT = (Systeme.C24, Modus.BELADUNG, "KONTOKORRENT")
    C24_BELADE_PERSON = (Systeme.C24, Modus.BELADUNG, "PERSON")
    KGS_BELADE_DEPOT = (Systeme.KGS, Modus.BELADUNG, "DEPOT")
    A360_ENTLADE_DARLEHEN = (Systeme.A360, Modus.ENTLADUNG, "DARLEHEN")
