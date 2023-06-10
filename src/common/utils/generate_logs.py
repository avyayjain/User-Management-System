import logging

logging.basicConfig(
    filename="error.log",
    format="%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s",
    level=logging.INFO,
)

from typing import Dict, List


def generate_details(message: str, error_type: str) -> List[Dict[str, str]]:
    """ Help in create response in case of errors """
    details = [{"msg": message, "type": str(error_type)}]

    return details