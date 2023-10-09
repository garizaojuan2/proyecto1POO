#include "airport.h"
#include "controlTower.h"
#include "aircraft.h"
#include "airplane.h"
#include "helicopter.h"
#include "gate.h"
#include "flight.h"
#include <iostream>
int main(){

    Airport::getInstance(); //Aeropuerto Alfonso Bonilla

    Aircraft air01;
    Aircraft air02;
    Aircraft air03;
    Aircraft air04;

    Helicopter h01;
    Helicopter h02;

    Airplane plane01;
    Airplane plane02;
    
    
    air01.setId("craft1");
    air02.setId("craft2");
    air03.setId("craft3");

    h01.setId("h1");
    h02.setId("h2");

    plane01.setId("plane1");
    plane02.setId("plane2");

    ControlTower::getInstance().addAircraft(&air01);
    ControlTower::getInstance().addAircraft(&air02);
    ControlTower::getInstance().addAircraft(&air03);

    ControlTower::getInstance().addAircraft(&h01);
    ControlTower::getInstance().addAircraft(&h02);

    ControlTower::getInstance().addAircraft(&plane01);
    ControlTower::getInstance().addAircraft(&plane02);

    air01.takeOff();
    cout << "#############################" << endl;

    air01.reportLocation("Panama");
    
    return 0;

}