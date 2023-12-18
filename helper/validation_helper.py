import i18n
import re
from config.constants import Constants


class ValidationHelper:
    def is_valid_email(cls, v):
        if not re.fullmatch(Constants.EMAIL_REGEX, v):
            raise ValueError(i18n.t(key='translation.INVALID_EMAIL'))
        return v

    def is_mobile(cls, v):
        if not re.fullmatch(Constants.MOBILE_NUMBER_REGEX, v):
            raise ValueError(i18n.t(key='translation.INVALID_MOBILE'))
        return v

    def is_valid_password(cls, v):
        if not re.fullmatch(Constants.PASSWORD_REGEX, v):
            raise ValueError(i18n.t(key='translation.INVALID_PASSWORD'))
        return v