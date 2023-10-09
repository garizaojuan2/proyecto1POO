#include "flight.h"

using namespace std;

Flight::Flight(int _id, const string& _date, const string& _origin, const string& _destination,
           const vector<Worker>& _assignedCrew,  Gate *_boardingGate,
           const map<int, Passenger>& _passengersRegistered)
        : id(_id), date(_date), origin(_origin), destination(_destination),
          assignedCrew(_assignedCrew), boardingGate(_boardingGate),
          passengersRegistered(_passengersRegistered) {
    }

    // Métodos get
    int Flight::getId()  { return id; }
    string Flight::getDate()  { return date; }
    string Flight::getOrigin()  { return origin; }
    string Flight::getDestination()  { return destination; }
    vector<Worker> Flight::getAssignedCrew()  { return assignedCrew; }
    Gate* Flight::getBoardingGate()  { return boardingGate; }
    map<int, Passenger> Flight::getPassengersRegistered()  { return passengersRegistered; }

    // Métodos set
    void Flight::setId(int _id) { id = _id; }
    void Flight::setDate(const string& _date) { date = _date; }
    void Flight::setOrigin(const string& _origin) { origin = _origin; }
    void Flight::setDestination(const string& _destination) { destination = _destination; }
    void Flight::setAssignedCrew(const vector<Worker>& _assignedCrew) { assignedCrew = _assignedCrew; }
    void Flight::setBoardingGate(Gate *_boardingGate) { boardingGate = _boardingGate; }
    void Flight::setPassengersRegistered(const map<int, Passenger>& _passengersRegistered) {
        passengersRegistered = _passengersRegistered;
    }