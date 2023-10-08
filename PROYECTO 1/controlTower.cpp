#include "controlTower.h"

using namespace std;

void ControlTower::aircraftTakeOff(Aircraft* aircraft) {
    string msg = "El avion " + aircraft->getId() + " ha despegado.";
    cout << "Torre de Control: " << msg << endl;
    notify(aircraft, msg);
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