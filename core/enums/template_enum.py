from enum import Enum


class TemplateEnum(Enum):
    REGISTER = ('Register', 'register.html')

    def __init__(self, name_subject, template_name):
        self.name_subject = name_subject
        self.template_name = template_name
