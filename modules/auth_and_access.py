import os
import json
from datetime import datetime, timedelta

OUTPUT_DIR = "data/auth_and_access"

def guardar_resultado(nombre_archivo, datos):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, nombre_archivo), "w") as f:
        json.dump(datos, f, indent=4)

def auditar_auth_and_access(service):
    print("🔍 Ejecutando auditoría de autenticación y accesos...")

    # 1. Obtener todos los usuarios
    usuarios = []
    page_token = None
    while True:
        results = service.users().list(customer='my_customer', maxResults=500,
                                       orderBy='email', pageToken=page_token).execute()
        usuarios.extend(results.get('users', []))
        page_token = results.get('nextPageToken')
        if not page_token:
            break

    print(f"👥 Usuarios totales encontrados: {len(usuarios)}")

    # 2. Contar usuarios sin MFA
    sin_mfa = [u for u in usuarios if not u.get('isEnrolledIn2Sv', False)]

    # 3. Usuarios inactivos hace más de 30 días
    hace_30_dias = datetime.utcnow() - timedelta(days=30)
    inactivos = []
    for u in usuarios:
        last_login = u.get('lastLoginTime')
        if last_login == '1970-01-01T00:00:00.000Z' or last_login is None:
            inactivos.append(u)
        else:
            dt_login = datetime.strptime(last_login, '%Y-%m-%dT%H:%M:%S.%fZ')
            if dt_login < hace_30_dias:
                inactivos.append(u)

    # 4. Usuarios privilegiados
    privilegiados = [u for u in usuarios if u.get('isAdmin') or u.get('isDelegatedAdmin')]

    # 5. Obtener cantidad de unidades organizativas
    ou_response = service.orgunits().list(customerId='my_customer', type='all').execute()
    total_ous = len(ou_response.get('organizationUnits', []))

    # 6. Obtener cantidad de grupos
    grupos_response = service.groups().list(customer='my_customer').execute()
    total_grupos = len(grupos_response.get('groups', []))

    # 7. Obtener usuarios con delegaciones (placeholder: requiere Gmail API más adelante)
    delegaciones = []  # Podemos implementarlo después

    # 8. Guardar resultados
    guardar_resultado("resumen_general.json", {
        "usuarios_totales": len(usuarios),
        "usuarios_sin_mfa": len(sin_mfa),
        "usuarios_inactivos": len(inactivos),
        "usuarios_privilegiados": len(privilegiados),
        "unidades_organizativas": total_ous,
        "grupos": total_grupos,
        "fecha_auditoria": datetime.utcnow().isoformat()
    })

    guardar_resultado("usuarios_sin_mfa.json", sin_mfa)
    guardar_resultado("usuarios_inactivos.json", inactivos)
    guardar_resultado("usuarios_privilegiados.json", privilegiados)
    guardar_resultado("usuarios_con_delegaciones.json", delegaciones)

    print("✅ Auditoría de autenticación y accesos finalizada.")