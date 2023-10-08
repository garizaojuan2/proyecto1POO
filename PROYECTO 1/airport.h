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
        vector<Flight> flightsRegister;
        vector<Gate> gatesRegister;
        vector<Airplane> airplaneRegister;
        vector<Helicopter> helicopterRegister;
        vector<PrivateJet> privateJetRegister;
        static Airport instance;

        Airport() {}  // Constructor privado para garantizar una única instancia

    public:
        // Obtener la instancia única del aeropuerto
        static Airport& getInstance();
        void createAircraft();
        void createAirplane();
        void createHelicopter();
        void createPrivateJet();
        void createGate();
    };

#endif
