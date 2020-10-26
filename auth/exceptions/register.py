from rest_framework.exceptions import APIException


class RegisterRequiredData(APIException):
    status_code = 422
    default_detail = "Required one or more parameters"
    default_code = 'register_required_data'
