#ifndef __GATE_H
#define __GATE_H

#include <iostream>
#include <string>
#include "flight.h"
#include <vector>

class Flight;

class Gate {
private:
    Flight* flightAssigned;
    int id;
    string location;
    bool availability;
    string boardingHour;
    vector<Flight> flightsRecord;

public:
    // Constructor
    Gate(int _id, const string& _location,
         bool _availability, const string& _boardingHour, const vector<Flight>& _flightsRecord);

    // Métodos get
    Flight getFlightAssigned();
    int getId();
    string getLocation();
    bool isAvailable();
    string getBoardingHour();
    vector<Flight> getFlightsRecord();

    // Métodos set
    void setFlightAssigned(Flight *_flightAssigned);
    void setId(int _id);
    void setLocation(const string& _location);
    void setAvailability(bool _availability);
    void setBoardingHour(const string& _boardingHour);
    void addFlightsRecord(const vector<Flight>& _flightsRecord);
};

#endif