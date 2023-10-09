#ifndef __AIRPORT_H
#define __AIRPORT_H

#include <iostream>
#include <string>
#include <vector>
#include "flight.h"
#include "gate.h"
#include "aircraft.h"

using namespace std;


class Airport {
    private:
        map<pair<string, string>, Flight> flightsRegister;
        vector<Gate> gatesRegister;
        vector<Airplane> airplaneRegister;
        vector<Helicopter> helicopterRegister;
        vector<PrivateJet> privateJetRegister;
        static Airport instance;
        Airport() {}  // Constructor privado para garantizar una única instancia

    public:
        // Obtener la instancia única del aeropuerto
        Airport getInstance();
        void createFlight();
        void createGate();
        void createPassanger();
        void createWorker();
        void createPrivateJet();
        void createHelicopter();
        void buyFlight(string, string);
        void assignFlight();
    };

#endif
