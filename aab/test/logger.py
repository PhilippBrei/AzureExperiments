"""Für remote Testauführung"""

import logging


from azure_storage_logging.handlers import TableStorageHandler
from aab.konfiguration.gwi_konfiguration import IntegrationsFluss
from aab.logging.aab_filter import IntegrationsLauf, AABFachlicherFilter
from datetime import datetime


class AzureKonfiguration(object):
    StorageAccountName = '-'
    StorageAccountKey = '-'


def get_aab_logger(_name=None):
    azure_konfiguration = AzureKonfiguration()
    table_storage_handler = TableStorageHandler(
        account_name=azure_konfiguration.StorageAccountName,
        account_key=azure_konfiguration.StorageAccountKey,
        extra_properties=['%(hostname)s', '%(levelname)s', '%(integrations_fluss)s', '%(integrationslauf_stichtag)s', '%(integrationslauf_laufnummer)s'])
    logger = logging.getLogger(_name)
    logger.addHandler(table_storage_handler)
    logger.addFilter(AABFachlicherFilter())
    return logger


if __name__ == "__main__":
    log = get_aab_logger("Logger")
    log.warning("Hallo", IntegrationsFluss.A360_ENTLADE_DARLEHEN,
                IntegrationsLauf(datetime(2020, 4, 1), 1))
