from pathlib import Path
import os

home_dir = str(Path.home())
SERVICE_ACCOUNT_PATH = os.path.join(home_dir, '.config', 'firebase', 'service-account.json')

CURRENT_YEAR = [
    "FA25",
    "SU25",
    "SP25",
    "WI25",
]

ALL_SEMESTERS = [
    "SP25",
    "WI25",
    "FA24",
    "SU24",
    "SP24",
    "WI24",
    "FA23",
    "SU23",
    "SP23",
    "WI23",
    "FA22",
    "SU22",
    "SP22",
    "WI22",
    "FA21",
    "SU21",
] 