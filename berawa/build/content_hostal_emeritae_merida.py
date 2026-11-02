# Contenido de la demo Hostal Emeritae (Mérida) (es/en/fr/de). Hechos de hostalemeritae.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios, sin valoraciones ni opiniones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hostal real.','en':' Images are illustrations and do not show the actual guesthouse.','fr':' Les images sont des illustrations et ne montrent pas l’hostal réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hostal.'}
H={'es':['Individuales y dobles','Doble con terraza, triples y cuádruples'],'en':['Single and double rooms','Double with terrace, triple and quadruple rooms'],'fr':['Chambres individuelles et doubles','Double avec terrasse, triples et quadruples'],'de':['Einzel- und Doppelzimmer','Doppelzimmer mit Terrasse, Dreibett- und Vierbettzimmer']}
RD={
'es':['Habitaciones confortables de colores claros, insonorizadas, con climatización, TV LED, wifi gratuito y doble acristalamiento.','Opciones para viajar en pareja, con amigos o en familia, con baño con ducha, secador de pelo, toallas y sábanas.'],
'en':['Comfortable rooms in light colours, soundproofed, with air conditioning, LED TV, free wifi and double glazing.','Options for couples, friends or families, with bathroom with shower, hairdryer, towels and sheets.'],
'fr':['Chambres confortables aux couleurs claires, insonorisées, avec climatisation, TV LED, wifi gratuit et double vitrage.','Des options pour voyager en couple, entre amis ou en famille, avec salle de bains avec douche, sèche-cheveux, serviettes et draps.'],
'de':['Komfortable, schallisolierte Zimmer in hellen Farben, mit Klimaanlage, LED-TV, kostenlosem WLAN und Doppelverglasung.','Für Paare, Freunde oder Familien, mit Bad mit Dusche, Haartrockner, Handtüchern und Bettwäsche.']}
ART={
'hero':('columns',7511,['#1a1714','#b7884f','#efdcbc','#6a5038','#44352a','#231c17']),
'intro':('arches',7512,['#f4efe6','#fbf8f1','#94683e','#634631','#2c2018']),
'r1':('arches',7521,['#efe8dc','#cda070','#94683e','#634631','#2c2018']),
'r2':('columns',7522,['#1a1714','#c2925a','#f1dfc1','#735640','#4b3a2d','#271f19']),
'g1':('skyline',7531,['#f2ebe1','#faf5ec','#a07040','#6a5038','#2c2018']),
'g2':('hills',7532,['#ede4d6','#f1e2c8','#cda070','#a08a68','#74624c','#4b3f31']),
'g3':('arches',7533,['#1a1714','#b7884f','#efdcbc','#6a5038','#44352a','#231c17']),
'g4':('waves',7534,['#1a1714','#c2925a','#f1dfc1','#735640','#4b3a2d','#271f19'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Emeritae · Tu hostal en el centro de Mérida',see_rooms='Ver las habitaciones',hero_k='Mérida · C/ Sagasta, 40',hero_t='En el corazón de Mérida, junto al teatro y el museo',hero_s='A 150 m del Museo Nacional de Arte Romano y del Teatro Romano.',
 intro_t='Mejor que un hotel',intro_p1='Habitaciones cómodas y tranquilas, preparadas para tu descanso, con todo lo necesario para una estancia confortable.',
 intro_p2='En nuestra calle están también el Pórtico del Foro Romano, el Templo de Diana y la Alcazaba. El edificio es sostenible: placas solares, iluminación LED y sensores de presencia.',
 stats=['A 150 m del Teatro Romano','Wifi gratis','Edificio adaptado','Parking privado'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Individual, doble, doble con terraza, triple y cuádruple.',
 svcs=['Parking privado','Guardamaletas','Edificio adaptado y ascensor','Patio con chill out','Lavado de bicis para peregrinos','Transporte de maletas'],
 loc_p='C/ Sagasta, 40 · 06800 Mérida (Badajoz). Teléfono: 924 303 183. Check-in desde las 14:00 h; check-out hasta las 12:00 h.',
 chips=['¿Qué habitaciones tenéis?','¿Hay parking?','¿Hay desayuno?','¿Cómo reservo?']),
'en':dict(title='Hostal Emeritae · Your guesthouse in central Mérida',see_rooms='See the rooms',hero_k='Mérida · C/ Sagasta, 40',hero_t='In the heart of Mérida, next to the theatre and the museum',hero_s='150 m from the National Museum of Roman Art and the Roman Theatre.',
 intro_t='Better than a hotel',intro_p1='Comfortable, quiet rooms prepared for your rest, with everything you need for a pleasant stay.',
 intro_p2='Our street is also home to the Portico of the Roman Forum, the Temple of Diana and the Alcazaba. The building is sustainable: solar panels, LED lighting and motion sensors.',
 stats=['150 m from the Roman Theatre','Free wifi','Adapted building','Private parking'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Single, double, double with terrace, triple and quadruple.',
 svcs=['Private parking','Luggage storage','Adapted building and lift','Patio with chill-out area','Bike wash for pilgrims','Luggage transport'],
 loc_p='C/ Sagasta, 40 · 06800 Mérida (Badajoz). Phone: +34 924 303 183. Check-in from 14:00; check-out until 12:00.',
 chips=['Which rooms do you have?','Is there parking?','Is there breakfast?','How do I book?']),
'fr':dict(title='Hostal Emeritae · Votre hostal au centre de Mérida',see_rooms='Voir les chambres',hero_k='Mérida · C/ Sagasta, 40',hero_t='Au cœur de Mérida, près du théâtre et du musée',hero_s='À 150 m du Musée national d’art romain et du Théâtre romain.',
 intro_t='Mieux qu’un hôtel',intro_p1='Des chambres confortables et calmes, préparées pour votre repos, avec tout le nécessaire pour un séjour agréable.',
 intro_p2='Dans notre rue se trouvent aussi le Portique du Forum romain, le Temple de Diane et l’Alcazaba. Le bâtiment est durable : panneaux solaires, éclairage LED et détecteurs de présence.',
 stats=['À 150 m du Théâtre romain','Wifi gratuit','Bâtiment adapté','Parking privé'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Individuelle, double, double avec terrasse, triple et quadruple.',
 svcs=['Parking privé','Bagagerie','Bâtiment adapté et ascenseur','Patio avec espace chill-out','Lavage de vélos pour pèlerins','Transport de bagages'],
 loc_p='C/ Sagasta, 40 · 06800 Mérida (Badajoz). Téléphone : +34 924 303 183. Arrivée à partir de 14:00 ; départ jusqu’à 12:00.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un parking ?','Y a-t-il un petit-déjeuner ?','Comment réserver ?']),
'de':dict(title='Hostal Emeritae · Ihr Hostal im Zentrum von Mérida',see_rooms='Zimmer ansehen',hero_k='Mérida · C/ Sagasta, 40',hero_t='Im Herzen von Mérida, beim Theater und Museum',hero_s='150 m vom Nationalmuseum für Römische Kunst und vom Römischen Theater.',
 intro_t='Besser als ein Hotel',intro_p1='Komfortable, ruhige Zimmer für Ihre Erholung, mit allem, was Sie für einen angenehmen Aufenthalt brauchen.',
 intro_p2='In unserer Straße liegen auch der Portikus des Römischen Forums, der Diana-Tempel und die Alcazaba. Das Gebäude ist nachhaltig: Solarmodule, LED-Beleuchtung und Bewegungsmelder.',
 stats=['150 m vom Römischen Theater','Kostenloses WLAN','Barrierefreies Gebäude','Privatparkplatz'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Einzel-, Doppel-, Doppelzimmer mit Terrasse, Dreibett- und Vierbettzimmer.',
 svcs=['Privatparkplatz','Gepäckaufbewahrung','Barrierefreies Gebäude und Aufzug','Innenhof mit Chill-out-Bereich','Fahrradwäsche für Pilger','Gepäcktransport'],
 loc_p='C/ Sagasta, 40 · 06800 Mérida (Badajoz). Telefon: +34 924 303 183. Check-in ab 14:00 Uhr; Check-out bis 12:00 Uhr.',
 chips=['Welche Zimmer gibt es?','Gibt es Parkplätze?','Gibt es Frühstück?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://booking.availroom.com/booking_engine.php?id=AE4B79D6460940DCBBAC84007FA1046A&lang='
BOOK=dict(mode='engine',url=dict(es=R+'es',en=R+'en',fr=R+'fr',de=R+'de'))
D=dict(name='Hostal Emeritae',ac='#221b16',ac2='#94683e',ac2_a11y='#6e4c2c',book=BOOK,around=[],foot=FOOT,
 address='C/ Sagasta, 40 · 06800 Mérida (Badajoz)',phones=['+34 924 303 183'],emails=['info@hostalemeritae.com'],maps='Hostal Emeritae, Calle Sagasta 40, 06800 Mérida',t=T)
META=dict(repo='demo-hostal-emeritae-merida',name='Hostal Emeritae',legal_name='HOSTAL EMERITAE S.L., NIF B06395552 (aviso legal de su web)',registry_ids=['B06395552'],
 url='https://www.hostalemeritae.com/',domain='hostalemeritae.com',municipality='Mérida',province='Badajoz',sector='hostal en el centro de Merida junto al Teatro Romano',
 read_at='2026-11-02T07:19:00+01:00',created_at='2026-11-02T07:18:00+01:00',built_at='2026-11-02T07:28:00+01:00',audit_date='2026-11-02T07:18:00+01:00',
 rating=dict(value=4.4,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/HOSTAL+EMERITAE+SL/@38.9172959,-6.3417157,17z'),
 book=dict(mode='engine',url=R+'es',note='motor AvailRoom enlazado desde su web (boton Reservas): https://booking.availroom.com/booking_engine.php?id=AE4B79D6460940DCBBAC84007FA1046A, HTTP 200 con &lang=es/en/fr/de (02/11/2026 07:17).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay wifi?','K02'),('¿Hay parking?','K03'),('¿Cuál es el horario de recepción?','K04'),('¿Dónde estáis?','K05'),('¿Cómo reservo?','K06'),('¿Podéis confirmarme disponibilidad para mañana?','K06'),('¿Puedo cancelar gratis?','K07'),('¿Admitís mascotas?','K08'),('¿Es accesible?','K09'),('Hago la Ruta de la Plata, ¿puedo lavar la bici?','K10'),('¿Puedo dejar las maletas?','K11'),('¿Hay lavandería?','K12'),('¿A qué hora es el check-in?','K13'),('¿Hay desayuno?','K14'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Is there wifi?','K02'),('Is there parking?','K03'),('What are the reception hours?','K04'),('Where are you?','K05'),('How do I book?','K06'),('Can you confirm availability for tomorrow?','K06'),('Can I cancel for free?','K07'),('Do you allow pets?','K08'),('Is it accessible?','K09'),('I am a pilgrim on the Vía de la Plata, can I wash my bike?','K10'),('Can I leave my luggage?','K11'),('Is there a laundry?','K12'),('What time is check-in?','K13'),('Is there breakfast?','K14'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il le wifi ?','K02'),('Y a-t-il un parking ?','K03'),('Quels sont les horaires de la réception ?','K04'),('Où êtes-vous ?','K05'),('Comment réserver ?','K06'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K06'),('Puis-je annuler gratuitement ?','K07'),('Acceptez-vous les animaux ?','K08'),('Est-ce accessible ?','K09'),('Je suis pèlerin à vélo, puis-je laver mon vélo ?','K10'),('Puis-je laisser mes bagages ?','K11'),('Y a-t-il une laverie ?','K12'),('À quelle heure est l’arrivée ?','K13'),('Y a-t-il un petit-déjeuner ?','K14'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es WLAN?','K02'),('Gibt es Parkplätze?','K03'),('Wann ist die Rezeption geöffnet?','K04'),('Wo liegt das Hostal?','K05'),('Wie kann ich buchen?','K06'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K06'),('Kann ich kostenlos stornieren?','K07'),('Sind Haustiere erlaubt?','K08'),('Ist es barrierefrei?','K09'),('Ich bin Pilger mit dem Fahrrad, gibt es etwas für Pilger?','K10'),('Kann ich mein Gepäck lassen?','K11'),('Gibt es eine Wäscherei?','K12'),('Ab wann ist der Check-in?','K13'),('Gibt es Frühstück?','K14'),('Was kostet eine Nacht?',None),('Gibt es einen Pool?',None)]}
