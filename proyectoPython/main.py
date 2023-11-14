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
from controller import Controller
from airline import Airline
import streamlit as st

def main():
    controller = Controller()
    
    if "person1" not in st.session_state:
        person1 = Passenger(
        _ident=1,
        _name="John",
        _lastName="Doe",
        _birthdate="01/15/1990",
        _gender="Male",
        _address="123 Main St",
        _phoneNumber="555-1234",
        _email="john.doe@example.com",
        _nationality="American",
        _baggageAmount=2,
        _medicalInformation="No known medical conditions"
        
        )
        controller.model.addNewPasajero(1,person1)
        
    if "person2" not in st.session_state:
        person2 = Passenger(
            _ident=2,
            _name="Jane",
            _lastName="Smith",
            _birthdate="05/20/1985",
            _gender="Female",
            _address="456 Oak St",
            _phoneNumber="555-5678",
            _email="jane.smith@example.com",
            _nationality="Canadian",
            _baggageAmount=1,
            _medicalInformation="Allergic to peanuts"
            
        )
        controller.model.addNewPasajero(2,person2)
        
    if "person3" not in st.session_state:
        person3 = Passenger(
            _ident=3,
            _name="Bob",
            _lastName="Johnson",
            _birthdate="12/10/1995",
            _gender="Male",
            _address="789 Pine St",
            _phoneNumber="555-9876",
            _email="bob.johnson@example.com",
            _nationality="British",
            _baggageAmount=3,
            _medicalInformation="Requires prescription medication"
        )
        controller.model.addNewPasajero(3,person3)
   
    
    
    
    
    airlines_data = [
        {"i": 1, "n": "Copa"},
        {"i": 2, "n": "Avianca"},
    ]

    for airline_data in airlines_data:
        airline_key = f"airline{airline_data['i']}"
        if airline_key not in st.session_state:
            airline = Airline(**airline_data)
            controller.model.addNewAirline(airline_data["i"], airline)
            st.session_state[airline_key] = airline

   

    airplanes_data = [
        {
            "brand": "Boeing",
            "model": "747",
            "ident": "ABC123",
            "capacity": 500,
            "max_speed": 900,
            "autonomy": 5000,
            "year": 2020,
            "condition": "Good",
            "max_altitude": 35000,
            "engine_amount": 4,
            "category": "Commercial",
        },
        {
            "brand": "Airbus",
            "model": "A320",
            "ident": "XYZ789",
            "capacity": 200,
            "max_speed": 800,
            "autonomy": 4500,
            "year": 2018,
            "condition": "Excellent",
            "max_altitude": 32000,
            "engine_amount": 2,
            "category": "Commercial",
        },
    ]

    for airplane_data in airplanes_data:
        airplane_key = f"airplane{airplane_data['ident']}"
        if airplane_key not in st.session_state:
            airplane = Airplane(**airplane_data)
            controller.model.addNewAvion(airplane_data["ident"], airplane)
            st.session_state[airplane_key] = airplane
    
    controller.showMenu()
    

main()