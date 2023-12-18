# Importing libraries
from typing import Any, Optional
from fastapi import HTTPException, status
from dtos.base_dto import BaseResponseModel, BaseErrorModel
import i18n

class APIHelper:
    # Send success response with custom message
    def send_error_response(errorMessageKey: Optional[str] = None, locale: Optional[str] = "en"):
        error_model = BaseErrorModel(error=i18n.t(key=errorMessageKey or 'translation.FAILURE', locale=locale))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_model.model_dump()
        )

    # Send unauthorized response with custom message
    def send_unauthorized_error(errorMessageKey: Optional[str] = None, locale: Optional[str] = "en"):
        error_model = BaseErrorModel(error=i18n.t(key=errorMessageKey or 'translation.FAILURE', locale=locale))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=error_model.model_dump()
        )

    # Send error response with custom message
    def send_success_response(data: Optional[Any] = None, successMessageKey: Optional[str] = None, locale: Optional[str] = "en"):
        return BaseResponseModel(data=data, message=i18n.t(key=successMessageKey or 'translation.SUCCESS', locale=locale))
