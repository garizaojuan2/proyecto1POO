#include "airplane.h"

using namespace std;

// Constructor
Airplane::Airplane(string brand, string model, string id, int capacity, int maxSpeed,
    int autonomy, int year, string condition, string ubication,
    bool availability, int maxAltitude, int engineAmount, string category)
    :Aircraft(brand, model, id, capacity, maxSpeed, autonomy, year, condition,
    ubication, availability), maxAltitude(maxAltitude),
    engineAmount(engineAmount), category(category) {}
Airplane::Airplane(){}
// Getters y setters para los atributos específicos de Airplane
int Airplane::getMaxAltitude()  { return maxAltitude; }
int Airplane::getEngineAmount()  { return engineAmount; }
string Airplane::getCategory()  { return category; }

void Airplane::setMaxAltitude(int newMaxAltitude) { maxAltitude = newMaxAltitude; }
void Airplane::setEngineAmount(int newEngineAmount) { engineAmount = newEngineAmount; }
void Airplane::setCategory(string newCategory) { category = newCategory; }

void Airplane::print() const {
    cout << "Airplane Information:" << endl;
    Aircraft::print();
    cout << "Max Altitude: " << maxAltitude << " meters" << endl;
    cout << "Engine Amount: " << engineAmount << endl;
    cout << "Category: " << category << endl;
}
