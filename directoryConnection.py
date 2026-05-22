import ssl

from ldap3 import Server, Connection, ALL, Tls

# -----------------------------
# LDAP Server Details
# -----------------------------
LDAP_HOST = "192.168.1.6"
LDAP_PORT = 636
LDAP_USER = "cn=admin,ou=sa,o=system"
LDAP_PASSWORD = "t6D%pl37"

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
