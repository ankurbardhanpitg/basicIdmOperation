from directoryConnection import get_ldap_connection

# -----------------------------
# User to Delete
# -----------------------------
USERNAME = "jdoedddd"
USER_DN = f"cn={USERNAME},ou=Active,ou=Users,ou=Ankur,o=QuickTraining"


def delete_user(conn):
    if conn.delete(dn=USER_DN):
        print(f"[SUCCESS] User '{USERNAME}' deleted successfully")
        return True

    print("[ERROR] Failed to delete user")
    print(conn.result)
    return False


def main():
    conn = None
    try:
        conn = get_ldap_connection()
        print("[SUCCESS] LDAP connection established")
        delete_user(conn)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        if conn and conn.bound:
            conn.unbind()


if __name__ == "__main__":
    main()
