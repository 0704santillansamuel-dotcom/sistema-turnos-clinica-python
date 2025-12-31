import random
import time
from datetime import datetime, timedelta

# ============================
# UTILIDADES VISUALES
# ============================

def separador():
    print("\n" + "═" * 80 + "\n")

def escribir(texto, velocidad=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()

def opcion_valida(mensaje, opciones):
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion in opciones:
            return opcion
        print("❌ Opción inválida. Intentá de nuevo.")

# ============================
# BIENVENIDA
# ============================

separador()
escribir("🏥 SISTEMA INTELIGENTE DE TURNOS MÉDICOS")
escribir("💎 Swiss Medical | OSDE Black | Clínica Premium Nordelta")
separador()

nombre = input("👤 Nombre completo: ").strip().title()

while True:
    try:
        edad = int(input("🎂 Edad: "))
        break
    except ValueError:
        print("❌ Por favor ingresá una edad válida.")

paciente_id = f"PAC-{random.randint(1000,9999)}"

# ============================
# OBRA SOCIAL
# ============================

separador()
print("💳 Cobertura médica:")
print("1️⃣ Swiss Medical")
print("2️⃣ OSDE")
print("3️⃣ Particular")

obra = opcion_valida("👉 Elegí una opción: ", ["1", "2", "3"])
obras = {"1": "Swiss Medical", "2": "OSDE", "3": "Particular"}
obra_social = obras[obra]

prioridad = {
    "Swiss Medical": "ALTA",
    "OSDE": "MEDIA",
    "Particular": "BAJA"
}[obra_social]

# ============================
# ESPECIALIDADES SEGÚN EDAD
# ============================

separador()
if edad < 18:
    especialidades = {
        "1": "Pediatría",
        "2": "Psicología Infantil",
        "3": "Odontopediatría"
    }
else:
    especialidades = {
        "1": "Clínica Médica",
        "2": "Cardiología",
        "3": "Traumatología",
        "4": "Dermatología",
        "5": "Psicología"
    }

print("🩺 Especialidades disponibles:")
for k, v in especialidades.items():
    print(f"{k}️⃣ {v}")

esp = opcion_valida("👉 Elegí la especialidad: ", especialidades.keys())
especialidad = especialidades[esp]

# ============================
# MÉDICOS
# ============================

medicos = {
    "Pediatría": ["Dra. Valentina Ríos"],
    "Psicología Infantil": ["Lic. Camila Torres"],
    "Odontopediatría": ["Dra. Sofía Lamas"],
    "Clínica Médica": ["Dr. Alejandro Funes"],
    "Cardiología": ["Dr. Ignacio Moretti"],
    "Traumatología": ["Dr. Pablo Rinaldi"],
    "Dermatología": ["Dra. Julieta Costa"],
    "Psicología": ["Lic. Federico Álvarez"]
}

medico = random.choice(medicos[especialidad])

# ============================
# TURNO
# ============================

sucursales = ["Nordelta", "Recoleta", "Puerto Madero"]
horarios = ["09:00", "10:30", "12:00", "15:30", "17:00"]

sucursal = random.choice(sucursales)
hora_turno = random.choice(horarios)
fecha_turno = datetime.now() + timedelta(days=random.randint(1, 7))
turno_id = f"TUR-{random.randint(10000,99999)}"
turno_activo = True

# ============================
# RESUMEN DEL TURNO
# ============================

separador()
print("📋 RESUMEN DEL TURNO")
print(f"🪪 ID Paciente: {paciente_id}")
print(f"🧾 Número de turno: {turno_id}")
print(f"👤 Paciente: {nombre}")
print(f"🎂 Edad: {edad}")
print(f"💳 Obra social: {obra_social}")
print(f"⭐ Prioridad: {prioridad}")
print(f"🏥 Sucursal: {sucursal}")
print(f"🩺 Especialidad: {especialidad}")
print(f"👨‍⚕️ Médico: {medico}")
print(f"📅 Fecha: {fecha_turno.strftime('%d/%m/%Y')}")
print(f"⏰ Hora: {hora_turno}")
separador()

confirmar = opcion_valida("✅ ¿Confirmar turno? (si/no): ", ["si", "no"])
if confirmar == "no":
    escribir("❌ Turno cancelado. Gracias por usar el sistema.")
    exit()

# ============================
# BENEFICIOS PREMIUM
# ============================

separador()
escribir("🌟 BENEFICIOS PREMIUM ACTIVADOS")
print("☕ Café Nespresso sin cargo")
print("🚗 Valet Parking incluido")
print("🛋️ Sala VIP exclusiva")
print("📱 Check-in digital automático")

# ============================
# MENÚ DEL PACIENTE
# ============================

while True:
    separador()
    print("📌 MENÚ DEL PACIENTE")
    print("1️⃣ Ver turno")
    print("2️⃣ Check-in")
    print("3️⃣ Reprogramar turno")
    print("4️⃣ Cancelar turno")
    print("5️⃣ Emergencia")
    print("6️⃣ Encuesta de satisfacción")
    print("7️⃣ Salir")

    opcion = opcion_valida("👉 Elegí una opción: ", ["1","2","3","4","5","6","7"])

    if opcion == "1":
        if turno_activo:
            print(f"📅 {fecha_turno.strftime('%d/%m/%Y')} ⏰ {hora_turno} | {especialidad}")
        else:
            print("❌ No tenés turno activo.")

    elif opcion == "2":
        escribir("📲 Check-in realizado con éxito.")
        escribir("⏳ Aguarde en la sala VIP.")

    elif opcion == "3":
        hora_turno = random.choice(horarios)
        escribir(f"🔁 Turno reprogramado para las {hora_turno}.")

    elif opcion == "4":
        cancelar = opcion_valida("❗ ¿Desea cancelar el turno? (si/no): ", ["si","no"])
        if cancelar == "si":
            turno_activo = False
            escribir("❌ Turno cancelado exitosamente.")
            break

    elif opcion == "5":
        escribir("🚨 EMERGENCIA ACTIVADA")
        escribir("🏃‍♂️ Personal médico en camino.")

    elif opcion == "6":
        calificacion = opcion_valida("⭐ Calificá el servicio (1-5): ", ["1","2","3","4","5"])
        escribir("🙏 Gracias por tu opinión. Nos ayuda a mejorar.")

    elif opcion == "7":
        escribir("👋 Gracias por elegir nuestra clínica premium.")
        break

separador()
escribir("💎 SISTEMA FINALIZADO")
