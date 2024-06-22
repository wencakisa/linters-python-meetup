import random
from utils import get_title

tools=[
    "flake8",'isort',    "black",



'ruff'
]




selected_tool = random.choice(tools)

title = get_title()

from datetime import datetime, timedelta


def get_today(arg):
    today = datetime.now().date()



print(f"{title} - {selected_tool}")
