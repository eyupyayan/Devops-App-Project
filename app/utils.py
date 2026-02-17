from datetime import datetime, timezone
import socket

def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def hostname() -> str:
    return socket.gethostname()
