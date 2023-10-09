#include "airport.h"

using namespace std;

// Obtener la instancia única del aeropuerto

/*
Airport& Airport::getInstance() {
    return instance;
}
*/

//Airport Airport::instance;
void Airport::addAirplane(Airplane* _plane){
    airplaneRegister.push_back(_plane);
}
void Airport::addFlight(Flight* _flight){
    string dest1 = _flight->getDestination();
    string date1 = _flight->getDate();
    pair<string,string> pareja(dest1, date1);
    flightsRegister[pareja] = _flight;
}
void Airport::addGate(Gate* _gate){
    gatesRegister.push_back(_gate);
}
void Airport::addHelicopter(Helicopter* _helicopter){
    helicopterRegister.push_back(_helicopter);
}
void Airport::addJet(PrivateJet* _jet){
    privateJetRegister.push_back(_jet);
}
void Airport::assignFlight(Flight *vuelo){
  int i = 0;
  bool flag = true;
  while(flag && i < airplaneRegister.size()){
      if(airplaneRegister[i]->getAssignedFlights()< 3){
          airplaneRegister[i]->addFlight(vuelo);
          vuelo->setAirplane((airplaneRegister[i]));
          flag = false;
          cout << "El vuelo ha sido asignado al avion identificado con el codigo " << airplaneRegister[i]->getId() << endl;
      }
      i += 1;
  }

  if(flag){
    cout << "No hay aviones disponibles " << endl;
  }
}
void Airport:: buyFlight(string destination, string date){
    pair<string, string> infoRequiered(destination, date);
    map<pair<string, string>, Flight*>::iterator it = flightsRegister.find(infoRequiered);
    if(it != flightsRegister.end()){
        Flight* vuelo = flightsRegister[infoRequiered];
        int seats = vuelo->getAvailableSeats();
        if(seats <= 0)
            cout << "El vuelo para el destino y fecha seleccionada, no se encuentra disponible" << endl;
        else{
            cout << "Su reserva ha sido exitosa" << endl;
            vuelo->setAvailableSeats(seats - 1);
        }
    }
    else
        cout << "El vuelo no existe para ese destino o fecha" << endl;
}