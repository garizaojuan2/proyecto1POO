import streamlit as st
import controller
from aircraft import Aircraft
from airplane import Airplane
from airport import Airport
from controlTower import ControlTower
from flight import Flight
from gate import Gate
from helicopter import Helicopter
from jet import PrivateJet
from passenger import Passenger
from person import Person
from worker import Worker

class View:
    def __init__(self):
        st.title("Aeropuerto Alfonso Bonilla Aragón")
        
    def menu(self):
        st.header("Menú de opciones")
        option = st.selectbox('Seleccione la operación que quiere realizar:', ['Crear una objeto', 'Ver los objetos', 'Reservar', 'Funciones de la torre de control', 'Json'])
        return option
    
    def selectObject(self):
        option = st.selectbox('Seleccione la :', ['Avión', 'Helicoptero', 'Jet_privado', 'Vuelo', 'Puerta_de_embarque', 'Pasajero', 'Trabajador'])
        return option
        
    
    def create_worker(self):
        st.header("Creación de Trabajador")
        
        # Entradas de texto para las características del trabajador
        ident = st.text_input("ID:")
        name = st.text_input("Nombre:")
        last_name = st.text_input("Apellido:")
        birthdate = st.date_input("Fecha de nacimiento", value=None)
        gender = st.selectbox(
        'Genero',
        ('Hombre', 'Mujer', 'Otro'))
        address = st.text_input("Dirección:")
        phone_number = st.text_input("Número de teléfono:")
        email = st.text_input("Correo electrónico:")
        position = st.text_input("Posición:")
        years_of_experience = st.text_input("Años de experiencia:")
        max_daily_hours = st.text_input("Máximo de horas diarias:")
        
        st.button("Crear", type="primary")

        if st.button and ident and name and last_name and birthdate and gender and address and phone_number and email and position and max_daily_hours:
            worker = Worker(
                ident,
                name,
                last_name,
                birthdate,
                gender,
                address,
                phone_number,
                email,
                position,
                years_of_experience,
                max_daily_hours
            )
            return worker
        else:
            st.warning("Por favor, complete todos los campos requeridos.")

    

    def create_airplane(self):
        st.header("Creación de Avión")
        
        # Entradas de texto para las características del avión
        brand = st.text_input("Marca:")
        model = st.text_input("Modelo:")
        ident = st.text_input("ID:")
        capacity = st.text_input("Capacidad:")
        max_speed = st.text_input("Velocidad Máxima:")
        autonomy = st.text_input("Autonomía:")
        year = st.text_input("Año:")
        condition = st.text_input("Condición:")
        availability = st.text_input("Disponibilidad:")
        max_altitude = st.text_input("Altitud Máxima:")
        engine_amount = st.text_input("Cantidad de Motores:")
        category = st.text_input("Categoría:")

        st.button("Crear", type="primary")
        
        if st.button and brand and model and ident and capacity and max_speed and autonomy and year and condition  and availability:
            airplane = Airplane(
                brand,
                model,
                ident,
                capacity,
                max_speed,
                autonomy,
                year,
                condition,
                availability,
                max_altitude,
                engine_amount,
                category
                
            )
            return airplane

        else:
            st.warning("Por favor, complete todos los campos requeridos.")
            
    def create_helicopter(self):
        st.header("Creación de Helicóptero")
        
        # Entradas de texto para las características del helicóptero
        brand = st.text_input("Marca:")
        model = st.text_input("Modelo:")
        ident = st.text_input("ID:")
        capacity = st.text_input("Capacidad:")
        max_speed = st.text_input("Velocidad Máxima:")
        autonomy = st.text_input("Autonomía:")
        year = st.text_input("Año:")
        condition = st.text_input("Condición:")
        availability = st.text_input("Disponibilidad:")
        engine_amount = st.text_input("Cantidad de Motores:")
        elevation_capacity = st.text_input("Capacidad de Elevación:")
        use = st.text_input("Uso:")
        
        st.button("Crear", type="primary")

        if st.button and brand and model and ident and capacity and max_speed and autonomy and year and condition and availability:
            helicopter = Helicopter(
                brand,
                model,
                ident,
                capacity,
                max_speed,
                autonomy,
                year,
                condition,
                availability,
                engine_amount,
                elevation_capacity,
                use
                
            )
            return helicopter

        else:
            st.warning("Por favor, complete todos los campos requeridos.")
            
            
    def create_jet(self):
        st.header("Creación de Aeronave Personalizada")
        
        # Entradas de texto para las características de la aeronave personalizada
        brand = st.text_input("Marca:")
        model = st.text_input("Modelo:")
        ident = st.text_input("ID:")
        capacity = st.text_input("Capacidad:")
        max_speed = st.text_input("Velocidad Máxima:")
        autonomy = st.text_input("Autonomía:")
        year = st.text_input("Año:")
        condition = st.text_input("Condición:")
        availability = st.text_input("Disponibilidad:")
        owner = st.text_input("Propietario:")
        services = st.text_input("Servicios (separe los servicios por espacios)")
        destinations = st.text_input("Destinos (separe los detinos por espacios)")
        lServices = []
        lDestinations = []
        lServices = services.split()
        lDestinations = destinations.split()
        st.button("Crear", type="primary")

        if st.button and brand and model and ident and capacity and max_speed and autonomy and year and condition and availability and owner:
            jet = PrivateJet(
                brand,
                model,
                ident,
                capacity,
                max_speed,
                autonomy,
                year,
                condition,
                availability,
                owner,
                lServices,
                lDestinations
                
            )
            return jet
        else:
            st.warning("Por favor, complete todos los campos requeridos.")
            
            
    def create_passenger(self):
        st.header("Creación de Pasajero")
        
        paises = ["Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda", "Arabia Saudita", "Argelia", "Argentina", "Armenia",
        "Australia", "Austria", "Azerbaiyán", "Bahamas", "Bangladés", "Barbados", "Baréin", "Bélgica", "Belice", "Benín",
        "Bielorrusia", "Birmania", "Bolivia", "Bosnia y Herzegovina", "Botsuana", "Brasil", "Brunéi", "Bulgaria", "Burkina Faso", "Burundi",
        "Bután", "Cabo Verde", "Camboya", "Camerún", "Canadá", "Catar", "Chad", "Chile", "China", "Chipre",
        "Colombia", "Comoras", "Corea del Norte", "Corea del Sur", "Costa de Marfil", "Costa Rica", "Croacia", "Cuba", "Dinamarca", "Dominica",
        "Ecuador", "Egipto", "El Salvador", "Emiratos Árabes Unidos", "Eritrea", "Eslovaquia", "Eslovenia", "España", "Estados Unidos", "Estonia",
        "Etiopía", "Filipinas", "Finlandia", "Fiyi", "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada",
        "Grecia", "Guatemala", "Guinea", "Guinea Ecuatorial", "Guinea-Bisáu", "Guyana", "Haití", "Honduras", "Hungría", "India",
        "Indonesia", "Irak", "Irán", "Irlanda", "Islandia", "Islas Marshall", "Islas Salomón", "Israel", "Italia", "Jamaica",
        "Japón", "Jordania", "Kazajistán", "Kenia", "Kirguistán", "Kiribati", "Kuwait", "Laos", "Lesoto", "Letonia",
        "Líbano", "Liberia", "Libia", "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte", "Madagascar", "Malasia", "Malaui",
        "Maldivas", "Malí", "Malta", "Marruecos", "Mauricio", "Mauritania", "México", "Micronesia", "Moldavia", "Mónaco",
        "Mongolia", "Montenegro", "Mozambique", "Namibia", "Nauru", "Nepal", "Nicaragua", "Níger", "Nigeria", "Noruega",
        "Nueva Zelanda", "Omán", "Países Bajos", "Pakistán", "Palaos", "Palestina", "Panamá", "Papúa Nueva Guinea", "Paraguay", "Perú",
        "Polonia", "Portugal", "Reino Unido", "República Centroafricana", "República Checa", "República del Congo", "República Democrática del Congo", "República Dominicana", "Ruanda",
        "Rumanía", "Rusia", "Samoa", "San Cristóbal y Nieves", "San Marino", "San Vicente y las Granadinas", "Santa Lucía", "Santo Tomé y Príncipe", "Senegal",
        "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Siria", "Somalia", "Sri Lanka", "Suazilandia", "Sudáfrica", "Sudán",
        "Sudán del Sur", "Suecia", "Suiza", "Surinam", "Tailandia", "Taiwán", "Tanzania", "Tayikistán", "Timor Oriental", "Togo",
        "Tonga", "Trinidad y Tobago", "Túnez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda", "Uruguay", "Uzbekistán",
        "Vanuatu", "Vaticano", "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia", "Zimbabue"]
        
        # Entradas de texto para las características del pasajero
        ident = st.text_input("ID:")
        name = st.text_input("Nombre:")
        last_name = st.text_input("Apellido:")
        birthdate = st.date_input("Fecha de nacimiento", value=None)
        gender = st.selectbox(
        'Genero',
        ('Hombre', 'Mujer', 'Otro'))
        address = st.text_input("Dirección:")
        phone_number = st.text_input("Número de teléfono:")
        email = st.text_input("Correo electrónico:")
        nationality = option = st.selectbox("Selecciona tu nacionalidad", paises)
        baggage_amount = st.text_input("Cantidad de equipaje:")
        medical_information = st.text_input("Información médica:")
        
        st.button("Crear", type="primary")

        if st.button and ident and name and last_name and birthdate and gender and address and phone_number and email and nationality and baggage_amount:
            passenger = Passenger(
                ident,
                name,
                last_name,
                birthdate,
                gender,
                address,
                phone_number,
                email,
                nationality,
                baggage_amount,
                medical_information
                
            )
            return passenger

        else:
            st.warning("Por favor, complete todos los campos requeridos.")
            
            
    def create_gate(self):
        st.header("Creación de Puerta de Embarque")
        
        # Entradas de texto para las características de la puerta de embarque
        ident = st.text_input("ID:")
        location = st.text_input("Ubicación:")
        availability = st.text_input("Disponibilidad:")
        boarding_hour = st.text_input("Hora de abordaje:")
        
        st.button("Crear", type="primary")

        if st.button and ident and location and availability and boarding_hour:
            gate = Gate(
                ident,
                location,
                availability,
                boarding_hour
            )
            return gate
        else:
            st.warning("Por favor, complete todos los campos requeridos.")
        
        
    def create_flight(self):
        st.header("Creación de vuelo")
        
        # Entradas de texto para las características de la puerta de embarque
        ident = st.text_input("ID:")
        date = st.date_input("Fecha:")
        origin = st.text_input("Origen:")
        destination = st.text_input("Destino:")
        available_seats = st.text_input("Sillas disponibles:")
        
        st.button("Crear", type="primary")

        if st.button and ident and date and origin and destination and available_seats:
            flight = Flight(
                ident,
                date,
                origin,
                destination,
                available_seats
            )
            return flight

        else:
            st.warning("Por favor, complete todos los campos requeridos.")
            
            
    """
    def ver_objetos():
        st.subheader("Ver objetos creados")
        selected_option = st.selectbox("Seleccione una opción:", ["Trabajador", "Avión", "Helicóptero", "Jet privado", "Pasajeros", "Puerta de embarque"])

        if selected_option == "Trabajador":
            st.header("Trabajador")
            controller.view_worker()

        elif selected_option == "Avión":
            st.header("Avión")
            controller.view_airplane()

        elif selected_option == "Helicóptero":
            st.header("Helicóptero")
            controller.view_helicopter()

        elif selected_option == "Jet privado":
            st.header("Jet privado")
            controller.view_jet()

        elif selected_option == "Pasajeros":
            st.header("Pasajeros")
            controller.view_passenger()

        elif selected_option == "Puerta de embarque":
            st.header("Puerta de embarque")
            controller.view_gate()
"""
        

