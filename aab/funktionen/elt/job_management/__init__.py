"""Azure Funktion um Jobs inkl. Abhängigkeiten zu steuern"""

import azure.functions as func
import json
import logging


def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()

    if not is_request_valid(req_body):
        return func.HttpResponse(
            "Invalid Request Paramters",
            status_code=400
        )
    else:
        pass

    return func.HttpResponse(
            "Invalid Request Paramters",
            status_code=400
        )


def is_request_valid(req_body):
    pass
