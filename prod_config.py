import os


class Config(object):
    LOG_ENABLE = False
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "bb06d4avfb49gc3eeb1aeb98ae0f571e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    USER_SESSION_STRING = os.environ.get("1BVtsOJEBu47-Frjt8X6STxqv4Ke3boHg3EeECRsMJDr717kmOcA7liEKH3uBnadiVcPNraBcKTPGl2s2JNmjxGVemon_m6L4UW5_bTMa-J8MS1FJ45dnhrklhZSdvtvBuXXgCkox4D3k2zvHtW0o5qoSF-TtVpb2yvXCiXby4WXN35HU3DU0HVJ0PP7_6haDGmbomPs-fA13Z25Qq1vbuxt3g0gfqIGGhwGnYX-p9HtdaQ41krPKv3VxKOLrN5ONPzr_dts4sZh8AZ2YVmuIPYv2AMLkohyVuwx3RuVtrDJL32_gUoMsEU64Vte-ThbVny0uVGhW3lQoLb3XFg_fIsHX1Wd4fGo=", None)
    MONGO_DB_URL = os.environ.get("MONGO_DB_URL", None)
    LOG_MAX_FILE_SIZE = 50000000
    STRIP_FILE_NAMES = os.environ.get("STRIP_FILE_NAMES", None)
    TAMILMV_URL = os.environ.get("TAMILMV_URL", None)
    SUDO_USERS = list(set(
        int(x) for x in os.environ.get("SUDO_USERS", "").split()
    ))
