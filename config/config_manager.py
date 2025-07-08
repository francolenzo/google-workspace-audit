import os
import json
from datetime import datetime

CONFIG_PATH = "config/config.json"

def config_exists():
    return os.path.exists(CONFIG_PATH)

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(data):
    # Asegurarse de que la carpeta exista
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=4)

def setup_config():
    print("🔐 Configuración inicial del entorno de auditoría de Google Workspace")
    print("🛑 Toda la información procesada se guarda de forma local y NO se comparte con terceros.")
    print("👉 Asegurate de haber creado y descargado tu archivo credentials.json desde:")
    print("   https://console.cloud.google.com/apis/credentials")

    input("📎 Colocá el archivo 'credentials.json' en la raíz del proyecto y presioná Enter para continuar...")

    domain = input("🌐 Ingresá el dominio de tu organización (ej. miempresa.com): ").strip()
    admin_email = input("📧 Ingresá el correo del administrador (ej. admin@miempresa.com): ").strip()

    config = {
        "domain": domain,
        "admin_email": admin_email,
        "setup_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_config(config)
    print("✅ Configuración guardada con éxito.")

def get_or_create_config():
    if config_exists():
        return load_config()
    else:
        setup_config()
        return load_config()
