import os.path
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build



SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user.readonly',
    'https://www.googleapis.com/auth/admin.directory.user.readonly',
    'https://www.googleapis.com/auth/admin.directory.group.readonly',
    'https://www.googleapis.com/auth/admin.directory.orgunit.readonly',
    'https://www.googleapis.com/auth/admin.directory.device.mobile.readonly',
    'https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
    'https://www.googleapis.com/auth/admin.reports.audit.readonly'
]

def get_service(api_name, api_version, creds):
    return build(api_name, api_version, credentials=creds)

def get_authenticated_service():
    creds = None
    print("🔍 Verificando si ya existe token.pickle...")

    if os.path.exists('token.pickle'):
        print("✅ Token existente encontrado. Cargando...")
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔁 Token expirado. Refrescando...")
            creds.refresh(Request())
        else:
            print("🚪 Iniciando flujo de autenticación OAuth...")
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Guardamos el token
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            print("💾 Nuevo token guardado en token.pickle")

    print("🔗 Creando servicio autenticado de Directory API...")
    service = build('admin', 'directory_v1', credentials=creds)
    return service