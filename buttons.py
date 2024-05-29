import string

from enum import Enum


class Characters(Enum):
    '''
        Variable names MUST BE THE SAME NAME as their own ui objects,
        otherwise it doesn't know which value is associated with the object
    '''
    lower_chkbx = string.ascii_lowercase
    upper_chkbx = string.ascii_uppercase
    digits_chkbx = string.digits
    symbols_chkbx = string.punctuation