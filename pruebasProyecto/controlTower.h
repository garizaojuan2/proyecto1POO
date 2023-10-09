#ifndef __CONTROLTOWER_H
#define __CONTROLTOWER_H

#include <iostream>
#include <string>
#include <vector>
//#include "aircraft.h"
#include "gate.h"
//#include "flight.h"
using namespace std;

class Aircraft;
class Flight;


class ControlTower {
public:
    static ControlTower& getInstance() {
        static ControlTower instance; // Singleton
        return instance;
    }

    void addAircraft(Aircraft* aircraft);

    void aircraftTakeOff (Aircraft* aircraft);
    void aircraftLanded(Aircraft* aircraft);
    void aircrafInFlight(Aircraft* aircraft, const string& location);

    void assignBoardingGate(Flight *flihgt);

private:
    void notify(Aircraft* aircraft, const string& message);

    vector<Aircraft*> aircrafts;
    vector<Gate*> gates;

};


#endif
