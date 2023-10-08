#include "Aircraft.h"

// Implementación del constructor
PrivateJet::PrivateJet(const string& _brand, const string& _model, const string& _id, int _capacity, int _maxSpeed,
                       int _autonomy, int _year, const string& _condition, const string& _ubication,
                       bool _availability, const Persona& _owner)
    : Aircraft(_brand, _model, _id, _capacity, _maxSpeed, _autonomy, _year, _condition, _ubication, _availability) {
    owner = _owner;
}

// Implementación de métodos set
void PrivateJet::setOwner(const Persona& _owner) {
    owner = _owner;
}

void PrivateJet::addService(const string& service) {
    services.push_back(service);
}

void PrivateJet::addDestination(const string& destination) {
    destinations.push_back(destination);
}

// Implementación de métodos get
Persona PrivateJet::getOwner() {
    return owner;
}

vector<string> PrivateJet::getServices() {
    return services;
}

vector<string> PrivateJet::getDestinations() {
    return destinations;
}
