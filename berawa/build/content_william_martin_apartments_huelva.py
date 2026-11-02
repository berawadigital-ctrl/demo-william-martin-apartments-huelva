# Contenido de la demo William Martin Apartments (Huelva) (es/en/fr/de). Hechos de williammartin.es leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Apartments.'}
H={'es':['Apartamentos de 1 habitación y loft','Apartamento de 2 habitaciones'],'en':['1-bedroom apartments and loft','2-bedroom apartment'],'fr':['Appartements 1 chambre et loft','Appartement 2 chambres'],'de':['1-Zimmer-Apartments und Loft','2-Zimmer-Apartment']}
RD={
'es':['De 30 a 47 m², para 2 a 4 personas: cama de matrimonio, salón con sofá cama, cocina y baño independiente. Hay versión premium y premium con gran terraza, y un loft con habitación integrada.','49 m², dos habitaciones con cama de matrimonio y dos baños, salón con sofá convertible y grandes ventanales a la calle Vázquez López esquina calle Palacio.'],
'en':['From 30 to 47 m², for 2 to 4 people: double bed, living room with sofa bed, kitchen and separate bathroom. There is a premium version, a premium one with a large terrace and a loft with integrated bedroom.','49 m², two bedrooms with a double bed and two bathrooms, living room with sofa bed and large windows onto Vázquez López street at the corner of Palacio street.'],
'fr':['De 30 à 47 m², pour 2 à 4 personnes : lit double, salon avec canapé-lit, cuisine et salle de bain indépendante. Il existe une version premium, une premium avec grande terrasse et un loft avec chambre intégrée.','49 m², deux chambres avec lit double et deux salles de bain, salon avec canapé convertible et grandes baies sur la rue Vázquez López, à l’angle de la rue Palacio.'],
'de':['30 bis 47 m² für 2 bis 4 Personen: Doppelbett, Wohnzimmer mit Schlafsofa, Küche und eigenes Bad. Es gibt eine Premium-Variante, eine Premium-Variante mit großer Terrasse und ein Loft mit integriertem Schlafbereich.','49 m², zwei Schlafzimmer mit Doppelbett und zwei Bäder, Wohnzimmer mit Schlafsofa und große Fenster zur Calle Vázquez López, Ecke Calle Palacio.']}
ART={
'hero':('waves',9601,['#1d2b3a','#d39a5b','#efc994','#3e5a6e','#2e4757','#172530']),
'intro':('columns',9602,['#eeece6','#f8f6f0','#3e5a6e','#2e4757','#172530']),
'r1':('arches',9611,['#ece5d9','#cf955a','#3e5a6e','#1d2b3a','#0f1720']),
'r2':('skyline',9612,['#e8ebee','#dba36a','#f1d0a0','#584235','#45342a','#291f19']),
'g1':('waves',9621,['#223344','#e0a86c','#f3d6aa','#3c566a','#2e4556','#18242e']),
'g2':('columns',9622,['#ecebe5','#f7f6f1','#6b4a33','#523826','#2f2016']),
'g3':('hills',9623,['#e9ece2','#efe2c6','#d89e62','#9fae94','#728468','#4c5b45']),
'g4':('skyline',9624,['#1d2b3a','#d89d5e','#f0cd98','#4a3c52','#3a2f41','#221b27'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='William Martin Apartments · Apartamentos turísticos en el centro de Huelva',see_rooms='Ver los apartamentos',hero_k='Huelva · Vázquez López 2',hero_t='Donde historia y modernidad se entrelazan',hero_s='Apartamentos exclusivos en el corazón de Huelva, en un edificio tematizado con la historia del «hombre que nunca existió».',
 intro_t='Apartamentos con historia',intro_p1='El nombre recuerda a William Martin, el oficial ficticio de la Operación Mincemeat que apareció en la costa de Huelva en 1943. Las paredes guardan sutiles referencias a aquel episodio.',
 intro_p2='Apartamentos de 1 y 2 habitaciones, todos exteriores, en 4 plantas con ascensor, con vistas al centro histórico, cocina equipada, aire acondicionado y wifi gratis.',
 stats=['Todos exteriores','4 plantas con ascensor','Smartphone Key','Wifi gratis'],nav_rooms='Apartamentos',rooms_t='Nuestros apartamentos',rooms_s='De 1 y 2 habitaciones, de 30 a 49 m².',
 svcs=['Acceso con el móvil (App Hoomvip)','Wifi gratis','Aire acondicionado y calefacción','Cocina equipada','Cunas sin coste bajo petición','Atención médica 24 h (Quirónsalud)'],
 around_s='En pleno corazón de Huelva, con vistas al centro histórico y sus puntos de interés a pie.',
 loc_p='Calle Vázquez López 2 · Huelva. Check-in y check-out: hasta las 12:00.',
 chips=['¿Qué apartamentos tenéis?','¿Cómo se entra al apartamento?','¿Admitís mascotas?','¿Cómo reservo?']),
'en':dict(title='William Martin Apartments · Tourist apartments in central Huelva',see_rooms='See the apartments',hero_k='Huelva · Vázquez López 2',hero_t='Where history and modernity intertwine',hero_s='Exclusive apartments in the heart of Huelva, in a building themed on the story of “the man who never was”.',
 intro_t='Apartments with a story',intro_p1='The name recalls William Martin, the fictitious officer of Operation Mincemeat who appeared on the coast of Huelva in 1943. The walls hold subtle references to that episode.',
 intro_p2='1- and 2-bedroom apartments, all exterior, on 4 floors with a lift, with views of the old town, equipped kitchen, air conditioning and free wifi.',
 stats=['All exterior','4 floors with lift','Smartphone Key','Free wifi'],nav_rooms='Apartments',rooms_t='Our apartments',rooms_s='1 and 2 bedrooms, from 30 to 49 m².',
 svcs=['Phone access (Hoomvip app)','Free wifi','Air conditioning and heating','Equipped kitchen','Free cots on request','24 h medical care (Quirónsalud)'],
 around_s='Right in the heart of Huelva, with views of the old town and its sights within walking distance.',
 loc_p='Calle Vázquez López 2 · Huelva. Check-in and check-out: until 12:00.',
 chips=['Which apartments do you have?','How do I get into the apartment?','Do you accept pets?','How do I book?']),
'fr':dict(title='William Martin Apartments · Appartements touristiques au centre de Huelva',see_rooms='Voir les appartements',hero_k='Huelva · Vázquez López 2',hero_t='Là où l’histoire et la modernité se rejoignent',hero_s='Des appartements exclusifs au cœur de Huelva, dans un immeuble consacré à l’histoire de « l’homme qui n’a jamais existé ».',
 intro_t='Des appartements chargés d’histoire',intro_p1='Le nom rappelle William Martin, l’officier fictif de l’opération Mincemeat retrouvé sur la côte de Huelva en 1943. Les murs gardent de discrètes références à cet épisode.',
 intro_p2='Appartements de 1 et 2 chambres, tous extérieurs, sur 4 étages avec ascenseur, vue sur le centre historique, cuisine équipée, climatisation et wifi gratuit.',
 stats=['Tous extérieurs','4 étages avec ascenseur','Smartphone Key','Wifi gratuit'],nav_rooms='Appartements',rooms_t='Nos appartements',rooms_s='1 et 2 chambres, de 30 à 49 m².',
 svcs=['Accès par mobile (app Hoomvip)','Wifi gratuit','Climatisation et chauffage','Cuisine équipée','Lits bébé gratuits sur demande','Assistance médicale 24 h (Quirónsalud)'],
 around_s='En plein cœur de Huelva, avec vue sur le centre historique et ses sites à pied.',
 loc_p='Calle Vázquez López 2 · Huelva. Arrivée et départ : jusqu’à 12:00.',
 chips=['Quels appartements avez-vous ?',"Comment entre-t-on dans l'appartement ?",'Acceptez-vous les animaux ?','Comment réserver ?']),
'de':dict(title='William Martin Apartments · Ferienapartments im Zentrum von Huelva',see_rooms='Apartments ansehen',hero_k='Huelva · Vázquez López 2',hero_t='Wo Geschichte und Moderne sich verbinden',hero_s='Exklusive Apartments im Herzen von Huelva, in einem Gebäude rund um die Geschichte des „Mannes, den es nie gab“.',
 intro_t='Apartments mit Geschichte',intro_p1='Der Name erinnert an William Martin, den fiktiven Offizier der Operation Mincemeat, der 1943 an der Küste von Huelva auftauchte. Die Wände enthalten dezente Hinweise auf diese Episode.',
 intro_p2='Apartments mit 1 und 2 Schlafzimmern, alle nach außen gelegen, auf 4 Etagen mit Aufzug, mit Blick auf die Altstadt, ausgestatteter Küche, Klimaanlage und kostenlosem WLAN.',
 stats=['Alle nach außen','4 Etagen mit Aufzug','Smartphone Key','Kostenloses WLAN'],nav_rooms='Apartments',rooms_t='Unsere Apartments',rooms_s='1 und 2 Schlafzimmer, 30 bis 49 m².',
 svcs=['Zugang per Handy (App Hoomvip)','Kostenloses WLAN','Klimaanlage und Heizung','Ausgestattete Küche','Kostenlose Kinderbetten auf Anfrage','Ärztliche Betreuung 24 h (Quirónsalud)'],
 around_s='Mitten im Herzen von Huelva, mit Blick auf die Altstadt und ihre Sehenswürdigkeiten zu Fuß.',
 loc_p='Calle Vázquez López 2 · Huelva. Check-in und Check-out: bis 12:00 Uhr.',
 chips=['Welche Apartments gibt es?','Wie komme ich ins Apartment?','Sind Haustiere erlaubt?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://booking.avirato.com/?code=46856891'
BOOK=dict(mode='engine',url={l:RB+'&lang='+l for l in ('es','en','fr','de')})
D=dict(name='William Martin Apartments',ac='#1d2b3a',ac2='#3e5a6e',ac2_a11y='#2e4757',book=BOOK,around=['Centro histórico de Huelva','Calle Palacio'],foot=FOOT,
 address='Calle Vázquez López 2 · Huelva',phones=['+34 614 233 630'],emails=['apartamentos@williammartin.es'],maps='William Martin Apartments, Calle Vázquez López 2, Huelva',t=T)
META=dict(repo='demo-william-martin-apartments-huelva',name='William Martin Apartments',legal_name='CASATO ONUBA, S.L. (CIF del pie de su web)',registry_ids=['B10593036','A/HU/00196'],
 url='https://williammartin.es/',domain='williammartin.es',municipality='Huelva',province='Huelva',sector='edificio de apartamentos turísticos en el centro de Huelva',
 read_at='2026-10-30T09:15:00+01:00',created_at='2026-10-30T09:14:00+01:00',built_at='2026-10-30T09:30:00+01:00',audit_date='2026-10-30T09:08:42+01:00',
 rating=dict(value=4.7,coincide=['telefono','web'],date='2026-10-29T16:36:07+01:00',url='https://www.google.com/maps/place/William+Martin+Apartments/@37.2564849,-6.9514036,17z/data=!3m1!4b1!4m6!3m5!1s0xd11d183858bac5d:0xbc4e3296c2073c36!8m2!3d37.2564849!4d-6.9514036!16s%2Fg%2F11lyw5p8n0'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (booking.williammartin.es redirige a Avirato, code 46856891), HTTP 200 comprobado el 30/10/2026 con lang es/en/fr/de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Cómo se entra al apartamento?','K02'),('¿Cuál es el horario de check-in y check-out?','K03'),('¿Hay wifi?','K04'),('¿Tienen cocina?','K05'),('¿Admitís mascotas?','K06'),('¿Tenéis cuna para el bebé?','K07'),('¿Dónde están los apartamentos?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Cuál es la política de cancelación?','K10'),('¿Hay ascensor?','K11'),('¿Hay atención médica?','K12'),('¿Por qué se llama William Martin?','K13'),('¿Tenéis piscina?',None),('¿Hay gimnasio?',None)],
'en':[('Which apartments do you have?','K01'),('How do I get into the apartment?','K02'),('What are the check-in and check-out times?','K03'),('Is there wifi?','K04'),('Is there a kitchen?','K05'),('Do you accept pets?','K06'),('Do you have a cot for the baby?','K07'),('Where are the apartments?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('What is the cancellation policy?','K10'),('Is there a lift?','K11'),('Is there medical assistance?','K12'),('Why is it called William Martin?','K13'),('Do you have a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),("Comment entre-t-on dans l'appartement ?",'K02'),('Quels sont les horaires d’arrivée et de départ ?','K03'),('Y a-t-il le wifi ?','K04'),('Y a-t-il une cuisine ?','K05'),('Acceptez-vous les animaux ?','K06'),('Avez-vous un lit bébé ?','K07'),('Où se trouvent les appartements ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),("Quelle est la politique d'annulation ?",'K10'),('Y a-t-il un ascenseur ?','K11'),('Y a-t-il une assistance médicale ?','K12'),('Pourquoi s’appelle-t-il William Martin ?','K13'),('Avez-vous une piscine ?',None),('Y a-t-il une salle de sport ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Wie komme ich ins Apartment?','K02'),('Wann sind Check-in und Check-out?','K03'),('Gibt es WLAN?','K04'),('Gibt es eine Küche?','K05'),('Sind Haustiere erlaubt?','K06'),('Haben Sie ein Kinderbett?','K07'),('Wo befinden sich die Apartments?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Wie sind die Stornobedingungen?','K10'),('Gibt es einen Aufzug?','K11'),('Gibt es ärztliche Betreuung?','K12'),('Warum heißt es William Martin?','K13'),('Haben Sie ein Schwimmbad?',None),('Gibt es ein Fitnessstudio?',None)]}
