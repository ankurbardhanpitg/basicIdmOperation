import os
import ssl

from dotenv import load_dotenv
from ldap3 import Server, Connection, ALL, Tls

load_dotenv()

# -----------------------------
# LDAP Server Details
# -----------------------------
LDAP_HOST = os.getenv("LDAP_HOST")
LDAP_PORT = int(os.getenv("LDAP_PORT", "636"))
LDAP_USER = os.getenv("LDAP_USER")
LDAP_PASSWORD = os.getenv("LDAP_PASSWORD")

tls_config = Tls(
    validate=ssl.CERT_NONE,  # test only
    version=ssl.PROTOCOL_TLSv1_2,
    ciphers="ALL",
)


def get_ldap_connection():
    server = Server(
        host=LDAP_HOST,
        port=LDAP_PORT,
        use_ssl=True,
        tls=tls_config,
        get_info=ALL,
    )
    conn = Connection(
        server,
        user=LDAP_USER,
        password=LDAP_PASSWORD,
        auto_bind=True,
    )
    return conn
