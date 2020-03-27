import logging

from enum import Enum

from azure_storage_logging.handlers import TableStorageHandler


class UmgebungsModus (Enum):
    LOKAL = 'LOKAL'
    CLOUD_PRODUKTION = 'CLOUD_PROD'
    CLOUD_TEST = 'CLOUD_TEST'

class Umgebungskonfiguration (object):
    def Umgebungsmodus (self):
        return UmgebungsModus.CLOUD_PRODUKTION

class AzureKonfiguration (object):
    StorageAccountName = ""
    StorageAccountKey = ""

def getAabLogger ():
    if (Umgebungskonfiguration().Umgebungsmodus == UmgebungsModus.CLOUD_PRODUKTION):
        azureKonfiguration = AzureKonfiguration()
        tableStorageHandler = TableStorageHandler(account_name=azureKonfiguration.StorageAccountName,
        account_key=azureKonfiguration.StorageAccountKey, extra_properties=(
            '%(levelname)s', '%(Prozess)s'
        ))
        return tableStorageHandler
    else:
        return logging.basicConfig (filename=) 

