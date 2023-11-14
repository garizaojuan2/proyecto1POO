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
from crew import Crew
import json
import requests
import pandas as pd

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
            
        
        elif option == 'Report':
            self.report()
        elif option == "Json":
            self.showJson()
        
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
            tripu = []
            for a in l:
                names.append(l[a].name)
            l2 = self.model.getAllTrabajador()
            num = 1
            total = len(l2)//3
            while num < total:
                cad = f"Tripulación #{num}"
                tripu.append(cad)
                num += 1
                
            obj = self.view.create_flight(names,tripu)
            if obj:
                if len(self.model.getAllAvion()) != 0:
                    flag1 = self.assignFlight(obj.ident, obj.origin)
                    if flag1 == True:
                        idd = obj.ident
                        self.model.addNewVuelo(idd,obj) 
                         
                    else:
                        self.view.noHayAvionesDisponibles()
                else:
                    self.view.noHayAviones()
                if total == 0:
                    self.view.noHayTripulaciones()
                    flag2 = False

                if flag1 and flag2:
                    self.model.addNewVuelo(idd,obj)               

                
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
                self.model.addNewTrabajador(idd, obj)
                
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


   """
        Gestiona el proceso de reservación de vuelos.

        Muestra la interfaz de usuario para la selección de pasajero, aerolínea y vuelo.
        Permite al usuario reservar un vuelo si hay asientos disponibles.
        Actualiza la cantidad de asientos disponibles después de realizar la reserva.

    """
    def reservar(self):
        st.header("Reservación de vuelos")
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
        
        self.view.showFlight(vuelo, self.model.getAllVuelo())
        
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
        flag = True
        for ap in l:
            if l[ap].assigned_flightsNum < 3 and l[ap].state == "Disponible" and flag:
                ans = True
                if origin != "Cali" or l[ap].caliOrig == True:
                    flag = False
                    if origin == "Cali":
                        self.model.updateAvion(l[ap].ident, ident, l[ap].assigned_flightsNum + 1, True)
                    else:
                        self.model.updateAvion(l[ap].ident, ident, l[ap].assigned_flightsNum + 1, False)
                
        return ans
    
    
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
            if l[ap].assigned_flightsNum < 3:
                ans = True
                if origin != "Cali" or l[ap].caliOrig == True:
                    if origin == "Cali":
                        self.model.updateAvion(l[ap].ident, ident, l[ap].assigned_flightsNum + 1, True)
                        return ans
                    else:
                        self.model.updateAvion(l[ap].ident, ident, l[ap].assigned_flightsNum + 1, False)
                        return ans
                
        return ans
    
    def report(self):
        ans = ""
        st.header("Reporte de trafico")
        l = list(self.model.getAllAvion().keys())
        torre = ControlTower.get_instance()

        for i in range(len(l)):
            ans += f"\nEl avión #{l[i]} se encuentra en puerta de embarque \n"
            for j in range(len(l)):
                if i != j:
                    ans += f"\nEl avion #{l[j]} ha recibido el mensaje\n"
        ans += "\n"
        
        for i in range(len(l)):
            ans += f"\nEl avión #{l[i]} esta en pista \n"
            for j in range(len(l)):
                if i != j:
                    ans += f"\nEl avion #{l[j]} ha recibido el mensaje\n"
        ans += "\n"
        
        for i in range(len(l)):
            ans += f"\nEl avión #{l[i]} ha despegado \n"
            for j in range(len(l)):
                if i != j:
                    ans += f"\nEl avion #{l[j]} ha recibido el mensaje\n"
        ans += "\n"
        
        for i in range(len(l)):
            ans += f"\nEl avión #{l[i]} esta en vuelo \n"
            for j in range(len(l)):
                if i != j:
                    ans += f"\nEl avion #{l[j]} ha recibido el mensaje\n"
        ans += "\n"
        
        for i in range(len(l)):
            ans += f"\nEl avión #{l[i]} ha aterrizado \n"
            for j in range(len(l)):
                if i != j:
                    ans += f"\nEl avion #{l[j]} ha recibido el mensaje\n"
        ans += "\n"
        
        self.view.showReport(ans)
                
    def showJson(self):
        contry = st.text_input("Ingrese un país:") 
        b = st.button("Consultar") 
        a = self.consultarApi(contry)
        if contry != "Error en la consulta de los datos" and b:
            b = self.getCountriesData2(a)
            self.view.showJson(b)
        
            
            
    def consultarApi(self,country):
        url = "https://restcountries.com/v3.1/name/" + country
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        else:
 
            return ("Error en la consulta de los datos")


    def getCountriesData2(self,data):
        if data != type(str):
            d={}
            d["name"]=data[0]["name"]["official"]
            d["capital"]=data[0]["capital"]
            cur = ""
            i=0
            for key in data[0]["currencies"]:
                cur = key
                i+=1
                if i>=1:
                    break
            d["currency"]=data[0]["currencies"][cur]["name"]
            d["region"]=data[0]["region"]
            d["population"]=data[0]["population"]
            d["flag"]=data[0]["flags"]["png"]
        return d
        


