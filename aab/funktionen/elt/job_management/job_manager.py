from azure.storage.queue.queueservice import QueueService


class AABJobManagementService(object):

    def __init__(self, queueService: QueueService, queue_name="AAB_QUEUE"):
        self.queue_service = queueService
        self.queue_name = queue_name

    def schreibe_entity_beladung_abgeschlossen(self, entity, system, stichtage, laufnummer):
        queue_service: QueueService = self.queue_service
        queue_service.put_message(self.queue_name, "Hallo")
        pass



if __name__ == "__main__":
    pass
