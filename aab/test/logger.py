import logging

from enum import Enum

from azure_storage_logging.handlers import TableStorageHandler
from aab.konfiguration.gwi_konfiguration import IntegrationsFluss
from aab.logging.AABFilter import IntegrationsLauf, AABFachlicherFilter
from datetime import datetime


class AzureKonfiguration(object):
    StorageAccountName = '-'
    StorageAccountKey = '-'


def getaablogger(_name=None):
    azureKonfiguration = AzureKonfiguration()
    tableStorageHandler = TableStorageHandler(
        account_name=azureKonfiguration.StorageAccountName,
        account_key=azureKonfiguration.StorageAccountKey,
        extra_properties=['%(hostname)s', '%(levelname)s', '%(integrations_fluss)s', '%(integrationslauf_stichtag)s', '%(integrationslauf_laufnummer)s'])
    logger = logging.getLogger(_name)
    logger.addHandler(tableStorageHandler)
    logger.addFilter(AABFachlicherFilter())
    return logger


if __name__ == "__main__":
    log = getaablogger("Logger")
    log.warning("Hallo", IntegrationsFluss.A360_ENTLADE_DARLEHEN,
                IntegrationsLauf(datetime(2020, 4, 1), 1))
