#ifndef __AIRPORT_H
#define __AIRPORT_H

#include <iostream>
#include <string>
#include <vector>
#include "flight.h"
#include "gate.h"
#include "aircraft.h"
#include "helicopter.h"
#include "jet.h"
#include <map>

using namespace std;


class Airport {
    private:
        map<pair<string, string>, Flight*> flightsRegister;
        vector<Gate*> gatesRegister;
        vector<Airplane*> airplaneRegister;
        vector<Helicopter*> helicopterRegister;
        vector<PrivateJet*> privateJetRegister;
        vector<Worker*> airportCrew;
        vector<Passenger*> passengersRegistered;


    public:

        static Airport& getInstance() {
            static Airport instance; // Singleton
            return instance;
        }
        void addFlight(Flight* _flight);
        void addGate(Gate* _gate);
        void addAirplane(Airplane* _plane);
        void addHelicopter(Helicopter* _helicopter);
        void addJet(PrivateJet* _jet);
        void addWorker(Worker* _worker);
        void addPassenger(Passenger* _passenger);
        void createAirplane();
        void createFlight();
        void createGate();
        void createPassenger();
        void createWorker();
        void createPrivateJet();
        void createHelicopter();
        void buyFlight(string, string, Passenger*);
        void assignFlight(Flight *vuelo);
        Passenger* getPassenger(int n);
        int getPassengersRegisterSize();
        /*
        void printHelicopters ();
        void printPrivateJets ();
        void printFlights ();
        void printPassengers ();
        void printGates ();
        */

        
    

    };

#endif
