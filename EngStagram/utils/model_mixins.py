class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_fields, getattr(self, str_fields, None)) for str_fields in self.str_fields]
        return ', '.join(f'{name}={value}' for (name, value) in fields)