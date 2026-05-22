from ldap3 import SUBTREE

from directoryConnection import get_ldap_connection

# -----------------------------
# Dynamic Group Details
# -----------------------------
GROUP_NAME = "HRDynamicGroup"
GROUP_DESCRIPTION = "Group for Active users with title=HR"
GROUP_BASE = "ou=Groups,ou=Ankur,o=QuickTraining"
GROUP_DN = f"cn={GROUP_NAME},{GROUP_BASE}"

MEMBER_SEARCH_BASE = "ou=Active,ou=Users,ou=Ankur,o=QuickTraining"
MEMBER_FILTER = "(title=HR)"


def find_matching_member_dns(conn):
    conn.search(
        search_base=MEMBER_SEARCH_BASE,
        search_filter=MEMBER_FILTER,
        search_scope=SUBTREE,
        attributes=["cn"],
    )
    return [entry.entry_dn for entry in conn.entries]


def add_dynamic_group(conn):
    member_dns = find_matching_member_dns(conn)

    attributes = {
        "objectClass": ["top", "group"],
        "cn": GROUP_NAME,
        "description": GROUP_DESCRIPTION,
    }
    if member_dns:
        attributes["member"] = member_dns

    if conn.add(dn=GROUP_DN, attributes=attributes):
        print(f"[SUCCESS] Group '{GROUP_NAME}' created successfully")
        print(f"  Filter: {MEMBER_FILTER} under {MEMBER_SEARCH_BASE}")
        if member_dns:
            print(f"  Members added ({len(member_dns)}):")
            for dn in member_dns:
                print(f"    - {dn}")
        else:
            print("  No matching users found yet; re-run after users have title=HR")
        return True

    print("[ERROR] Failed to create dynamic group")
    print(conn.result)
    return False


def main():
    conn = None
    try:
        conn = get_ldap_connection()
        print("[SUCCESS] LDAP connection established")
        add_dynamic_group(conn)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        if conn and conn.bound:
            conn.unbind()


if __name__ == "__main__":
    main()
