#include "flight.h"
#include "controlTower.h"
#include "airport.h"
using namespace std;

// Constructor de Flight
Flight::Flight(int _id, const string& _date, const string& _origin, const string& _destination,
           const vector<Worker*>& _assignedCrew,
           const map<int, Passenger*>& _passengersRegistered)
        : id(_id), date(_date), origin(_origin), destination(_destination),
          assignedCrew(_assignedCrew),
          passengersRegistered(_passengersRegistered){
    }

// Constructor vacío de Flight
Flight::Flight(){}

// Métodos get para obtener los valores de los atributos
int Flight::getId()  { return id; }
string Flight::getDate()  { return date; }
string Flight::getOrigin()  { return origin; }
string Flight::getDestination()  { return destination; }
vector<Worker*> Flight::getAssignedCrew()  { return assignedCrew; }
Gate* Flight::getBoardingGate()  { return boardingGate; }
map<int, Passenger*> Flight::getPassengersRegistered()  { return passengersRegistered; }
Airplane* Flight::getAirplane(){return airplane;}
int Flight::getAvailableSeats(){return availableSeats;}

// Métodos set para modificar los valores de los atributos
void Flight::setId(int _id) { id = _id; }
void Flight::setDate(const string& _date) { date = _date; }
void Flight::setOrigin(const string& _origin) { origin = _origin; }
void Flight::setDestination(const string& _destination) { destination = _destination; }
void Flight::setAssignedCrew(const vector<Worker*>& _assignedCrew) { assignedCrew = _assignedCrew; }
void Flight::setBoardingGate(Gate *_boardingGate) { boardingGate = _boardingGate; }
void Flight::setPassengersRegistered(Passenger* _passenger) {
    int id = _passenger->getId();
    passengersRegistered[id] = _passenger;
}

// Funcionalidad para embarcar
void Flight::embark(){
    ControlTower::getInstance().assignBoardingGate(this);
}

// Establecer el avión para el vuelo
void Flight::setAirplane(Airplane *_airplane) {
    airplane = _airplane;
    availableSeats = (*_airplane).getCapacity();
}

// Establecer el número de asientos disponibles
void Flight::setAvailableSeats(int num) {availableSeats = num;}