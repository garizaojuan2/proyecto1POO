#include "airplane.h"

using namespace std;

// Constructor
Airplane::Airplane(string brand, string model, int capacity, int maxSpeed,
    int autonomy, int year, string condition, string ubication,
    bool availability, int maxAltitude, int engineAmount, string category)
    : Aircraft(brand, model, capacity, maxSpeed, autonomy, year, condition,
    ubication, availability), maxAltitude(maxAltitude),
    engineAmount(engineAmount), category(category) {}

// Getters y setters para los atributos específicos de Airplane
int Airplane::getMaxAltitude()  { return maxAltitude; }
int Airplane::getEngineAmount()  { return engineAmount; }
string Airplane::getCategory()  { return category; }

void Airplane::setMaxAltitude(int newMaxAltitude) { maxAltitude = newMaxAltitude; }
void Airplane::setEngineAmount(int newEngineAmount) { engineAmount = newEngineAmount; }
void Airplane::setCategory(string newCategory) { category = newCategory; }