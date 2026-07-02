import os
import base64
import time
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")

HEADERS = {
    "x-apikey": API_KEY
}


def get_existing_report(url):

    try:

        url_id = base64.urlsafe_b64encode(
            url.encode()
        ).decode().strip("=")

        response = requests.get(

            f"https://www.virustotal.com/api/v3/urls/{url_id}",

            headers=HEADERS,

            timeout=15

        )

        if response.status_code == 200:

            stats = response.json()["data"]["attributes"]["last_analysis_stats"]

            malicious = stats["malicious"]

            suspicious = stats["suspicious"]

            harmless = stats["harmless"]

            score = (
                malicious +
                suspicious
            )

            return {

                "status": "completed",

                "engines": score,

                "malicious": malicious,

                "suspicious": suspicious,

                "harmless": harmless,

                "score": score

            }

        return None

    except Exception:

        return None


def submit_new_scan(url):

    try:

        response = requests.post(

            "https://www.virustotal.com/api/v3/urls",

            headers=HEADERS,

            data={
                "url": url
            }

        )

        if response.status_code != 200:

            return {

                "status": "Unavailable",

                "engines": 0,

                "malicious": 0,

                "suspicious": 0,

                "harmless": 0,

                "score": 0

            }

        analysis = response.json()["data"]["id"]

        for _ in range(10):

            result = requests.get(

                f"https://www.virustotal.com/api/v3/analyses/{analysis}",

                headers=HEADERS

            )

            if result.status_code != 200:

                time.sleep(1)

                continue

            data = result.json()["data"]["attributes"]

            if data["status"] != "completed":

                time.sleep(1)

                continue

            stats = data["stats"]

            return {

                "status": "completed",

                "engines":

                    stats["malicious"] +
                    stats["suspicious"],

                "malicious":

                    stats["malicious"],

                "suspicious":

                    stats["suspicious"],

                "harmless":

                    stats["harmless"],

                "score":

                    stats["malicious"] +
                    stats["suspicious"]

            }

        return {

            "status": "Unavailable",

            "engines": 0,

            "malicious": 0,

            "suspicious": 0,

            "harmless": 0,

            "score": 0

        }

    except Exception:

        return {

            "status": "Unavailable",

            "engines": 0,

            "malicious": 0,

            "suspicious": 0,

            "harmless": 0,

            "score": 0

        }


def check_virustotal(url):

    report = get_existing_report(url)

    if report:

        return report

    return submit_new_scan(url)