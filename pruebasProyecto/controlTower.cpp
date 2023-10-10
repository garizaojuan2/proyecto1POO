#include "controlTower.h"

using namespace std;

void ControlTower::aircraftTakeOff(Aircraft* aircraft) {
    string msg = "El avion " + aircraft->getId() + " ha despegado.";
    cout << "Torre de Control: " << msg << endl;
    notify(aircraft, msg);

    int i = 0;
    bool flag = true;
    while(i < gates.size() && flag){
        if(gates[i]->getFlightAssigned().getId() == aircraft->getFlightAsociated()->getId()){
        flag = false;
        gates[i]->setAvailability(true);
        }
        i++;
    }
}

void ControlTower::aircraftLanded(Aircraft* aircraft) {
    string msg = "El avion " + aircraft->getId() + " ha aterrizado.";
    cout << "Torre de Control: " << msg << endl;
    notify(aircraft, msg);
}

void ControlTower::aircrafInFlight(Aircraft* aircraft, const string& ubicacion) {
    string msg = "El avion " + aircraft->getId() + " informa su ubicacion: " + ubicacion;
    cout << "Torre de Control: " << msg << endl;
    notify(aircraft, msg);
}

void ControlTower::notify(Aircraft* aircraft, const string& msg) {
    for (Aircraft* otherAircraft : aircrafts) {
        if (otherAircraft != aircraft) {
            otherAircraft->recibeInfo(msg);
        }
    }
}

void ControlTower::addAircraft(Aircraft* aircraft) {
        aircrafts.push_back(aircraft);
    }

void ControlTower::assignBoardingGate(Flight *flight){
    int i = 0;
    bool flag = true;
    while(i < gates.size() && flag){
        if(gates[i]->isAvailable())
        flag = false;
        i++;
    }
    if(!flag){
        gates[i]->setFlightAssigned(flight);
        gates[i]->setAvailability(false);
        gates[i]->addFlightsRecord(flight);
        flight->setBoardingGate(gates[i]);
        cout << "El vuelo " << flight->getId() << " se ha asociado a la puerta: Gate " << this->gates[i]->getId();  
    }
    else{
        cout << "No hay puertas de embarque disponibles" << endl;
    }

   
}