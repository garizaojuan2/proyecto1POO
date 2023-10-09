#ifndef PRIVATEJET_H
#define PRIVATEJET_H

#include "aircraft.h" 
#include "person.h"  
#include <vector>
#include <string>

using namespace std;

class PrivateJet : public Aircraft {
private:
    Person *owner;
    vector<string> services;
    vector<string> destinations;

public:
    // Constructor
    PrivateJet(const string& _brand, const string& _model, const string& _id,  int _capacity, int _maxSpeed,
             int _autonomy, int _year, const string& _condition, const string& _ubication,
             bool _availability,  Person *_owner);

    // Métodos set
    void setOwner( Person *_owner);
    void addService(const string& service);
    void addDestination(const string& destination);

    // Métodos get
    Person* getOwner();
    vector<string> getServices();
    vector<string> getDestinations();
};

#endif
