from aircraft import Aircraft
from airplane import Airplane
from airport import Airport
#from controlTower import ControlTower
from flight import Flight
from gate import Gate
from helicopter import Helicopter
from jet import PrivateJet
from passenger import Passenger
from person import Person
from worker import Worker
import streamlit as st


class TodoModel:
    def __init__(self):
        if 'trabajador' not in st.session_state:
            st.session_state['trabajador'] = {}
            self.trabajador = {}
        else:
            self.trabajador = st.session_state['trabajador']

        if 'avion' not in st.session_state:
            st.session_state['avion'] = {}
            self.avion = {}
        else:
            self.avion = st.session_state['avion']

        if 'helicoptero' not in st.session_state:
            st.session_state['helicoptero'] = {}
            self.helicoptero = {}
        else:
            self.helicoptero = st.session_state['helicoptero']

        if 'jet_privado' not in st.session_state:
            st.session_state['jet_privado'] = {}
            self.jet_privado = {}
        else:
            self.jet_privado = st.session_state['jet_privado']

        if 'pasajero' not in st.session_state:
            st.session_state['pasajero'] = {}
            self.pasajero = {}
        else:
            self.pasajero = st.session_state['pasajero']

        if 'puerta_de_embarque' not in st.session_state:
            st.session_state['puerta_de_embarque'] = {}
            self.puerta_de_embarque = {}
        else:
            self.puerta_de_embarque = st.session_state['puerta_de_embarque']
        
        if 'vuelo' not in st.session_state:
            st.session_state['vuelo'] = {}
            self.vuelo = {}
        else:
            self.vuelo = st.session_state['vuelo']
            
        if 'aerolinea' not in st.session_state:
            st.session_state['aerolinea'] = {}
            self.airline = {}
        else:
            self.airline = st.session_state['aerolinea']
    # C - Create
    def addNewTrabajador(self, id, trabajador):
        self.trabajador[id] = trabajador
        st.session_state['trabajador'] = self.trabajador

    def addNewAvion(self, id, avion):
        self.avion[id] = avion
        st.session_state['avion'] = self.avion

    def addNewHelicoptero(self, id, helicoptero):
        self.helicoptero[id] = helicoptero
        st.session_state['helicoptero'] = self.helicoptero

    def addNewJetPrivado(self, id, jet_privado):
        self.jet_privado[id] = jet_privado
        st.session_state['jet_privado'] = self.jet_privado

    def addNewPasajero(self, id, pasajero):
        self.pasajero[id] = pasajero
        st.session_state['pasajero'] = self.pasajero

    def addNewPuertaDeEmbarque(self, id, puerta_de_embarque):
        self.puerta_de_embarque[id] = puerta_de_embarque
        st.session_state['puerta_de_embarque'] = self.puerta_de_embarque

    def addNewVuelo(self, id, vuelo):
        self.vuelo[id] = vuelo
        st.session_state['vuelo'] = self.vuelo
        
    def addNewAirline(self, id, airline):
        self.airline[id] = airline
        st.session_state['aerolinea'] = self.airline

    # R - Read
    def getAllTrabajador(self):
        return self.trabajador

    def getAllAvion(self):
        return self.avion

    def getAllHelicoptero(self):
        return self.helicoptero

    def getAllJetPrivado(self):
        return self.jet_privado

    def getAllPasajero(self):
        return self.pasajero

    def getAllPuertaDeEmbarque(self):
        return self.puerta_de_embarque
    
    def getAllVuelo(self):
        return self.vuelo
    
    def getAllAirlines(self):
        return self.airline
     # R - Read
    

    # U - Update
    
    def updateSeats(self, ident, num):
        self.vuelo[ident].set_available_seats(num)
    
    def updateAvion(self,ident,fA, afn, cO):
        self.avion[ident].set_flight_associated(fA)
        self.avion[ident].add_flight(fA)
        self.avion[ident].setAssociatedNum(afn)
        self.avion[ident].setCaliOrig(cO)
        
        
    """
    def checkTrabajador(self, trabajadorid):
        self.trabajador[trabajadorid].setState("Completada")
    
    def checkAirline(self, airline_id):
        # Implementar la lógica de actualización según sea necesario
        pass

    def checkAvion(self, avionid):
        self.avion[avionid].setState("Completada")

    def checkHelicoptero(self, helicoptero_id):
        self.helicoptero[helicoptero_id].setState("Completada")

    def checkJetPrivado(self, jet_privado_id):
        self.jet_privado[jet_privado_id].setState("Completada")

    def checkPasajero(self, pasajero_id):
        self.pasajero[pasajero_id].setState("Completada")

    def checkPuertaDeEmbarque(self, puerta_id):
        self.puerta_de_embarque[puerta_id].setState("Completada")
        
    
    """
    
    # D - Delete
    def removeTrabajador(self, trabajadorid):
        del self.trabajador[trabajadorid]

    def removeAvion(self, avionid):
        del self.avion[avionid]

    def removeHelicoptero(self, helicoptero_id):
        del self.helicoptero[helicoptero_id]

    def removeJetPrivado(self, jet_privado_id):
        del self.jet_privado[jet_privado_id]

    def removePasajero(self, pasajero_id):
        del self.pasajero[pasajero_id]

    def removePuertaDeEmbarque(self, puerta_id):
        del self.puerta_de_embarque[puerta_id]
    def removeAirline(self, airline_id):
        del self.airline[airline_id]