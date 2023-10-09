#include "airport.h"

using namespace std;

// Obtener la instancia única del aeropuerto
Airport& Airport::getInstance() {
    return instance;
}

void Airport::assignFlight(Flight &vuelo){
  int i = 0;
  bool flag = true;
  while(flag && i < airplaneRegister.size()){
      if(airplaneRegister[i].getAssignedFlights().size() < 3){
          airplaneRegister[i].addFlight();
          vuelo.setAirplane(airplaneRegister[i]);
          flag = false;
      }
      i += 1;
  }
}

void Airport:: buyFlight(string destination, string date){
    pair<string, string> infoRequiered(destination, date);
    map<pair<string, string>, Flight>::iterator it = flightsRegister.find(infoRequiered);
    if(it != flightsRegister.end()){
        if((*it).getAvailableSeats() <= 0)
            cout << "El vuelo para el destino y fecha seleccionada, no se encuentra disponible" << endl;
        else{
            cout << "Su reserva ha sido exitosa" << endl;
            (*it).setAvailableSeats((*it).getAvailableSeats() - 1);
        }
        }
    else
        cout << "El vuelo no existe para ese destino o fecha" << endl;
}
