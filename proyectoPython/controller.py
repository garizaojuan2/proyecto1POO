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
import streamlit as st
from view import View
from modeloDeRevista import TodoModel

class Controller:
    def __init__(self):
        self.view = View()
        self.model = TodoModel()
    

    def showMenu(self):
        option = self.view.menu()
        st.session_state['option'] = option
        if option == 'Crear una objeto':
            self.createObjects()
        """
        elif option == 'Ver los objetos':
            self.listAllTasks()
        elif option == 'Reservar un vuelo':
            self.checkTask()
        elif option == 'Cambiar estado de vuelo':
            self.removeTask()
        elif option == "Json":
            self.Json()
        """
    def createObjects(self):
        op = self.view.selectObject()
        if op =='Avión':
            obj = self.view.create_airplane()
            if obj:
                idd = obj.ident
                self.model.addNewAvion(idd,obj)                
        elif op == 'Helicoptero':
            obj = self.view.create_helicopter()
            if obj:
                idd = obj.ident
                self.model.addNewHelicoptero(idd,obj)  
        elif op == 'Jet_privado':
            obj = self.view.create_jet()
            if obj:
                idd = obj.ident
                self.model.addNewJetPrivado(idd,obj)  
        elif op == 'Vuelo':
            obj = self.view.create_flight()
            if obj:
                idd = obj.ident
                self.model.addNewVuelo(idd,obj)  
        elif op == 'Puerta_de_embarque':
            obj = self.view.create_gate()
            if obj:
                idd = obj.ident
                self.model.addNewPuertaDeEmbarque(idd,obj)  
        elif op == 'Pasajero':
            obj = self.view.create_passenger()
            if obj:
                idd = obj.ident
                self.model.addNewPasajero(idd,obj)  
        elif op == 'Trabajador':
            obj = self.view.create_worker()
            if obj:
                idd = obj.ident
                self.model.addNewTrabajador(idd,obj)  
            
    

            
            
