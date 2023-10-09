#include "airport.h"

using namespace std;

// Obtener la instancia única del aeropuerto
Airport& Airport::getInstance() {
    return instance;
}

void Airport::assignFlight(Aircraft &aircrft, Flight &flight, Gate &gate){
  
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
        cout << "El vuelo no está disponible" << endl;
}
