class BaseCommand:
    def __init__(self, *args):
        pass

    @classmethod
    def validate_or_raise(cls, *args):
        return cls(*args)
