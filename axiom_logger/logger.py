import axiom
import rfc3339
from datetime import datetime
import json
import os

def getenv_with_error(key):
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} is not set! Provide env variable or pass it as an argument.")
    return value

class TestClient:
    def __init__(self, logger):
        self.logger = logger
    
    def ingest_events(self, dataset, events):
        for event in events:
            func = None
            match event["type"]:
                case "DEBUG":
                    func = self.logger.debug
                case "INFO":
                    func = self.logger.info
                case "WARNING":
                    func = self.logger.warning
                case "ERROR":
                    func = self.logger.error
                case "CRITICAL":
                    func = self.logger.critical
                case _:
                    func = self.logger.error
            func(json.dumps(event, indent=2))

class AxiomLogger:
    def __init__(self, dataset_name, token=None, org_id=None, logger=None):
        if logger is None:
            if token is None:
                token = getenv_with_error("AXIOM_TOKEN")
            if org_id is None:
                org_id = getenv_with_error("AXIOM_ORG_ID")
            self.client = axiom.Client(token, org_id)
        else:
            self.client = TestClient(logger)
        self.dataset_name = dataset_name
        self._use_always = {}
        self.debug = self.function_factory("DEBUG")
        self.info = self.function_factory("INFO")
        self.warning = self.function_factory("WARNING")
        self.error = self.function_factory("ERROR")
        self.critical = self.function_factory("CRITICAL")

    def function_factory(self, log_type):
        def log_function(name, **data):
            status = self.client.ingest_events(
                dataset=self.dataset_name,
                events=[{
                    "type": log_type,
                    "name": name,
                    **self._use_always,
                    **data 
                }]
            )
        return log_function
    
    def time(self):
        time = datetime.utcnow()
        time_formatted = rfc3339.format(time)
        return time_formatted
    
    def add_use_always(self, key, value):
        self._use_always[key] = value

    def remove_use_always(self, key):
        if key in self._use_always:
            del self._use_always[key]

    def clear_use_always(self):
        self._use_always = {}
