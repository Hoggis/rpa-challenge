""" End reporting stuff """


from robot.libraries.BuiltIn import BuiltIn
from libraries.utils import debug, run_kw, get_variable, get_library
import time


class Stage2:

    def main_action(self):
        print("Begin the last stage, waiting for a moment before proceeding...")
        time.sleep(5)
        task_objects = run_kw("Find All Task Objects By Stage", 1)
        filtered_task_objects = self.filter_out_processing_objects(task_objects)
        debug()
        report_temp_location = get_variable("${end_reports_path}")

    def filter_out_processing_objects(self, objects: list) -> list:
        """
        Checks status for each TO returned by find all task objects by stage
        If TO has status 'processing' it should not be reported yet, but in the next run

        For now implementation works only when a single TO is in state processing at the sametime
        In the future if multiple executors of Stage 1 are taken into productions, then remove break statement
        from the if clause in the for loop
        """
        filtered_objects = objects
        for object in objects:
            if object["status"] == "processing":
                filtered_objects.remove(object)
        return filtered_objects


