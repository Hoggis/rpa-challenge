"""Example Producer stage of an RPA process.

This is a template to be used as the starting point for RPA development.
Replace all docstrings in this module with your own when implementing the stage
(including this one).
"""
from urllib import request
import requests
import json
import pandas as pd
from robot.api import logger
from robot.api.deco import keyword
from RPALibrary.stages.Producer import Producer

from libraries.utils import debug, run_kw, get_variable, get_library


class Stage0(Producer):
    """Stage class inherits either RPALibrary.stages.Producer or RPALibrary.stages.Consumer
    and is named according to its place in the overall process sequence
    (starting from ``Stage0.py``, followed by ``Stage1.py`` etc.).

    Typically, the first stage (numbered 0) is a Producer.
    Implement ``process_data`` and, optionally, ``preloop_action``, ``postprocess_data`` for creating task objects.
    Call ``main loop`` from Robot script:

    .. code:: robotframework

        Library  ../stages/Stage0.py

        *** Tasks ***
        My Producer Stage
            [Tags]    stage_0
            [Setup]    Stage0.Setup
            Stage0.Main Loop
            [Teardown]    Stage0.Teardown
    """

    def __init__(self):
        super().__init__()
        self.download_url = get_variable("${download_url}")


    def preloop_action(self):
        """Prefetch data to iterate in ``process_data``.
        This method should return a sequence (list, tuple) or a generator.

        Implementation is optional, but needed in most processes. See ``RPALibrary.stages.Producer`` for details.
        """
        response = requests.get(self.download_url)
        with open('./csv/challenge.xlsx', 'wb') as output:
            output.write(response.content)
        data = []
        df = pd.read_excel(
            get_variable("${input_file_path}"),
        )
        df.columns = df.columns.str.replace(' ', '')
        result = df.to_json(orient="records")
        data = json.loads(result)
        return data

    def process_data(self, item):
        """Define how the data is turned into a task object.
        Task object(s) are created from the return value of this method.

        Implementation is mandatory. See ``RPALibrary.stages.Producer`` for details.
        """
        return item






