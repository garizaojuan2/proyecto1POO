#include "gate.h"

using namespace std;


// Constructor
    Gate::Gate(int _id, const string& _location,
         bool _availability, const string& _boardingHour)
        : id(_id), location(_location),
          availability(_availability), boardingHour(_boardingHour) {
    }
    Gate::Gate(){}

    // Métodos get
    Flight Gate::getFlightAssigned()  { return *flightAssigned; }
    int Gate::getId()  { return id; }
    string Gate::getLocation()  { return location; }
    bool Gate::isAvailable()  { return availability; }
    string Gate::getBoardingHour()  { return boardingHour; }
    vector<Flight*> Gate::getFlightsRecord()  { return flightsRecord; }

    // Métodos set
    void Gate::setFlightAssigned( Flight *_flightAssigned) {flightAssigned = _flightAssigned; }
    void Gate::setId(int _id) { id = _id; }
    void Gate::setLocation(const string& _location) { location = _location; }
    void Gate::setAvailability(bool _availability) { availability = _availability; }
    void Gate::setBoardingHour(const string& _boardingHour) { boardingHour = _boardingHour; }
    void Gate::addFlightsRecord(Flight *_flight) {flightsRecord.push_back(_flight);}

    void Gate::print() {
    cout << "Gate Information:" << endl;
    cout << "ID: " << id << endl;
    cout << "Location: " << location << endl;
    cout << "Availability: " << (availability ? "Available" : "Not Available") << endl;
    cout << "Boarding Hour: " << boardingHour << endl;

    // Imprime la información del vuelo asignado
    if (flightAssigned != nullptr) {
        cout << "Flight Assigned Information:" << endl;
        flightAssigned->print();
    }

    // Imprime la información de los vuelos registrados
    cout << "Flights Record Information:" << endl;
    for (int i = 0; i < flightsRecord.size(); ++i) {
        cout << "Flight " << i + 1 << ":" << endl;
        flightsRecord[i]->print();
    }
}
