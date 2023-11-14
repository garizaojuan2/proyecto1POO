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
import pandas as pd
from airline import Airline

class View:
    def __init__(self):
        st.title("Aeropuerto Alfonso Bonilla Aragón")
        
    def menu(self):
        st.header("Menú de opciones")
        option = st.selectbox('Seleccione la operación que quiere realizar:', ['Crear una objeto', 'Ver los objetos', 'Reservar un vuelo', 'Report', 'Json'])
        return option
    
    def selectObject(self):
        option = st.selectbox('Seleccione la :', ['Avión', 'Helicoptero', 'Jet_privado', 'Vuelo', 'Puerta_de_embarque', 'Pasajero', 'Trabajador', 'Aerolinea'])
        return option
        
    
    def create_worker(self):
        st.header("Creación de Trabajador")
        
        # Entradas de texto para las características del trabajador
        ident = st.text_input("ID:", value=None)
        name = st.text_input("Nombre:", value=None)
        last_name = st.text_input("Apellido:", value=None)
        birthdate = st.date_input("Fecha de nacimiento", value=None)
        gender = st.selectbox(
        'Genero',
        ('Hombre', 'Mujer', 'Otro'))
        address = st.text_input("Dirección:", value=None)
        phone_number = st.text_input("Número de teléfono:", value=None)
        email = st.text_input("Correo electrónico:", value=None)
        position = st.text_input("Posición:", value=None)
        years_of_experience = st.text_input("Años de experiencia:", value=None)
        max_daily_hours = st.text_input("Máximo de horas diarias:", value=None)
        
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

    def create_airline(self):
        st.header("Creación de airline")
        
        ident = st.text_input("ID:", value=None)
        name = st.text_input("Nombre:",value=None)
 
        st.button("Crear", type="primary")

        if st.button and ident and name :
            airl = Airline(
                ident,
                name
            )
            return airl
        else:
            st.warning("Por favor, complete todos los campos requeridos.")

    def create_airplane(self):
        st.header("Creación de Avión")
        
        brand = st.text_input("Marca:", value=None)
        model = st.text_input("Modelo:", value=None)
        ident = st.text_input("ID:", value=None)
        capacity = st.text_input("Capacidad:", value=None)
        max_speed = st.text_input("Velocidad Máxima:", value=None)
        autonomy = st.text_input("Autonomía:", value=None)
        year = st.text_input("Año:", value=None)
        condition = st.text_input("Condición:", value=None)
        max_altitude = st.text_input("Altitud Máxima:", value=None)
        engine_amount = st.text_input("Cantidad de Motores:", value=None)
        category = st.text_input("Categoría:", value=None)

        st.button("Crear", type="primary")
        
        if st.button and brand and model and ident and capacity and max_speed and autonomy and year and condition:
            airplane = Airplane(
                brand,
                model,
                ident,
                capacity,
                max_speed,
                autonomy,
                year,
                condition,
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
        brand = st.text_input("Marca:", value=None)
        model = st.text_input("Modelo:", value=None)
        ident = st.text_input("ID:", value=None)
        capacity = st.text_input("Capacidad:", value=None)
        max_speed = st.text_input("Velocidad Máxima:", value=None)
        autonomy = st.text_input("Autonomía:", value=None)
        year = st.text_input("Año:", value=None)
        condition = st.text_input("Condición:", value=None)
        #availability = st.text_input("Disponibilidad:", value=None)
        engine_amount = st.text_input("Cantidad de Motores:", value=None)
        elevation_capacity = st.text_input("Capacidad de Elevación:", value=None)
        use = st.text_input("Uso:", value=None)
        
        st.button("Crear", type="primary")

        if st.button and brand and model and ident and capacity and max_speed and autonomy and year and condition and engine_amount and elevation_capacity and use:
            helicopter = Helicopter(
                brand,
                model,
                ident,
                capacity,
                max_speed,
                autonomy,
                year,
                condition,
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
        brand = st.text_input("Marca:", value=None)
        model = st.text_input("Modelo:", value=None)
        ident = st.text_input("ID:")
        capacity = st.text_input("Capacidad:", value=None)
        max_speed = st.text_input("Velocidad Máxima:", value=None)
        autonomy = st.text_input("Autonomía:", value=None)
        year = st.text_input("Año:", value=None)
        condition = st.text_input("Condición:", value=None)
        #availability = st.text_input("Disponibilidad:", value=None)
        owner = st.text_input("Propietario:", value=None)
        services = st.text_input("Servicios (separe los servicios por espacios)", value=None)
        destinations = st.text_input("Destinos (separe los detinos por espacios)", value=None)
        lServices = []
        lDestinations = []
        lServices = services.split()
        lDestinations = destinations.split()
        st.button("Crear", type="primary")

        if st.button and brand and model and ident and capacity and max_speed and autonomy and year and condition  and owner and lServices and lDestinations:
            jet = PrivateJet(
                brand,
                model,
                ident,
                capacity,
                max_speed,
                autonomy,
                year,
                condition,
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
        ident = st.text_input("ID:", value=None)
        name = st.text_input("Nombre:", value=None)
        last_name = st.text_input("Apellido:", value=None)
        birthdate = st.date_input("Fecha de nacimiento", value=None)
        gender = st.selectbox(
        'Genero',
        ('Hombre', 'Mujer', 'Otro'))
        address = st.text_input("Dirección:", value=None)
        phone_number = st.text_input("Número de teléfono:", value=None)
        email = st.text_input("Correo electrónico:", value=None)
        nationality = option = st.selectbox("Selecciona tu nacionalidad", paises)
        baggage_amount = st.text_input("Cantidad de equipaje:", value=None)
        medical_information = st.text_input("Información médica:", value=None)
        
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
        ident = st.text_input("ID:", value=None)
        location = st.text_input("Ubicación:", value=None)
        availability = st.text_input("Disponibilidad:", value=None)
        boarding_hour = st.text_input("Hora de abordaje:", value=None)
        
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
        
        
    def create_flight(self, names, tripu):
        st.header("Creación de vuelo")
        
        ident = st.text_input("ID:", value=None)
        date = st.date_input("Fecha:", value=None)
        origin = st.text_input("Origen:", value=None)
        destination = st.text_input("Destino:", value=None)
        available_seats = st.text_input("Sillas disponibles:", value=None)
        airl = st.selectbox("Seleccione la aerolinea asociada", names)
        if len(tripu) == 0:
            st.warning("Deben de existir minimo 3 trabajadores")
        else:
            crew = st.selectbox("Seleccione la tripulación asociada", tripu)
        st.button("Crear", type="primary")

        if st.button and ident and date and origin and destination and available_seats and airl:
            flight = Flight(
                ident,
                date,
                origin,
                destination,
                int(available_seats),
                airl,
                crew
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
        

    def listAllAirplanes(self, airplanes):
        st.header("Módulo de visualización de aviones")
        
        if not airplanes:
            st.info("No hay aviones creados hasta el momento", icon="ℹ️")
            return

        data = {'ID': [], 'Brand': [], 'Model': [], 'Capacity': [], 'Max Speed': [],
                'Autonomy': [], 'Year': [], 'Condition': [],
                'Max Altitude': [], 'Engine Amount': [], 'Category': [], 'Estado': [], 'Cantidad de vuelos asociados': []}

        for id, airplane in airplanes.items():
            data['ID'].append(id)
            data['Brand'].append(airplane.brand)
            data['Model'].append(airplane.model)
            data['Capacity'].append(airplane.capacity)
            data['Max Speed'].append(airplane.max_speed)
            data['Autonomy'].append(airplane.autonomy)
            data['Year'].append(airplane.year)
            data['Condition'].append(airplane.condition)
            data['Max Altitude'].append(airplane.max_altitude)
            data['Engine Amount'].append(airplane.engine_amount)
            data['Category'].append(airplane.category)
            data['Estado'].append(airplane.state)
            data['Cantidad de vuelos asociados'].append(airplane.assigned_flightsNum)

        st.dataframe(pd.DataFrame(data))

    def listAllGates(self,gates):
        st.header("Módulo de visualización de puertas de embarque")
        
        if not gates:
            st.info("No hay puertas de embarque creadas hasta el momento", icon="ℹ️")
            return

        data = {'ID': [], 'Location': [], 'Availability': [], 'Boarding Hour': []}

        for id, gate in gates.items():
            data['ID'].append(id)
            data['Location'].append(gate.location)
            data['Availability'].append(gate.availability)
            data['Boarding Hour'].append(gate.boarding_hour)

        st.dataframe(pd.DataFrame(data))
        
    def listAllHelicopters(self, helicopters):
        st.header("Módulo de visualización de helicópteros")
        
        if not helicopters:
            st.info("No hay helicópteros creados hasta el momento", icon="ℹ️")
            return

        data = {'ID': [], 'Brand': [], 'Model': [], 'Capacity': [], 'Max Speed': [],
                'Autonomy': [], 'Year': [], 'Condition': [], 'Ubication': [],
                'Engine Amount': [], 'Elevation Capacity': [], 'Use': []}

        for id, helicopter in helicopters.items():
            data['ID'].append(id)
            data['Brand'].append(helicopter.brand)
            data['Model'].append(helicopter.model)
            data['Capacity'].append(helicopter.capacity)
            data['Max Speed'].append(helicopter.max_speed)
            data['Autonomy'].append(helicopter.autonomy)
            data['Year'].append(helicopter.year)
            data['Condition'].append(helicopter.condition)
            data['Ubication'].append(helicopter.ubication)
            data['Engine Amount'].append(helicopter.engine_amount)
            data['Elevation Capacity'].append(helicopter.elevation_capacity)
            data['Use'].append(helicopter.use)

        st.dataframe(pd.DataFrame(data))
        
    def listAllPrivateJets(self,private_jets):
        st.header("Módulo de visualización de jets privados")
        
        if not private_jets:
            st.info("No hay jets privados creados hasta el momento", icon="ℹ️")
            return

        data = {'ID': [], 'Brand': [], 'Model': [], 'Capacity': [], 'Max Speed': [],
                'Autonomy': [], 'Year': [], 'Condition': [],
                'Owner': [], 'Services': [], 'Destinations': []}

        for id, jet in private_jets.items():
            data['ID'].append(id)
            data['Brand'].append(jet.brand)
            data['Model'].append(jet.model)
            data['Capacity'].append(jet.capacity)
            data['Max Speed'].append(jet.max_speed)
            data['Autonomy'].append(jet.autonomy)
            data['Year'].append(jet.year)
            data['Condition'].append(jet.condition)
            data['Owner'].append(jet.owner)
            data['Services'].append(jet.services)
            data['Destinations'].append(jet.destinations)

        st.dataframe(pd.DataFrame(data))
        
    def listAllPassengers(self, passengers):
        st.header("Módulo de visualización de pasajeros")
        
        if not passengers:
            st.info("No hay pasajeros creados hasta el momento", icon="ℹ️")
            return

        data = {'ID': [], 'Name': [], 'Last Name': [], 'Birthdate': [], 'Gender': [],
                'Address': [], 'Phone Number': [], 'Email': [], 'Nationality': [],
                'Baggage Amount': [], 'Medical Information': []}

        for id, passenger in passengers.items():
            data['ID'].append(id)
            data['Name'].append(passenger.name)
            data['Last Name'].append(passenger.lastName)
            data['Birthdate'].append(passenger.birthdate)
            data['Gender'].append(passenger.gender)
            data['Address'].append(passenger.address)
            data['Phone Number'].append(passenger.phoneNumber)
            data['Email'].append(passenger.email)
            data['Nationality'].append(passenger.nationality)
            data['Baggage Amount'].append(passenger.baggageAmount)
            data['Medical Information'].append(passenger.medicalInformation)

        st.dataframe(pd.DataFrame(data))
        
    def listAllWorkers(self, workers):
        st.header("Módulo de visualización de trabajadores")
        
        if not workers:
            st.info("No hay trabajadores creados hasta el momento", icon="ℹ️")
            return

        data = {'ID': [], 'Name': [], 'Last Name': [], 'Birthdate': [], 'Gender': [],
                'Address': [], 'Phone Number': [], 'Email': [], 'Position': [],
                'Years of Experience': [], 'Max Daily Hours': []}

        for id, worker in workers.items():
            data['ID'].append(id)
            data['Name'].append(worker.name)
            data['Last Name'].append(worker.lastName)
            data['Birthdate'].append(worker.birthdate)
            data['Gender'].append(worker.gender)
            data['Address'].append(worker.address)
            data['Phone Number'].append(worker.phoneNumber)
            data['Email'].append(worker.email)
            data['Position'].append(worker.position)
            data['Years of Experience'].append(worker.yearsOfExperience)
            data['Max Daily Hours'].append(worker.maxDailyHours)

        st.dataframe(pd.DataFrame(data))
        
    def listAllFlights(self,flights):
        st.header("Módulo de visualización de vuelos")
        
        if not flights:
            st.info("No hay vuelos creados hasta el momento", icon="ℹ️")
            return

        data = {'ID': [], 'Date': [], 'Origin': [], 'Destination': [], 'available_seats': [], 'Aerolinea': [] }

        for id, flight in flights.items():
            data['ID'].append(id)
            if flight.date is not None:
                data['Date'].append(flight.date)
            if flight.origin is not None:
                data['Origin'].append(flight.origin)
            if flight.destination is not None:
                data['Destination'].append(flight.destination)
            if flight.available_seats is not None:
                data['available_seats'].append(flight.available_seats)
            if flight.airline is not None:
                data['Aerolinea'].append(flight.airline)

        st.dataframe(pd.DataFrame(data))
        
    def listAllAirlines(self, airlines):
        st.header("Módulo de visualización de aerolíneas")
        
        if not airlines:
            st.info("No hay aerolíneas creadas hasta el momento", icon="ℹ️")
            return

        data = {'ID': [], 'Name': []}

        for id, airline in airlines.items():
            data['ID'].append(id)
            if airline.name is not None:
                data['Name'].append(airline.name)

        st.dataframe(pd.DataFrame(data))
    
    def selectPasajero(self, names):
        p = st.selectbox("Seleccione el pasajero que va reservar un vuelo:", names)
        return p
    def selectAerolinea(self, names):
        a = st.selectbox("Seleccione una aerolinea:", names)
        return a
    def selectVuelo(self, names):
        v = st.selectbox("Seleccione un vuelo:", names)
        return v
    def noHayAsientos(self):
        st.error("Lo sentimos, no hay suficientes asientos disponibles para tu solicitud.")
        
    def asientosDisponibles(self, vuelo):
        st.success(f"¡Asientos reservados con éxito para el vuelo {vuelo}!")
    def noHayAvionesDisponibles(self):
        st.error("Lo sentimos, no hay aviones con disponibilidad de vuelo por el momento.")
    def noHayAviones(self):
        st.error("Lo sentimos, no existen aviones hasta el momento")
    def noHayTripulaciones(self):
        st.error("Lo sentimos, no existen tripulaciones hasta el momento")
        
    def showReport(self, ans):
        st.write(ans)
        
    def showJson(self, d):
        st.header(d["name"])
        st.subheader("Capital")
        st.write(d["capital"][0])
        st.subheader("Moneda")
        st.write(d["currency"])
        st.subheader("Región")
        st.write(d["region"])
        st.subheader("Población")
        st.write(d["population"])
        st.subheader("Bandera")
        st.image(d["flag"])
