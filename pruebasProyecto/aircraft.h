#ifndef __AIRCRAFT_H
#define __AIRCRAFT_H

#include <iostream>
#include <string>
//#include "flight.h"
#include <vector>
//#include "controlTower.h"



using namespace std;

class ControlTower;
class Flight;

class Aircraft {
private:
    string brand;
    string model;
    string id;
    int capacity;
    int maxSpeed;
    int autonomy;
    int year;
    string condition;
    vector<Flight*> assignedFlights;
    string ubication;
    bool availability;
    Flight* flightAssociated;

public:
    // Constructor
    Aircraft(const string& _brand, const string& _model, const string& _id,  int _capacity, int _maxSpeed,
             int _autonomy, int _year, const string& _condition, const string& _ubication,
             bool _availability);
    Aircraft();

    // Métodos get
    string getBrand();
    string getModel();
    string getId();
    int getCapacity();
    int getMaxSpeed();
    int getAutonomy();
    int getYear();
    string getCondition();
    string getUbication();
    bool isAvailable();
    Flight* getFlightAsociated();
    int getAssignedFlights();



    // Métodos set
    void setBrand(const string& _brand);
    void setModel(const string& _model);
    void setId(const string & _id);
    void setCapacity(int _capacity);
    void setMaxSpeed(int _maxSpeed);
    void setAutonomy(int _autonomy);
    void setYear(int _year);
    void setCondition(const string& _condition);
    void setUbication(const string& _ubication);
    void setAvailability(bool _availability);
    void setFlightAsociated(Flight *_flightAssociated);

    // Funcionalidades
    virtual void print() const;
    void takeOff();
    void landed();
    void reportLocation(const string& location);
    void recibeInfo(const string& msg);
    void addFlight(Flight *flight);
};
#endif
