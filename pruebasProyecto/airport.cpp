#include "airport.h"

using namespace std;

// Obtener la instancia única del aeropuerto

/*
Airport& Airport::getInstance() {
    return instance;
}
*/

//Airport Airport::instance;
void Airport::addAirplane(Airplane* _plane){
    airplaneRegister.push_back(_plane);
}
void Airport::addFlight(Flight* _flight){
    string dest1 = _flight->getDestination();
    string date1 = _flight->getDate();
    pair<string,string> pareja(dest1, date1);
    flightsRegister[pareja] = _flight;
}
void Airport::addGate(Gate* _gate){
    gatesRegister.push_back(_gate);
}
void Airport::addHelicopter(Helicopter* _helicopter){
    helicopterRegister.push_back(_helicopter);
}
void Airport::addJet(PrivateJet* _jet){
    privateJetRegister.push_back(_jet);
}
void Airport::addWorker(Worker* _worker){
    airportCrew.push_back(_worker);
}
void Airport::addPassenger(Passenger* _passenger){
    passengersRegistered.push_back(_passenger);
}

void Airport::assignFlight(Flight *vuelo){
  int i = 0;
  bool flag = true;
  while(flag && i < airplaneRegister.size()){
      if(airplaneRegister[i]->getAssignedFlights()< 3){
          airplaneRegister[i]->addFlight(vuelo);
          vuelo->setAirplane((airplaneRegister[i]));
          flag = false;
          cout << "El vuelo ha sido asignado al avion identificado con el codigo " << airplaneRegister[i]->getId() << endl;
      }
      i += 1;
  }

  if(flag){
    cout << "No hay aviones disponibles, pero eso no es problema Cristiano Ronaldo te patrocina un nuevo avion" << endl << "Crea tu avion..." << endl; 
    Airport::getInstance().createAirplane();

  }
}
void Airport:: buyFlight(string destination, string date,Passenger* _passenger){
    pair<string, string> infoRequiered(destination, date);
    map<pair<string, string>, Flight*>::iterator it = flightsRegister.find(infoRequiered);
    if(it != flightsRegister.end()){
        Flight* vuelo = flightsRegister[infoRequiered];
        int seats = vuelo->getAvailableSeats();
        if(seats <= 0)
            cout << "El vuelo para el destino y fecha seleccionada, no se encuentra disponible" << endl;
        else{
            cout << "Su reserva ha sido exitosa" << endl;
            vuelo->setAvailableSeats(seats - 1);
            vuelo->setPassengersRegistered(_passenger);
        }
    }
    else
        cout << "El vuelo no existe para ese destino o fecha" << endl;
}

void Airport::createAirplane(){
    Airplane* airplane = new Airplane;

    string temp;

    cout << "Digite la marca: ";
    cin >> temp;
    airplane->setBrand(temp);
    cout << endl;

    cout << "Digite el modelo: ";
    cin >> temp;
    airplane->setModel(temp);
    cout << endl;

    cout << "Digite el ID: ";
    cin >> temp;
    airplane->setId(temp);
    cout << endl;

    cout << "Digite la capacidad: ";
    int capacity;
    cin >> capacity;
    airplane->setCapacity(capacity);
    cout << endl;

    cout << "Digite la velocidad maxima: ";
    int maxSpeed;
    cin >> maxSpeed;
    airplane->setMaxSpeed(maxSpeed);
    cout << endl;

    cout << "Digite la autonomia (distancia maxima que la aeronave puede recorrer sin recargar combustible): ";
    int autonomy;
    cin >> autonomy;
    airplane->setAutonomy(autonomy);
    cout << endl;

    cout << "Digite el ano: ";
    int year;
    cin >> year;
    airplane->setYear(year);
    cout << endl;

    cout << "Digite la condicion: ";
    cin >> temp;
    airplane->setCondition(temp);
    cout << endl;

    cout << "Digite la ubicacion: ";
    cin >> temp;
    airplane->setUbication(temp);
    cout << endl;

    cout << "Digite la altitud maxima: ";
    int maxAltitude;
    cin >> maxAltitude;
    airplane->setMaxAltitude(maxAltitude);
    cout << endl;

    cout << "Digite la cantidad de motores: ";
    int engineAmount;
    cin >> engineAmount;
    airplane->setEngineAmount(engineAmount);
    cout << endl;

    cout << "Digite la categoria: ";
    cin >> temp;
    airplane->setCategory(temp);
    cout << endl;

    airplane->setAvailability(true);

    Airport::getInstance().addAirplane(airplane);
}

