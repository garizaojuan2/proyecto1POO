#ifndef __FLIGHT_H
#define __FLIGHT_H

#include <iostream>
#include <string>
#include "worker.h"
#include "gate.h"
#include "passenger.h"
#include <map>
#include <vector>

using namespace std;


class Flight {
private:
    int id;
    string date;
    string origin;
    string destination;
    vector<Worker> assignedCrew;
    Gate boardingGate;
    map<int, Passenger> passengersRegistered;

public:
    // Constructor
    Flight(int _id, const string& _date, const string& _origin, const string& _destination,
           const vector<Worker>& _assignedCrew, const Gate& _boardingGate,
           const map<int, Passenger>& _passengersRegistered)
        : id(_id), date(_date), origin(_origin), destination(_destination),
          assignedCrew(_assignedCrew), boardingGate(_boardingGate),
          passengersRegistered(_passengersRegistered) {
    }

    // Métodos get
    int getId() const { return id; }
    string getDate() const { return date; }
    string getOrigin() const { return origin; }
    string getDestination() const { return destination; }
    vector<Worker> getAssignedCrew() const { return assignedCrew; }
    Gate getBoardingGate() const { return boardingGate; }
    map<int, Passenger> getPassengersRegistered() const { return passengersRegistered; }

    // Métodos set
    void setId(int _id) { id = _id; }
    void setDate(const string& _date) { date = _date; }
    void setOrigin(const string& _origin) { origin = _origin; }
    void setDestination(const string& _destination) { destination = _destination; }
    void setAssignedCrew(const vector<Worker>& _assignedCrew) { assignedCrew = _assignedCrew; }
    void setBoardingGate(const Gate& _boardingGate) { boardingGate = _boardingGate; }
    void setPassengersRegistered(const map<int, Passenger>& _passengersRegistered) {
        passengersRegistered = _passengersRegistered;
    }
};

#endif