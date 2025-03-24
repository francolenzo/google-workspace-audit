import os
import json

OUTPUT_DIR = "data/email_security"

def guardar(nombre, data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, nombre), "w") as f:
        json.dump(data, f, indent=4)

def auditar_seguridad_email(gmail_service, users):
    print("📧 Auditando configuración de seguridad de Gmail...")

    delegaciones = []
    reenvios_externos = []
    imap_pop_habilitado = []

    for user in users:
        email = user['primaryEmail']
        try:
            # Delegaciones
            delegates = gmail_service.users().settings().delegates().list(userId=email).execute()
            if delegates.get('delegates'):
                delegaciones.append({"user": email, "delegates": delegates['delegates']})

            # Reenvíos automáticos
            forwarding = gmail_service.users().settings().forwardingAddresses().list(userId=email).execute()
            for addr in forwarding.get('forwardingAddresses', []):
                if not addr.get('verificationStatus') == 'accepted':
                    continue
                if not email.endswith(addr['forwardingEmail'].split('@')[-1]):
                    reenvios_externos.append({"user": email, "to": addr['forwardingEmail']})

            # IMAP/POP
            imap = gmail_service.users().settings().imap().get(userId=email).execute()
            pop = gmail_service.users().settings().pop().get(userId=email).execute()
            if imap.get("enabled") or pop.get("accessWindow") != "disabled":
                imap_pop_habilitado.append({"user": email, "imap": imap.get("enabled"), "pop": pop.get("accessWindow")})

        except Exception as e:
            print(f"⚠️ No se pudo auditar {email}: {e}")

    guardar("delegaciones.json", delegaciones)
    guardar("reenvios_externos.json", reenvios_externos)
    guardar("imap_pop.json", imap_pop_habilitado)

    print("✅ Auditoría de seguridad de email completada.")