void Airport::createFlight(){
    Flight* flight = new Flight;

    string temp;

    cout << "Digite el ID del vuelo: ";
    int id;
    cin >> id;
    flight->setId(id);
    cout << endl;

    cout << "Digite la fecha del vuelo: ";
    cin >> temp;
    flight->setDate(temp);
    cout << endl;

    cout << "Digite el origen: ";
    cin >> temp;
    flight->setOrigin(temp);
    cout << endl;

    cout << "Digite el destino: ";
    cin >> temp;
    flight->setDestination(temp);
    cout << endl;

    Airport::getInstance().addFlight(flight);
    Airport::getInstance().assignFlight(flight);
}

void Airport::createGate() {
    Gate* gate = new Gate;

    string temp;

    cout << "Digite la ubicacion de la puerta: ";
    cin >> temp;
    gate->setLocation(temp);
    cout << endl;

    cout << "Digite la hora de abordaje: ";
    cin >> temp;
    gate->setBoardingHour(temp);
    cout << endl;

    Airport::getInstance().addGate(gate);
}

void Airport::createPassenger() {
    Passenger* passenger = new Passenger;

    string temp;

    cout << "Digite el ID del pasajero: ";
    int id;
    cin >> id;
    passenger->setId(id);
    cout << endl;

    cout << "Digite el nombre del pasajero: ";
    cin.ignore();  
    getline(cin, temp);
    passenger->setName(temp);
    cout << endl;

    cout << "Digite el apellido del pasajero: ";
    getline(cin, temp);
    passenger->setLastName(temp);
    cout << endl;

    cout << "Digite la fecha de nacimiento del pasajero (YYYY-MM-DD): ";
    cin >> temp;
    passenger->setBirthdate(temp);
    cout << endl;

    cout << "Digite el genero del pasajero: ";
    cin >> temp;
    passenger->setGender(temp);
    cout << endl;

    cout << "Digite la direccion del pasajero: ";
    cin.ignore(); 
    getline(cin, temp);
    passenger->setAddress(temp);
    cout << endl;

    cout << "Digite el numero de telefono del pasajero: ";
    int phoneNumber;
    cin >> phoneNumber;
    passenger->setPhoneNumber(phoneNumber);
    cout << endl;

    cout << "Digite el correo electronico del pasajero: ";
    cin >> temp;
    passenger->setEmail(temp);
    cout << endl;

    cout << "Digite la nacionalidad del pasajero: ";
    cin >> temp;
    passenger->setNationality(temp);
    cout << endl;

    cout << "Digite la cantidad de equipaje del pasajero: ";
    int baggageAmount;
    cin >> baggageAmount;
    passenger->setBaggageAmount(baggageAmount);
    cout << endl;

    cout << "Digite informacion medica del pasajero: ";
    cin.ignore();  
    getline(cin, temp);
    passenger->setMedicalInformation(temp);
    cout << endl;

    Airport::getInstance().addPassenger(passenger);
}

void Airport::createWorker() {
    Worker* worker = new Worker;

    string temp;

    cout << "Digite el ID del trabajador: ";
    int id;
    cin >> id;
    worker->setId(id);
    cout << endl;

    cout << "Digite el nombre del trabajador: ";
    cin.ignore(); 
    getline(cin, temp);
    worker->setName(temp);
    cout << endl;

    cout << "Digite el apellido del trabajador: ";
    getline(cin, temp);
    worker->setLastName(temp);
    cout << endl;

    cout << "Digite la fecha de nacimiento del trabajador (YYYY-MM-DD): ";
    cin >> temp;
    worker->setBirthdate(temp);
    cout << endl;

    cout << "Digite el genero del trabajador: ";
    cin >> temp;
    worker->setGender(temp);
    cout << endl;

    cout << "Digite la direccion del trabajador: ";
    cin.ignore();  
    getline(cin, temp);
    worker->setAddress(temp);
    cout << endl;

    cout << "Digite el numero de telefono del trabajador: ";
    int phoneNumber;
    cin >> phoneNumber;
    worker->setPhoneNumber(phoneNumber);
    cout << endl;

    cout << "Digite el correo electronico del trabajador: ";
    cin >> temp;
    worker->setEmail(temp);
    cout << endl;

    cout << "Digite la posicion del trabajador: ";
    cin >> temp;
    worker->setPosition(temp);
    cout << endl;

    cout << "Digite los años de experiencia del trabajador: ";
    int yearsOfExperience;
    cin >> yearsOfExperience;
    worker->setYearsOfExperience(yearsOfExperience);
    cout << endl;

    cout << "Digite el maximo de horas diarias del trabajador: ";
    int maxDailyHours;
    cin >> maxDailyHours;
    worker->setMaxDailyHours(maxDailyHours);
    cout << endl;

    Airport::getInstance().addWorker(worker);
}

