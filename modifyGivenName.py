from ldap3 import MODIFY_REPLACE

from directoryConnection import get_ldap_connection

# -----------------------------
# User to Modify
# -----------------------------
USERNAME = "jdoedddd"
NEW_GIVEN_NAME = "Jonathan"
USER_DN = f"cn={USERNAME},ou=Active,ou=Users,ou=Ankur,o=QuickTraining"


def modify_given_name(conn):
    changes = {
        "givenName": [(MODIFY_REPLACE, [NEW_GIVEN_NAME])],
    }

    if conn.modify(dn=USER_DN, changes=changes):
        print(f"[SUCCESS] givenName updated to '{NEW_GIVEN_NAME}'")
        return True

    print("[ERROR] Failed to modify givenName")
    print(conn.result)
    return False


def main():
    conn = None
    try:
        conn = get_ldap_connection()
        print("[SUCCESS] LDAP connection established")
        modify_given_name(conn)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        if conn and conn.bound:
            conn.unbind()


if __name__ == "__main__":
    main()
