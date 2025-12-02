import re

def get_first_group_total(message_text: str) -> int:
    """Extrait le total du premier groupe (le chiffre avant les parenthèses)"""
    try:
        pattern = r"[✅🔰]?(\d+)\(([^)]+)\)"
        matches = re.findall(pattern, message_text)
        if matches and len(matches) >= 1:
            total = int(matches[0][0])
            print(f"📊 Total du premier groupe: {total}")
            return total
        return -1
    except Exception as e:
        print(f"Erreur get_first_group_total: {e}")
        return -1
