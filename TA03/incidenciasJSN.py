import xml.etree.ElementTree as ET
import json

tree = ET.parse('/home/david.hortelano.7e8/PycharmProjects/DavidHortelano-ITB2425-MDS/IncidenciasEntero.xml')
root = tree.getroot()

incidencias_lista = []

for incidencia in root.findall('Incidencia'):
    usuario = incidencia.find('Usuario')
    id_usuario = usuario.find('ID').text
    nombre_usuario = usuario.find('Nombre').text
    correo_usuario = usuario.find('Correo').text
    dispositivo = incidencia.find('Dispositivo').text

    problema = incidencia.find('Problema')
    fecha_problema = problema.find('Fecha').text
    tipo_problema = problema.find('Tipo').text
    descripcion_problema = problema.find('Descripcion').text
    prioridad_problema = problema.find('Prioridad').text
    comentario_adicional = problema.find('ComentarioAdicional').text

    print(f"ID Usuario: {id_usuario}")
    print(f"Nombre Usuario: {nombre_usuario}")
    print(f"Correo Usuario: {correo_usuario}")
    print(f"Dispositivo: {dispositivo}")
    print(f"Fecha del problema: {fecha_problema}")
    print(f"Tipo de problema: {tipo_problema}")
    print(f"Descripción del problema: {descripcion_problema}")
    print(f"Prioridad: {prioridad_problema}")
    print(f"Comentario adicional: {comentario_adicional if comentario_adicional else 'Ninguno'}")
    print("-" * 40)

    incidencia_dict = {
        "ID Usuario": id_usuario,
        "Nombre Usuario": nombre_usuario,
        "Correo Usuario": correo_usuario,
        "Dispositivo": dispositivo,
        "Fecha del problema": fecha_problema,
        "Tipo de problema": tipo_problema,
        "Descripción del problema": descripcion_problema,
        "Prioridad": prioridad_problema,
        "Comentario adicional": comentario_adicional if comentario_adicional else 'Ninguno'
    }

    incidencias_lista.append(incidencia_dict)

with open('incidencies.json', 'w', encoding='utf-8') as json_file:
    json.dump(incidencias_lista, json_file, ensure_ascii=False, indent=4)

print("Incidencias guardadas en incidencies.json")
