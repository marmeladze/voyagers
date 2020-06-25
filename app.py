import config
from containers import Logger, Session, Application, Command, Settings
from custom_logger import log
import boot
from stories import *


settings = Settings(
    editor_lines     = config.editor_lines, 
    notes_folder     = config.notes_path, 
    logs_folder      = config.logs_path,
    date_format      = config.date_format,
    date_time_format = config.date_time_format
)

mappings = Command(bucket={
    "_AUTH": auth_user_story,
    "_MAIN_PAGE": main_page_story,
    "GEO": get_geolocation_info_story,
    "CHEM": chemical_training_story,
    "TN": take_note_story,
    "SN": search_note_story,
    "RN": read_note_story,
    "SB": search_book_at_gutenberg_story,
    "RB": get_book_from_gutenberg_story,
})


logs_path = boot.prepare_logger(
    logs_path   = settings.logs_folder, 
    date_format = settings.date_format
)


logger = Logger(
    log=(lambda msg: log(msg, level="INFO", path=logs_path, date_time_format=settings.date_time_format))
)
session = Session(
    variables={'last_login': ''}
)

app = Application(
    name="Time Traveler's Terminal", 
    logger=logger, 
    session=session, 
    mappings=mappings, 
    settings=settings
)



auth_user_story(app)
main_page_story(app)

while True:
    action = app.session.variables['last_action']
    try:
        app.mappings.bucket[action](app)
    except Exception as e:
        raise e
        break
