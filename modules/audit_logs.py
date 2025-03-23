import os
import json
from datetime import datetime, timedelta

OUTPUT_DIR = "data/audit_logs"

def guardar(nombre, data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, nombre), "w") as f:
        json.dump(data, f, indent=4)

def auditar_eventos(service):
    print("🕵️ Auditando eventos recientes del dominio...")

    eventos_login_sospechoso = []
    cambios_admin = []
    apps_terceros = []
    eventos_drive = []

    ahora = datetime.utcnow()
    hace_7_dias = ahora - timedelta(days=7)
    fecha_inicio = hace_7_dias.strftime("%Y-%m-%dT%H:%M:%SZ")

    def obtener_eventos(applicationName, filtros=None):
        eventos = []
        page_token = None
        while True:
            params = {
                'userKey': 'all',
                'applicationName': applicationName,
                'startTime': fecha_inicio,
                'maxResults': 1000,
                'pageToken': page_token
            }
            if filtros:
                params.update(filtros)

            response = service.activities().list(**params).execute()
            eventos.extend(response.get('items', []))
            page_token = response.get('nextPageToken')
            if not page_token:
                break
        return eventos

    # 1. Eventos de Login
    logins = obtener_eventos("login")
    for e in logins:
        if e.get("events"):
            for ev in e["events"]:
                if ev["name"] in ["failed_login", "login_failure", "suspicious_login", "unauthorized_access"]:
                    eventos_login_sospechoso.append(e)

    # 2. Eventos de administración (admin)
    cambios_admin = obtener_eventos("admin")

    # 3. Eventos de Drive (ej. sharing, delete, etc.)
    eventos_drive = obtener_eventos("drive")

    # 4. Eventos de tokens (OAuth apps)
    apps_terceros = obtener_eventos("token")

    # Guardar resultados
    guardar("logins_sospechosos.json", eventos_login_sospechoso)
    guardar("cambios_admin.json", cambios_admin)
    guardar("apps_terceros.json", apps_terceros)
    guardar("drive_eventos.json", eventos_drive)

    print("✅ Auditoría de eventos finalizada.")