import json
import os
import re
import time

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


class Status(str):
    SUBMITTED = "esriJobSubmitted"
    EXECUTING = "esriJobExecuting"
    SUCCEEDED = "esriJobSucceeded"


class Mode(str):
    SYNC = "sync"
    ASYNC = "async"


class Config(str):
    INTERLIS = "INTERLIS"
    ESRI = "ESRI"
    ORACLE = "ORACLE"


class Result(object):
    def __init__(
        self,
        jobid: str = None,
        logfile: str = None,
        success: bool = None,
        valid: bool = None,
    ):
        self.jobid = jobid
        self.logfile = logfile
        self.success = success
        self.valid = valid


class Checker:
    """Checks Interlis1 or Interlis2 files on server with rest-service.
    Neither error handling is implemented nor user inputs will be checked.
    """

    def __init__(
        self,
        check_url: str = None,
        scratch_url: str = None,
        server: str = "ltetl.adr.admin.ch:6443",
    ):
        self.__check_url = (
            check_url
            if check_url is not None
            else f"https://{server}/arcgis/rest/services/Quality/InterlisChecker/GPServer/InterlisChecker"
        )
        self.__scratch_url = (
            scratch_url
            if scratch_url is not None
            else f"https://{server}/arcgis/rest/services/swisstopoUtilities/AgsScratchFolder/GPServer/AgsScratchFolder/execute"
        )

    def __get_scratch(self) -> str:
        """Returns the scratch workspace of the server."""
        session = requests.Session()
        session.trust_env = False
        response = session.get(
            url=self.__scratch_url,
            params={"f": "json"},
            verify=False,
        )
        return json.loads(response.text)["results"][0]["value"]

    def get_status(
        self,
        jobid: str,
        min_wait: int = 5,
        max_wait: int = 3600,
    ) -> Result:
        """Returns the status of the rest job."""
        job_url = self.__check_url + "/jobs/" + jobid
        loop = 0
        while True:
            loop += 1
            session = requests.Session()
            session.trust_env = False
            response = session.get(
                url=job_url,
                params={"f": "json"},
                verify=False,
            ).json()

            job_status = response.get("jobStatus")

            if job_status == Status.SUCCEEDED or loop * min_wait > max_wait:
                break
            elif job_status in [Status.SUBMITTED, Status.EXECUTING]:
                time.sleep(min_wait)
            else:
                break

        # Check Result
        result = Result(jobid=jobid)
        if job_status == Status.SUCCEEDED:
            messages = [m.get("description") for m in response.get("messages")]
            matches = [
                m
                for m in messages
                if re.search("completed with no (errors|warnings|infos)", m)
            ]
            if len(matches) == 3:
                result.success = True
                result.valid = True
            else:
                result.success = True
                result.valid = False
        else:
            result.success = False
            result.valid = None
        return result

    def run_check(
        self,
        xtf: str,
        ili: str,
        mode: Mode = Mode.SYNC,
        config: Config = Config.ESRI,
        comment: str = os.environ["USERNAME"],
        email: str = "#",
    ) -> Result:
        """Execute interlis check with rest service."""

        # declate parameter
        submit_url = self.__check_url + "/submitJob"
        parameter = {
            "InputFile": xtf,
            "InputModel": ili,
            "Config": config,
            "email": email,
            "comment": comment,
            "f": "json",
        }

        # submit job
        session = requests.Session()
        session.trust_env = False
        response = session.get(
            url=submit_url,
            params=parameter,
            verify=False,
        ).json()

        # read response messages
        # job_status = response["jobStatus"]
        jobid = response["jobId"]

        # get logfile path
        logfile = os.path.join(
            self.__get_scratch(),
            "quality",
            "interlischecker_gpserver",
            jobid,
            "scratch",
            os.path.splitext(os.path.basename(xtf.split(",")[0]))[0] + ".log",
        )

        if mode == Mode.ASYNC:
            result = Result(jobid=jobid, logfile=logfile)
        else:
            # wait until job finished
            result = self.get_status(jobid)
            result.logfile = logfile

        return result
