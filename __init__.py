from flask import Flask

app = Flask(__name__)

from app import routes
from app import clicks
from app import CreateChange
from app import send_data_change_page
from app import user_click
from app import get_user_click_info
from app import get_devices
from app import get_pages
from app import Clicks_Loads_sg
from app import get_browser
from app import get_game_time
from app import set_game_time
from app import get_response_loads