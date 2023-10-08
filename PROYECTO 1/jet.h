#ifndef PRIVATEJET_H
#define PRIVATEJET_H

#include "Aircraft.h" // Asegúrate de incluir el archivo que contiene la definición de la clase Aircraft
#include "Persona.h"  // Asegúrate de incluir el archivo que contiene la definición de la clase Persona
#include <vector>
#include <string>

using namespace std;

class PrivateJet : public Aircraft {
private:
    Persona owner;
    vector<string> services;
    vector<string> destinations;

public:
    // Constructor
    PrivateJet(const string& _brand, const string& _model, const string& _id, int _capacity, int _maxSpeed,
               int _autonomy, int _year, const string& _condition, const string& _ubication,
               bool _availability, const Persona& _owner);

    // Métodos set
    void setOwner(const Persona& _owner);
    void addService(const string& service);
    void addDestination(const string& destination);

    // Métodos get
    Persona getOwner();
    vector<string> getServices();
    vector<string> getDestinations();
};

#endif
