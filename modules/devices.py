import os
import json
from datetime import datetime

OUTPUT_DIR = "data/devices"

def guardar(nombre, data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, nombre), "w") as f:
        json.dump(data, f, indent=4)

def auditar_dispositivos(service):
    print("📱 Auditando dispositivos móviles...")

    dispositivos_moviles = []
    page_token = None
    while True:
        response = service.mobiledevices().list(customerId='my_customer', projection='FULL', maxResults=100, pageToken=page_token).execute()
        dispositivos_moviles.extend(response.get('mobiledevices', []))
        page_token = response.get('nextPageToken')
        if not page_token:
            break

    print(f"📦 Total de dispositivos móviles encontrados: {len(dispositivos_moviles)}")

    no_cifrados = []
    sin_screenlock = []
    rooteados = []
    incumplimiento = []

    for d in dispositivos_moviles:
        if d.get("encryptionStatus") != "ENCRYPTED":
            no_cifrados.append(d)
        if d.get("screenLockEnabled") is False:
            sin_screenlock.append(d)
        if d.get("isJailbroken") or d.get("isRooted"):
            rooteados.append(d)
        if d.get("complianceStatus") != "COMPLIANT":
            incumplimiento.append(d)

    guardar("todos_los_dispositivos_moviles.json", dispositivos_moviles)
    guardar("no_cifrados.json", no_cifrados)
    guardar("sin_screenlock.json", sin_screenlock)
    guardar("rooteados_o_jailbreak.json", rooteados)
    guardar("incumplen_politicas.json", incumplimiento)

    print("💻 Auditando dispositivos ChromeOS...")

    chromeos = []
    try:
        page_token = None
        while True:
            res = service.chromeosdevices().list(customerId='my_customer', maxResults=100, pageToken=page_token).execute()
            chromeos.extend(res.get('chromeosdevices', []))
            page_token = res.get('nextPageToken')
            if not page_token:
                break
    except Exception as e:
        print("⚠️ No se pudo obtener dispositivos ChromeOS:", e)

    guardar("chromeos.json", chromeos)
    print(f"📦 Total de dispositivos ChromeOS encontrados: {len(chromeos)}")

    print("✅ Auditoría de dispositivos finalizada.")