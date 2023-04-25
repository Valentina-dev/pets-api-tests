import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class APIService:
    BASE_URL = "https://petstore.swagger.io/v2"

    def _request(
        self,
        method: str,
        route: str,
        body: dict = None,
        headers: dict = None,
        params=None,
        files=None,
    ) -> requests.Response:
        logger.info(
            f"[REQUEST][{method.upper()}] URL: {self.BASE_URL+route} | Body: {body}"
        )
        response = requests.request(
            method,
            self.BASE_URL + route,
            json=body,
            headers=headers,
            params=params,
            verify=False,
            files=files,
        )
        logger.info(f"[RESPONSE][{response.status_code}] {response.text[:128]}")
        return response
