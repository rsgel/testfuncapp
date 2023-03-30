import logging
import json
import socket
import getpass
import os
from requests import get
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    ip_address = req.headers.get('X-Forwarded-For')
    return func.HttpResponse(f"Hello! Your IP address is {ip_address}")
