# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.batch.models import BatchErrorException


class MissingParameterValue(ValueError):

    def __init__(self, message, parameter_name=None, parameter_description=None):
        self.parameter_name = parameter_name
        self.parameter_description = parameter_description
        super(MissingParameterValue, self).__init__(message)


class CreateTasksErrorException(BatchErrorException):
    """
    :param str message: Error message describing exit reason
    :param [~TaskAddResult] failures: List of tasks with detected client side errors.
    :param [~TaskAddParameter] pending_task_list: List of tasks remaining to be submitted.
    """
    def __init__(self, message, failures, pending_task_list):
        self.message = message
        self.failures = list(failures)
        self.pending_tasks = list(pending_task_list)
