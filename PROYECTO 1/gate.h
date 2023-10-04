#ifndef __GATE_H
#define __GATE_H

#include <iostream>
#include <string>
#include "flight.h"
#include <vector>

class Gate {
private:
    Flight flightAssigned;
    int id;
    string location;
    bool availability;
    string boardingHour;
    vector<Flight> flightsRecord;

public:
    // Constructor
    Gate(const Flight& _flightAssigned, int _id, const string& _location,
         bool _availability, const string& _boardingHour, const vector<Flight>& _flightsRecord)
        : flightAssigned(_flightAssigned), id(_id), location(_location),
          availability(_availability), boardingHour(_boardingHour), flightsRecord(_flightsRecord) {
    }

    // Métodos get
    Flight getFlightAssigned() const { return flightAssigned; }
    int getId() const { return id; }
    string getLocation() const { return location; }
    bool isAvailable() const { return availability; }
    string getBoardingHour() const { return boardingHour; }
    vector<Flight> getFlightsRecord() const { return flightsRecord; }

    // Métodos set
    void setFlightAssigned(const Flight& _flightAssigned) { flightAssigned = _flightAssigned; }
    void setId(int _id) { id = _id; }
    void setLocation(const string& _location) { location = _location; }
    void setAvailability(bool _availability) { availability = _availability; }
    void setBoardingHour(const string& _boardingHour) { boardingHour = _boardingHour; }
    void setFlightsRecord(const vector<Flight>& _flightsRecord) { flightsRecord = _flightsRecord; }
};

#endif