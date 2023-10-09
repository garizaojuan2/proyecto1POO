#include "gate.h"

using namespace std;


// Constructor
    Gate::Gate(int _id, const string& _location,
         bool _availability, const string& _boardingHour, const vector<Flight>& _flightsRecord)
        : id(_id), location(_location),
          availability(_availability), boardingHour(_boardingHour), flightsRecord(_flightsRecord) {
    }

    // Métodos get
    Flight Gate::getFlightAssigned()  { return *flightAssigned; }
    int Gate::getId()  { return id; }
    string Gate::getLocation()  { return location; }
    bool Gate::isAvailable()  { return availability; }
    string Gate::getBoardingHour()  { return boardingHour; }
    vector<Flight> Gate::getFlightsRecord()  { return flightsRecord; }

    // Métodos set
    void Gate::setFlightAssigned( Flight *_flightAssigned) {flightAssigned = _flightAssigned; }
    void Gate::setId(int _id) { id = _id; }
    void Gate::setLocation(const string& _location) { location = _location; }
    void Gate::setAvailability(bool _availability) { availability = _availability; }
    void Gate::setBoardingHour(const string& _boardingHour) { boardingHour = _boardingHour; }
    void Gate::addFlightsRecord(const vector<Flight>& _flightsRecord) { flightsRecord = _flightsRecord; }
