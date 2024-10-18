import xml.etree.ElementTree as ET

# Cargar el archivo XML
tree = ET.parse('/home/david.hortelano.7e8/Documents/VS/IncidenciasEntero.xml')
root = tree.getroot()

# Recorrer y mostrar cada incidencia
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
