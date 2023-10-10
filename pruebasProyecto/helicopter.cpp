#include "helicopter.h"
using namespace std;

// Constructor de la clase Helicopter
Helicopter::Helicopter(string brand, string model, string id, int capacity, int maxSpeed,
    int autonomy, int year, string condition, string ubication,
    bool availability, int engineAmount, int elevationCapacity, string use)
    : Aircraft(brand, model, id, capacity,  maxSpeed, autonomy, year, condition,
     ubication, availability), engineAmount(engineAmount),
    elevationCapacity(elevationCapacity), use(use) {
}

// Constructor vacío de la clase Helicopter
Helicopter::Helicopter(){}

// Getters para obtener los valores de los atributos específicos de Helicopter
int Helicopter::getEngineAmount() { return engineAmount; }
int Helicopter::getElevationCapacity()  { return elevationCapacity; }
string Helicopter::getUse() { return use; }

// Setters para modificar los valores de los atributos específicos de Helicopter
void Helicopter::setEngineAmount(int newEngineAmount) { engineAmount = newEngineAmount; }
void Helicopter::setElevationCapacity(int newElevationCapacity) { elevationCapacity = newElevationCapacity; }
void Helicopter::setUse(string newUse) { use = newUse; }