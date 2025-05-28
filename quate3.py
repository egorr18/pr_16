from abc import ABC, abstractmethod

# інтерфейс ISP та DIP
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# різні сповіщення

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending EMAIL: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class PushNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending PUSH notification: {message}")

# Високорівневий модуль, який залежить від абстракції Notifier
class NotificationService:
    def __init__(self, notifiers: list[Notifier]):
        self.notifiers = notifiers

    def notify_all(self, message: str):
        for notifier in self.notifiers:
            notifier.send(message)

if __name__ == "__main__":
    notifiers = [
        EmailNotifier(),
        SMSNotifier(),
        PushNotifier()
    ]

    service = NotificationService(notifiers)
    service.notify_all("Увага! Нова подія в системі.")
