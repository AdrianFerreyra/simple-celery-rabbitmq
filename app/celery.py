from celery import Celery

USERNAME = "default_user_t9xO6TWH-eJaBeoIrdE"
PASSWORD = "Lk7RPsn5Rzm84awDGjMnpgniHVokuTdM"

app = Celery(
    "tasks",
    broker=f"pyamqp://{USERNAME}:{PASSWORD}@localhost:5672",
    backend="redis://localhost:6379",
)
