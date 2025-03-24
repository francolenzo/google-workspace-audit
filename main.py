from config.config_manager import get_or_create_config
from config.auth import get_authenticated_service, get_service
from modules.auth_and_access import auditar_auth_and_access
from modules.devices import auditar_dispositivos
from modules.dlp_and_sharing import auditar_drive
from modules.audit_logs import auditar_eventos
from modules.email_security import auditar_seguridad_email
from modules.environment_security import auditar_configuracion_entorno



def main():
    print("🚀 Iniciando script...")
    print("⚙️ Entrando al main()...")

    # Paso 1: Obtener configuración guardada o pedirla
    config = get_or_create_config()
    print(f"🔧 Dominio configurado: {config['domain']}")
    print(f"👤 Admin: {config['admin_email']}")

    # Paso 2: Autenticación con Google OAuth
    print("🔐 Autenticando con Google Workspace...")
    service = get_authenticated_service()

    # Paso 3: Probar llamada a Directory API
    print("👥 Obteniendo los primeros 10 usuarios del dominio...")
    results = service.users().list(customer='my_customer', maxResults=10, orderBy='email').execute()
    users = results.get('users', [])

    if not users:
        print('❌ No se encontraron usuarios.')
    else:
        print('✅ Usuarios encontrados:')
        for user in users:
            print(f" - {user['primaryEmail']} ({user['name']['fullName']})")

    # Ejecutar módulo 1
    auditar_auth_and_access(service)
    
    # Ejecutar módulo 2
    auditar_dispositivos(service)

    # Ejecutar módulo 3 (Google Drive)
    drive_service = get_service("drive", "v3", service._http.credentials)
    auditar_drive(drive_service)

    # Ejecutar módulo 4 (Reports API)
    reports_service = get_service("admin", "reports_v1", service._http.credentials)
    auditar_eventos(reports_service)

    emails = [user['primaryEmail'] for user in users]
    gmail_service = get_service("gmail", "v1", service._http.credentials)

    # Ejecutar módulo 5
    auditar_seguridad_email(gmail_service, users)

    # Ejecutar módulo 6
    auditar_configuracion_entorno(service, reports_service)


if __name__ == "__main__":
    main()