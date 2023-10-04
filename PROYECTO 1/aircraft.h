#ifndef __AIRCRAFT_H
#define __AIRCRAFT_H

#include <iostream>
#include <string>
#include "flight.h"
#include <vector>

using namespace std;

class Aircraft {
private:
    string brand;
    string model;
    int capacity;
    int maxSpeed;
    int autonomy;
    int year;
    string condition;
    vector<Flight> assignedFlights;
    string ubication;
    bool availability;

public:
    // Constructor
    Aircraft(const string& _brand, const string& _model, int _capacity, int _maxSpeed,
             int _autonomy, int _year, const string& _condition, const string& _ubication,
             bool _availability);

    // Métodos get
    string getBrand();
    string getModel();
    int getCapacity();
    int getMaxSpeed();
    int getAutonomy();
    int getYear();
    string getCondition();
    vector<Flight> getAssignedFlights();
    string getUbication();
    bool isAvailable();

    // Métodos set
    void setBrand(const string& _brand);
    void setModel(const string& _model);
    void setCapacity(int _capacity);
    void setMaxSpeed(int _maxSpeed);
    void setAutonomy(int _autonomy);
    void setYear(int _year);
    void setCondition(const string& _condition);
    void setAssignedFlights(const vector<Flight>& _assignedFlights);
    void setUbication(const string& _ubication);
    void setAvailability(bool _availability);
};
#endif