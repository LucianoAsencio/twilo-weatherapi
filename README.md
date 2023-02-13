# **Alertas del clima**
Este proyecto extrae datos del clima en la ciudad de Mar del Plata utilizando la API de WeatherAPI y los envía a través de un mensaje de texto en Whatsapp utilizando la librería de Twilio.

# **Requisitos previos**

- Crear una cuenta en WeatherAPI y obtener una clave de API.
- Crear una cuenta en Twilio y obtener una clave de API y un número de Twilio.
- Tener un número de teléfono verificado en Twilio y agregarlo como contacto en Whatsapp.


# **Uso**
<ol>
<li>Clone este repositorio a su máquina local.</li>
<li>Instale las dependencias necesarias mediante pip. (twilio, python-dotenv)</li>
<li>Reemplace los valores del archivo '.env' con sus propias claves de API y números de teléfono.</li>
<li>Ejecute el archivo weather_alerts.py</li>
</ol>


# **Personalización**

- Puede modificar la ciudad para la cual se extraen los datos del clima en el script, intercambiando el link que se otorga en la request.
- Puede personalizar el mensaje de texto enviado en el método .create().


<hr>

`Este proyecto es solo para fines educativos y no se recomienda su uso en producción sin una revisión adecuada y pruebas exhaustivas.`
`WeatherAPI y Twilio pueden cobrar tarifas por el uso de sus servicios.`
