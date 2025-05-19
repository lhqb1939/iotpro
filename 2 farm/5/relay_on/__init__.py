import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, outputEventHubMessage: func.Out[str]) -> func.HttpResponse:
    logging.info('relay_on trigger processed a request.')

    message = {"command": "relay_on"}
    outputEventHubMessage.set(json.dumps(message))

    return func.HttpResponse("Relay turned ON.", status_code=200)
