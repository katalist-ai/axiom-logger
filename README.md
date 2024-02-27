# axiom-logger

Install with
`pip install git+https://github.com/katalist-ai/axiom-logger.git`

Usage:
```python
from axiom_logger import AxiomLogger

token = "your_token"
org_id = "your_org_id"
dataset_name = "your_dataset_name"

logger = AxiomLogger(dataset_name, token, org_id)

logger.info("basic log", text="This is the first log")
logger.info("basic log", text="This is the second log")
logger.info("basic log", text="This is the third log")
```

If you have env variables set for `AXIOM_TOKEN` and `AXIOM_ORG_ID` you can use the following:
```python
from axiom_logger import AxiomLogger

dataset_name = "your_dataset_name"

logger = AxiomLogger(dataset_name)
```

In testing environments, you can set custom logger and pass it to axiom logger
The logger won't send logs to axiom, but you can use it to check if logs are being sent correctly
```python
from axiom_logger import AxiomLogger
import logging

logger = logging.getLogger("axiom_logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

dataset_name = "your_dataset_name"

axiom_logger = AxiomLogger(dataset_name, logger=logger)
```
