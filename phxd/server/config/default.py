import logging


################################################################################
# database configuration
################################################################################

DB_TYPE = 'sqlite'
DB_ARG = 'phxd.db'

################################################################################
# logging configuration
################################################################################

LOG_FILE = None
LOG_LEVEL = logging.DEBUG

################################################################################
# server configuration
################################################################################

SERVER_PORTS = (5500,)
SERVER_NAME = "my_phxd_server"
IDLE_TIME = 10 * 60
BAN_TIME = 15 * 60

################################################################################
# SSL configuration
################################################################################

ENABLE_SSL = False
SSL_PORT = 5600
SSL_KEY_FILE = 'certs/privkey.pem'
SSL_CERT_FILE = 'certs/cacert.pem'

################################################################################
# tracker configuration
################################################################################

ENABLE_TRACKER_REGISTER = False
TRACKER_ADDRESS = "tracker.example.com"
TRACKER_PORT = 5499
TRACKER_PASSWORD = ""
TRACKER_INTERVAL = 5 * 60
SERVER_DESCRIPTION = "My phxd server."

################################################################################
# chat options
################################################################################

# filled with (nick, chat)
CHAT_FORMAT = "\r%13.13s:  %s"
CHAT_PREFIX_LEN = 17
CHAT_PREFIX_ADD_NICK_LEN = False
EMOTE_FORMAT = "\r *** %s %s"
EMOTE_PREFIX_LEN = 7  # + len(nick)
MAX_NICK_LEN = 32
MAX_CHAT_LEN = 4096
LOG_CHAT = True
LOG_DIR = "chatlogs"

################################################################################
# message options
################################################################################

MAX_MSG_LEN = 2048

################################################################################
# news options
################################################################################

# filled with (nick, login, date, body)
NEWS_FORMAT = "From %s [%s] (%s):\r\r%s\r_________________________________________________________\r"
DEFAULT_NEWS_LIMIT = 25

################################################################################
# files options
################################################################################

FILE_ROOT = "files"
SHOW_DOTFILES = False
DIR_UMASK = 0o755
UPLOAD_SCRIPT = None

################################################################################
# transfer options
################################################################################

XFER_TIMEOUT = 30.0

################################################################################
# GIF icon options
################################################################################

ENABLE_GIF_ICONS = True
MAX_GIF_SIZE = 32768
DEFAULT_ICON_TIME = 10
