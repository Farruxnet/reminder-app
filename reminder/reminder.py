from pathlib import Path
import os
import random

BASE_DIR = Path(__file__).resolve().parent.parent


class ReminderApp:

    @property
    def _read_db(self) -> None:
        path = os.path.join(BASE_DIR, "reminder")
        with open(f'{path}/db.txt', 'r') as f:
            data = f.readlines()
        return data

    @property
    def random_word(self):
        word_data = self._read_db
        random_data = random.choice(word_data)
        return random_data
