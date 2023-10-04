#include "aircraft.h"

using namespace std;

// Constructor
Aircraft::Aircraft(const string& _brand, const string& _model, int _capacity, int _maxSpeed,
    int _autonomy, int _year, const string& _condition, const string& _ubication,
    bool _availability)
    : brand(_brand), model(_model), capacity(_capacity), maxSpeed(_maxSpeed),
    autonomy(_autonomy), year(_year), condition(_condition), ubication(_ubication),
    availability(_availability) {
    }

// Métodos get
string Aircraft::getBrand()  { return brand; }
string Aircraft::getModel()  { return model; }
int Aircraft::getCapacity()  { return capacity; }
int Aircraft::getMaxSpeed()  { return maxSpeed; }
int Aircraft::getAutonomy()  { return autonomy; }
int Aircraft::getYear()  { return year; }
string Aircraft::getCondition()  { return condition; }
vector<Flight> Aircraft::getAssignedFlights()  { return assignedFlights; }
string Aircraft::getUbication()  { return ubication; }
bool Aircraft::isAvailable()  { return availability; }

// Métodos set
void Aircraft::setBrand(const string& _brand) { brand = _brand; }
void Aircraft::setModel(const string& _model) { model = _model; }
void Aircraft::setCapacity(int _capacity) { capacity = _capacity; }
void Aircraft::setMaxSpeed(int _maxSpeed) { maxSpeed = _maxSpeed; }
void Aircraft::setAutonomy(int _autonomy) { autonomy = _autonomy; }
void Aircraft::setYear(int _year) { year = _year; }
void Aircraft::setCondition(const string& _condition) { condition = _condition; }
void Aircraft::setAssignedFlights(const vector<Flight>& _assignedFlights) { assignedFlights = _assignedFlights; }
void Aircraft::setUbication(const string& _ubication) { ubication = _ubication; }
void Aircraft::setAvailability(bool _availability) { availability = _availability; }