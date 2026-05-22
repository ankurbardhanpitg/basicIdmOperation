from directoryConnection import get_ldap_connection

# -----------------------------
# New User Details
# -----------------------------
USERNAME = "testankurprog1"
FULL_NAME = "Ankur Programmer"
SURNAME = "Programmer"
GIVEN_NAME = "Ankur"
USER_PASSWORD = "Welcome@123"
USER_DN = f"cn={USERNAME},ou=Active,ou=Users,ou=Ankur,o=QuickTraining"


def add_user(conn):
    attributes = {
        "objectClass": [
            "top",
            "person",
            "organizationalPerson",
            "inetOrgPerson",
        ],
        "cn": USERNAME,
        "sn": SURNAME,
        "givenName": GIVEN_NAME,
        "displayName": FULL_NAME,
        "uid": USERNAME,
        "mail": f"{USERNAME}@example.com",
        "userPassword": USER_PASSWORD,
    }

    if conn.add(dn=USER_DN, attributes=attributes):
        print("[SUCCESS] User added successfully")
        return True

    print("[ERROR] Failed to add user")
    print(conn.result)
    return False


def main():
    conn = None
    try:
        conn = get_ldap_connection()
        print("[SUCCESS] LDAP connection established")
        add_user(conn)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        if conn and conn.bound:
            conn.unbind()


if __name__ == "__main__":
    main()
