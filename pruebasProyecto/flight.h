#ifndef __FLIGHT_H
#define __FLIGHT_H

#include <iostream>
#include <string>
#include "worker.h"
#include "gate.h"
#include "passenger.h"
#include <map>
#include <vector>
#include "aircraft.h"
#include "airplane.h"

using namespace std;

class Aircraft;
class Gate;

class Flight {
private:
    int id;
    string date;
    string origin;
    string destination;
    vector<Worker*> assignedCrew;
    Gate* boardingGate;
    map<int, Passenger*> passengersRegistered;
    Airplane* airplane;
    int availableSeats;


public:
    // Constructor
    Flight(int _id, const string& _date, const string& _origin, const string& _destination,
           const vector<Worker*>& _assignedCrew,
           const map<int, Passenger*>& _passengersRegistered);
    Flight();
    

    // Métodos get
    int getId();
    string getDate() ;
    string getOrigin() ;
    string getDestination();
    vector<Worker*> getAssignedCrew();
    Gate* getBoardingGate();
    map<int, Passenger*> getPassengersRegistered();
    Airplane* getAirplane();
    int getAvailableSeats();
        
    

    // Métodos set
    void setId(int _id);
    void setDate(const string& _date);
    void setOrigin(const string& _origin);
    void setDestination(const string& _destination);
    void setAssignedCrew(const vector<Worker*>& _assignedCrew);
    void setBoardingGate(Gate *_boardingGate) ;
    void setPassengersRegistered(Passenger* _passenger);
    void setAirplane(Airplane *_airplane);

    
    void setAvailableSeats(int _avaliableSeats);

    //funcionalidades
    void embark();
    void print() const;
};

#endif
