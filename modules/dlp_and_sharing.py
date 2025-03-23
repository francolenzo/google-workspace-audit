import os
import json

OUTPUT_DIR = "data/dlp_and_sharing"

def guardar(nombre, data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, nombre), "w") as f:
        json.dump(data, f, indent=4)

def auditar_drive(service):
    print("🔍 Auditando archivos de Google Drive visibles para el administrador...")

    archivos = []
    page_token = None

    while True:
        response = service.files().list(
            pageSize=100,
            fields="nextPageToken, files(id, name, mimeType, owners, permissions, shared, sharingUser)",
            q="trashed = false",
            pageToken=page_token,
        ).execute()
        
        archivos.extend(response.get('files', []))
        page_token = response.get('nextPageToken')
        if not page_token:
            break

    print(f"📁 Archivos encontrados: {len(archivos)}")

    publicos = []
    externos = []
    sospechosos = []

    palabras_clave = ['contraseña', 'clave', 'dni', 'tarjeta', 'confidencial', 'acceso']

    for archivo in archivos:
        permisos = archivo.get('permissions', [])

        for p in permisos:
            tipo = p.get('type')
            dominio = p.get('domain')

            if tipo == 'anyone':
                publicos.append(archivo)
                break
            elif tipo == 'user' and dominio and not dominio.endswith('.com'):  # básico
                externos.append(archivo)
                break

        for palabra in palabras_clave:
            if palabra in archivo['name'].lower():
                sospechosos.append(archivo)
                break

    guardar("archivos_publicos.json", publicos)
    guardar("archivos_externos.json", externos)
    guardar("archivos_sospechosos.json", sospechosos)

    print("✅ Auditoría de compartición y DLP básica completada.")