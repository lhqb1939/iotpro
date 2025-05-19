import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, outputEventHubMessage: func.Out[str]) -> func.HttpResponse:
    logging.info('relay_off trigger processed a request.')

    message = {"command": "relay_off"}
    outputEventHubMessage.set(json.dumps(message))

    return func.HttpResponse("Relay turned OFF.", status_code=200)
