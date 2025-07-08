import os
from reporting.resumen import generar_portada_y_resumen
from reporting.mod1_auth import generar_modulo1
from reporting.mod2_dispositivos import generar_modulo2
from reporting.mod3_dlp import generar_modulo3
from reporting.mod4_eventos import generar_modulo4
from reporting.mod5_email import generar_modulo5
from reporting.mod6_entorno import generar_modulo6

def generar_html_completo():
    html = f"""
    <html>
    <head>
        <title>Reporte de Auditoría - Google Workspace</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1, h2, h3 {{ color: #2c3e50; }}
            .box {{ background: #f4f4f4; padding: 20px; border-radius: 8px; width: 90%; margin-bottom: 40px; }}
            .item {{ margin-bottom: 8px; }}
            .label {{ font-weight: bold; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ padding: 10px; border: 1px solid #ccc; text-align: left; }}
        </style>
    </head>
    <body>
        <h1>📄 Google Workspace Audit Report</h1>
    """

    # Agregar secciones
    html += generar_portada_y_resumen()
    html += generar_modulo1()
    html += generar_modulo2()
    html += generar_modulo3()
    html += generar_modulo4()
    html += generar_modulo5()
    html += generar_modulo6()

    html += """
    </body>
    </html>
    """

    return html

def main():
    print("🧾 Generando reporte final de auditoría...")
    html = generar_html_completo()

    os.makedirs("output", exist_ok=True)
    output_path = "output/reporte_resumen_general.html"

    with open(output_path, "w") as f:
        f.write(html)

    print(f"✅ Reporte generado en {output_path}")