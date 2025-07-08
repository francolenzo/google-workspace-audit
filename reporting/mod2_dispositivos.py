# reporting/mod2_dispositivos.py
from reporting.common import cargar_json

def generar_modulo2():
    moviles = cargar_json("data/devices/todos_los_dispositivos_moviles.json")
    dispositivos_no_cifrados = cargar_json("data/devices/no_cifrados.json")
    dispositivos_sin_screenlock = cargar_json("data/devices/sin_screenlock.json")
    dispositivos_rooteados = cargar_json("data/devices/rooteados_o_jailbreak.json")
    chromeos = cargar_json("data/devices/chromeos.json")

    html = """
    <!-- 🔧 Módulo 2: Dispositivos -->
    <div class="box">
        <h2>🛠️ Módulo 2: Dispositivos</h2>
        <table>
            <tr><th>📱 Categoría</th><th>Resultado</th></tr>
            <tr><td>📱 Total dispositivos móviles</td><td>{}</td></tr>
            <tr><td>🔓 Sin cifrado</td><td>{}</td></tr>
            <tr><td>🔐 Sin screen lock</td><td>{}</td></tr>
            <tr><td>⚠️ Rooteados / Jailbreak</td><td>{}</td></tr>
        </table>
    </div>
    """.format(
        len(moviles),
        len(dispositivos_no_cifrados),
        len(dispositivos_sin_screenlock),
        len(dispositivos_rooteados),
        len(chromeos)
    )

    return html