#include "aircraft.h"
#include "controlTower.h"
#include "aircraft.h"

using namespace std;

// Constructor
Aircraft::Aircraft(const string& _brand, const string& _model, const string& _id, int _capacity, int _maxSpeed,
    int _autonomy, int _year, const string& _condition, const string& _ubication,
    bool _availability)
    : brand(_brand), model(_model), id(_id), capacity(_capacity), maxSpeed(_maxSpeed),
    autonomy(_autonomy), year(_year), condition(_condition), ubication(_ubication),
    availability(_availability){
    }
Aircraft::Aircraft(){}

// Métodos get
string Aircraft::getBrand()  { return brand; }
string Aircraft::getModel()  { return model; }
string Aircraft::getId() { return id;}
int Aircraft::getCapacity()  { return capacity; }
int Aircraft::getMaxSpeed()  { return maxSpeed; }
int Aircraft::getAutonomy()  { return autonomy; }
int Aircraft::getYear()  { return year; }
string Aircraft::getCondition()  { return condition; }
string Aircraft::getUbication()  { return ubication; }
bool Aircraft::isAvailable()  { return availability; }
Flight* Aircraft::getFlightAsociated() {return flightAssociated;}
int Aircraft::getAssignedFlights(){return assignedFlights.size();}

// Métodos set
void Aircraft::setBrand(const string& _brand) { brand = _brand; }
void Aircraft::setModel(const string& _model) { model = _model; }
void Aircraft::setId(const string& _id) { id = _id;}
void Aircraft::setCapacity(int _capacity) { capacity = _capacity; }
void Aircraft::setMaxSpeed(int _maxSpeed) { maxSpeed = _maxSpeed; }
void Aircraft::setAutonomy(int _autonomy) { autonomy = _autonomy; }
void Aircraft::setYear(int _year) { year = _year; }
void Aircraft::setCondition(const string& _condition) { condition = _condition; }
void Aircraft::setUbication(const string& _ubication) { ubication = _ubication; }
void Aircraft::setAvailability(bool _availability) { availability = _availability; }
void Aircraft::setFlightAsociated(Flight *_flightAssociated) {flightAssociated = _flightAssociated;}

// Funcionalidades

void Aircraft::takeOff() {
    ControlTower::getInstance().aircraftTakeOff(this);

}

void Aircraft::landed() {
    ControlTower::getInstance().aircraftLanded(this);
}

void Aircraft::reportLocation(const string& ubicacion) {
    ControlTower::getInstance().aircrafInFlight(this, ubicacion);
}

void Aircraft::recibeInfo(const string& mensaje) {
    cout << "Avion " << id << " recibio un mensaje: " << mensaje << endl;
}

void Aircraft::addFlight(Flight *flight){
    assignedFlights.push_back(flight);
}
void Aircraft::print() const {
    cout << "Aircraft Information:" << endl;
    cout << "Brand: " << brand << endl;
    cout << "Model: " << model << endl;
    cout << "ID: " << id << endl;
    cout << "Capacity: " << capacity << " passengers" << endl;
    cout << "Max Speed: " << maxSpeed << " km/h" << endl;
    cout << "Autonomy: " << autonomy << " km" << endl;
    cout << "Year: " << year << endl;
    cout << "Condition: " << condition << endl;
    cout << "Ubication: " << ubication << endl;
    cout << "Availability: " << (availability ? "Available" : "Not Available") << endl;

    if (flightAssociated) {
        cout << "Flight Associated:" << endl;
        cout << "Flight Number: " << flightAssociated->getFlightNumber() << endl;
        cout << "Flight Details:" << endl;
        flightAssociated->print();
    }

    cout << "Assigned Flights:" << endl;
    for (int i = 0; i < assignedFlights.size(); i++) {
        cout << "Flight Number: " <<  i + 1<< endl;
        cout << "Flight Details:" << endl;
        flight->print();
    }
}
