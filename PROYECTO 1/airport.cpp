#include "airport.h"

using namespace std;

// Obtener la instancia única del aeropuerto
Airport& Airport::getInstance() {
    return instance;
}