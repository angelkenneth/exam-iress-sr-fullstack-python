from app.shared.exception import MessagedException


class InvalidCommandArgument(MessagedException):
    pass


class UnknownCommandException(MessagedException):
    def __init__(self, command):
        self.command = command

    def __str__(self):
        return f"Unknown command: {self.command}"
