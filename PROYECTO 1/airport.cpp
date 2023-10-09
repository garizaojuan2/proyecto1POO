#include "airport.h"

using namespace std;

// Obtener la instancia única del aeropuerto
Airport& Airport::getInstance() {
    return instance;
}

void Airport:: buyFlight(string destination, string date){
    pair<string, string> infoRequiered(destination, date);
    
}
