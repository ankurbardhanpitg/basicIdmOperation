from ldap3 import MODIFY_ADD

from directoryConnection import get_ldap_connection

# -----------------------------
# Group and Member Details
# -----------------------------
GROUP_NAME = "TestStaticProgGroup1"
GROUP_BASE = "ou=Groups,ou=Ankur,o=QuickTraining"
GROUP_DN = f"cn={GROUP_NAME},{GROUP_BASE}"

MEMBER_DN = "cn=testankurprog1,ou=Active,ou=Users,ou=Ankur,o=QuickTraining"


def add_group_member(conn):
    changes = {
        "member": [(MODIFY_ADD, [MEMBER_DN])],
    }

    if conn.modify(dn=GROUP_DN, changes=changes):
        print(f"[SUCCESS] Member added to group '{GROUP_NAME}'")
        print(f"  Member: {MEMBER_DN}")
        return True

    print("[ERROR] Failed to add member to group")
    print(conn.result)
    return False


def main():
    conn = None
    try:
        conn = get_ldap_connection()
        print("[SUCCESS] LDAP connection established")
        add_group_member(conn)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        if conn and conn.bound:
            conn.unbind()


if __name__ == "__main__":
    main()
