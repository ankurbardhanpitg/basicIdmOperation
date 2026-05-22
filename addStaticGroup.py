from directoryConnection import get_ldap_connection

# -----------------------------
# New Static Group Details
# -----------------------------
GROUP_NAME = "TestStaticProgGroup1"
GROUP_DESCRIPTION = "Static group created via script"
GROUP_BASE = "ou=Groups,ou=Ankur,o=QuickTraining"
GROUP_DN = f"cn={GROUP_NAME},{GROUP_BASE}"

# Optional: add member user DNs when creating the group
MEMBERS = [
    # "cn=testankurprog1,ou=Active,ou=Users,ou=Ankur,o=QuickTraining",
]


def add_static_group(conn):
    attributes = {
        "objectClass": ["top", "group"],
        "cn": GROUP_NAME,
        "description": GROUP_DESCRIPTION,
    }

    if MEMBERS:
        attributes["member"] = MEMBERS

    if conn.add(dn=GROUP_DN, attributes=attributes):
        print(f"[SUCCESS] Static group '{GROUP_NAME}' created successfully")
        return True

    print("[ERROR] Failed to create static group")
    print(conn.result)
    return False


def main():
    conn = None
    try:
        conn = get_ldap_connection()
        print("[SUCCESS] LDAP connection established")
        add_static_group(conn)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        if conn and conn.bound:
            conn.unbind()


if __name__ == "__main__":
    main()
