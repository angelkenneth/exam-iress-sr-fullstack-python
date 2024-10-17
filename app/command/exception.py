from app.exception.exception import MessagedException


class InvalidCommandArgumentException(MessagedException):
    pass


class UnknownCommandException(MessagedException):
    def __init__(self, command: str):
        super().__init__(f"Unknown command: {command}")
