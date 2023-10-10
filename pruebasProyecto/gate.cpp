#include "gate.h"
using namespace std;

// Constructor de la clase Gate
Gate::Gate(int _id, const string& _location,
         bool _availability, const string& _boardingHour)
        : id(_id), location(_location),
          availability(_availability), boardingHour(_boardingHour) {
}

// Constructor vacío de la clase Gate
Gate::Gate(){}

// Métodos get para obtener los valores de los atributos
Flight Gate::getFlightAssigned()  { return *flightAssigned; }
int Gate::getId()  { return id; }
string Gate::getLocation()  { return location; }
bool Gate::isAvailable()  { return availability; }
string Gate::getBoardingHour()  { return boardingHour; }
vector<Flight*> Gate::getFlightsRecord()  { return flightsRecord; }

// Métodos set para modificar los valores de los atributos
void Gate::setFlightAssigned(Flight *_flightAssigned) {flightAssigned = _flightAssigned; }
void Gate::setId(int _id) { id = _id; }
void Gate::setLocation(const string& _location) { location = _location; }
void Gate::setAvailability(bool _availability) { availability = _availability; }
void Gate::setBoardingHour(const string& _boardingHour) { boardingHour = _boardingHour; }

// Agregar un vuelo al registro de vuelos en la puerta
void Gate::addFlightsRecord(Flight *_flight) {
    flightsRecord.push_back(_flight);
}