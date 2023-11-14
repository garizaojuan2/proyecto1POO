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
        
        elif option == 'Ver los objetos':
            self.verObjetos()
        
        elif option == 'Reservar un vuelo':
            self.reservar()
            
        """
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
            l = self.model.getAllAirlines()
            names = []
            for a in l:
                names.append(l[a].name)
                
            obj = self.view.create_flight(names)
            if obj:
                if len(self.model.getAllAvion()) != 0:
                    flag = self.assignFlight(obj.ident, obj.origin)
                    if flag == True:
                        idd = obj.ident
                        self.model.addNewVuelo(idd,obj) 
                         
                    else:
                        self.view.noHayAvionesDisponibles()
                else:
                    self.view.noHayAviones()
                
                torre = ControlTower.get_instance()
                torre.assign_boarding_gate(obj)
                
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
                
        elif op == 'Aerolinea':
            obj = self.view.create_airline()
            
            if obj:
                idd = obj.ident
                self.model.addNewAirline(idd,obj)  
            
    

    def verObjetos(self):
        op = self.view.selectObject()
        if op =='Avión':
            aviones = self.model.getAllAvion()   
            self.view.listAllAirplanes(aviones)  
                      
        elif op == 'Helicoptero':
            helicopteros = self.model.getAllHelicoptero()   
            self.view.listAllHelicopters(helicopteros)   
            
        elif op == 'Jet_privado':
            jets = self.model.getAllJetPrivado()
            self.view.listAllPrivateJets(jets)  
                 
        elif op == 'Vuelo':
            vuelos = self.model.getAllVuelo() 
            self.view.listAllFlights(vuelos)    
            
        elif op == 'Puerta_de_embarque':
            puertas = self.model.getAllPuertaDeEmbarque()  
            self.view.listAllGates(puertas)  
             
        elif op == 'Pasajero':
            pasajeros = self.model.getAllPasajero() 
            self.view.listAllPassengers(pasajeros) 
               
        elif op == 'Trabajador':
            trabajadores = self.model.getAllTrabajador()  
            self.view.listAllWorkers(trabajadores)   
            
        elif op == 'Aerolinea':
            aerolineas = self.model.getAllAirlines()  
            self.view.listAllAirlines(aerolineas)  


    def reservar(self):
        st.header("Reservacion de vuelos")
        l = self.model.getAllPasajero()
        names = []
        for a in l:
           names.append(l[a].name)         
        pasajero = self.view.selectPasajero(names)
        
        l = self.model.getAllAirlines()
        names = []
        for a in l:
            names.append(l[a].name)      
        aerolinea = self.view.selectAerolinea(names)
        
        l = self.model.getAllVuelo()
        names = []
        for a in l:
            if l[a].airline == aerolinea:
                names.append(l[a].ident)
        vuelo = self.view.selectVuelo(names)
        
        b = st.button("Reservar", type="primary")
        if vuelo and aerolinea and pasajero and b:
            l = self.model.getAllVuelo()
            v = l[vuelo]
            if v.available_seats <= 0:
                self.view.noHayAsientos()
            else:
                self.view.asientosDisponibles(vuelo)
                num = v.available_seats - 1
                self.model.updateSeats(vuelo, num)
                
    def assignFlight(self,ident,origin):
        ans = False
        l = self.model.getAllAvion()
        for ap in l:
            if l[ap].assigned_flightsNum < 3 and l[ap].state == "Disponible":
                ans = True
                if origin != "Cali" or l[ap].caliOrig == True:
                    if origin == "Cali":
                        self.model.updateAvion(l[ap].ident, ident, l[ap].assigned_flightsNum + 1, True)
                        return ans
                    else:
                        self.model.updateAvion(l[ap].ident, ident, l[ap].assigned_flightsNum + 1, False)
                        return ans
                
        return ans