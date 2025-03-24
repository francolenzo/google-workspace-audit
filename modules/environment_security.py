import os
import json
from googleapiclient.errors import HttpError

OUTPUT_DIR = "data/environment_security"

def guardar(nombre, data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, nombre), "w") as f:
        json.dump(data, f, indent=4)

def auditar_configuracion_entorno(directory_service, reports_service):
    print("☁️ Auditando configuración general del entorno...")

    resultados = {
        "verificacion_en_2_pasos_enforced": "No determinado",
        "apps_terceros_detectadas": [],
        "comparticion_externa_detectada": False
    }

    # 🔐 1. 2FA Enforcement
    try:
        response = directory_service.users().list(customer='my_customer', maxResults=1).execute()
        users = response.get('users', [])
        if users and users[0].get('isEnforcedIn2Sv'):
            resultados["verificacion_en_2_pasos_enforced"] = "Sí (por usuario muestreado)"
        else:
            resultados["verificacion_en_2_pasos_enforced"] = "No (en usuario muestreado)"
    except Exception as e:
        resultados["verificacion_en_2_pasos_enforced"] = f"Error al consultar: {str(e)}"

    # 🚫 2. Apps de terceros (token usage detectado)
    try:
        token_events = reports_service.activities().list(
            userKey='all',
            applicationName='token',
            maxResults=100
        ).execute()

        apps_detectadas = set()
        for event in token_events.get('items', []):
            for ev in event.get('events', []):
                app_name = ev.get('parameters', [{}])[0].get('value')
                if app_name:
                    apps_detectadas.add(app_name)

        resultados["apps_terceros_detectadas"] = list(apps_detectadas)

    except HttpError as e:
        resultados["apps_terceros_detectadas"] = [f"Error al consultar tokens: {str(e)}"]

    # 🌍 3. Compartición fuera del dominio (inferencia del módulo 3)
    try:
        drive_data_path = "data/dlp_sharing/externos.json"
        if os.path.exists(drive_data_path):
            with open(drive_data_path) as f:
                externos = json.load(f)
                resultados["comparticion_externa_detectada"] = len(externos) > 0
        else:
            resultados["comparticion_externa_detectada"] = "Sin datos - módulo 3 no ejecutado aún"
    except Exception as e:
        resultados["comparticion_externa_detectada"] = f"Error al leer archivos: {str(e)}"

    guardar("configuracion_seguridad.json", resultados)
    print("✅ Auditoría mejorada del entorno finalizada.")