void Airport::createPrivateJet() {
    PrivateJet* privateJet = new PrivateJet;

    string temp;

    cout << "Digite la marca: ";
    cin >> temp;
    privateJet->setBrand(temp);
    cout << endl;

    cout << "Digite el modelo: ";
    cin >> temp;
    privateJet->setModel(temp);
    cout << endl;

    cout << "Digite el ID: ";
    cin >> temp;
    privateJet->setId(temp);
    cout << endl;

    cout << "Digite la capacidad: ";
    int capacity;
    cin >> capacity;
    privateJet->setCapacity(capacity);
    cout << endl;

    cout << "Digite la velocidad maxima: ";
    int maxSpeed;
    cin >> maxSpeed;
    privateJet->setMaxSpeed(maxSpeed);
    cout << endl;

    cout << "Digite la autonomia (distancia maxima que la aeronave puede recorrer sin recargar combustible): ";
    int autonomy;
    cin >> autonomy;
    privateJet->setAutonomy(autonomy);
    cout << endl;

    cout << "Digite el ano: ";
    int year;
    cin >> year;
    privateJet->setYear(year);
    cout << endl;

    cout << "Digite la condicion: ";
    cin >> temp;
    privateJet->setCondition(temp);
    cout << endl;

    cout << "Digite la ubicacion: ";
    cin >> temp;
    privateJet->setUbication(temp);
    cout << endl;


    privateJet->setAvailability(true);

    Airport::getInstance().addJet(privateJet);
}


void Airport::createHelicopter() {
    Helicopter* helicopter = new Helicopter;

    string temp;

    cout << "Digite la marca: ";
    cin >> temp;
    helicopter->setBrand(temp);
    cout << endl;

    cout << "Digite el modelo: ";
    cin >> temp;
    helicopter->setModel(temp);
    cout << endl;

    cout << "Digite el ID: ";
    cin >> temp;
    helicopter->setId(temp);
    cout << endl;

    cout << "Digite la capacidad: ";
    int capacity;
    cin >> capacity;
    helicopter->setCapacity(capacity);
    cout << endl;

    cout << "Digite la velocidad máxima: ";
    int maxSpeed;
    cin >> maxSpeed;
    helicopter->setMaxSpeed(maxSpeed);
    cout << endl;

    cout << "Digite la autonomía: ";
    int autonomy;
    cin >> autonomy;
    helicopter->setAutonomy(autonomy);
    cout << endl;

    cout << "Digite el año: ";
    int year;
    cin >> year;
    helicopter->setYear(year);
    cout << endl;

    cout << "Digite la condición: ";
    cin >> temp;
    helicopter->setCondition(temp);
    cout << endl;

    cout << "Digite la ubicación: ";
    cin >> temp;
    helicopter->setUbication(temp);
    cout << endl;

    cout << "Digite la cantidad de motores: ";
    int engineAmount;
    cin >> engineAmount;
    helicopter->setEngineAmount(engineAmount);
    cout << endl;

    cout << "Digite la capacidad de elevación: ";
    int elevationCapacity;
    cin >> elevationCapacity;
    helicopter->setElevationCapacity(elevationCapacity);
    cout << endl;


    cout << "Digite el uso del helicóptero: ";
    cin >> temp;
    helicopter->setUse(temp);
    cout << endl;

    helicopter->setAvailability(true);
    

    Airport::getInstance().addHelicopter(helicopter);
}

Passenger* Airport::getPassenger(int n){
    return passengersRegistered[n];
}

int Airport::getPassengersRegisterSize(){
    return passengersRegistered.size();
}

void Airport::printAirplanes() const {
    cout << "Airplanes Registered:" << endl;
    for (int i = 0; i < airplaneRegister.size(); ++i) {
        cout << "Airplane " << i + 1 << ":" << endl;
        airplaneRegister[i]->print();
    }
}

void Airport::printHelicopters() const {
    cout << "Helicopters Registered:" << endl;
    for (int i = 0; i < helicopterRegister.size(); ++i) {
        cout << "Helicopter " << i + 1 << ":" << endl;
        helicopterRegister[i]->print();
    }
}

void Airport::printPrivateJets() const {
    cout << "Private Jets Registered:" << endl;
    for (int i = 0; i < privateJetRegister.size(); ++i) {
        cout << "Private Jet " << i + 1 << ":" << endl;
        privateJetRegister[i]->print();
    }
}






