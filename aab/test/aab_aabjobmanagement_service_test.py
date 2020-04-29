import unittest

from aab.funktionen.elt.job_management.job_manager import AABJobManagementService
from azure.storage.queue.queueservice import QueueService

class MyTestCase(unittest.TestCase):

    def test_job_management_service(self):
        service = AABJobManagementService (__create_azure_dao__(), "aabtestqueue")
        service.schreibe_entity_beladung_abgeschlossen(None,None,None,None)





def __create_azure_dao__():
    return QueueService (connection_string="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;")


if __name__ == '__main__':
    unittest.main()