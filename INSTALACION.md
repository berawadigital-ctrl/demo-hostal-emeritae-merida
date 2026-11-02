# Instalación

## Requisitos
Cualquier hosting estático (Apache, Nginx, Netlify, Cloudflare Pages, GitHub Pages, S3…). No necesita PHP, base de datos, Node ni claves de API. Probado con `python3 -m http.server` y abriendo `index.html` desde disco (`file://`) en Chromium.

## Pasos
1. Descomprime `demo-hostal-emeritae-merida.zip`.
2. Sube **el contenido** de la carpeta (no la carpeta) al directorio público del hosting: `index.html`, `styles.css`, `app.js`, `robots.txt`, `img/`, `fonts/` y `berawa/`.
3. Abre la URL y comprueba: la página carga con imágenes y tipografía; el selector ES/EN/FR/DE cambia todo el texto; el menú y el botón de reservar funcionan; el asistente responde a la primera pregunta sugerida y dice «No dispongo de esa información» ante algo que no sabe.

## Mientras sea una propuesta
No quites el aviso «Propuesta de rediseño independiente, no oficial» ni el `noindex` (`<meta name="robots">` y `robots.txt`). No publiques bajo el dominio del negocio sin su autorización.

## Seguridad: lo que el hosting debe añadir
El sitio lleva una Content-Security-Policy y una política de referrer por `<meta>`, que cubren casi todo. Las siguientes protecciones **solo funcionan como cabeceras HTTP** y GitHub Pages no permite configurarlas; si el hosting lo permite, añade:
```
X-Content-Type-Options: nosniff
Content-Security-Policy: <la misma del <meta>> ; frame-ancestors 'none'
Referrer-Policy: no-referrer
Permissions-Policy: camera=(), microphone=(), geolocation=()
```
Si cambias el contenido de `index.html`, mantén los scripts y estilos en `app.js` y `styles.css`: la CSP no admite código en línea.

## Limitaciones
- Datos leídos de hostalemeritae.com el 02/11/2026; precios y condiciones pueden haber cambiado (el asistente avisa de que se confirmen al reservar).
- Reservas: motor AvailRoom enlazado desde su web (boton Reservas): https://booking.availroom.com/booking_engine.php?id=AE4B79D6460940DCBBAC84007FA1046A, HTTP 200 con &lang=es/en/fr/de (02/11/2026 07:17). Teléfono +34 924 303 183 · info@hostalemeritae.com. No hay motor de reservas ni disponibilidad en esta demo.
- No se ha probado en Safari ni Firefox ni con lector de pantalla.
- No se toca DNS ni se publica nada por iniciativa propia.
