#ifndef __CONTROLTOWER_H
#define __CONTROLTOWER_H

#include <iostream>
#include <string>
#include <vector>
#include "aircraft.h"

using namespace std;

class Aircraft;

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

private:
    void notify(Aircraft* aircraft, const string& message);

    vector<Aircraft*> aircrafts;
};


#endif
