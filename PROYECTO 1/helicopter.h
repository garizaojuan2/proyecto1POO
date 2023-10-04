#ifndef __HELICOPTER_H
#define __HELICOPTER_H

#include <string>
#include <iostream>
#include "aircraft.h"


class Helicopter : public Aircraft {
    private:
        int engineAmount;
        int elevationCapacity;
        string use;

    public:
        // Constructor
        Helicopter(string brand, string model, int capacity, int maxSpeed,
                   int autonomy, int year, string condition, string ubication,
                   bool availability, int engineAmount, int elevationCapacity, string use)
            : Aircraft(brand, model, capacity, maxSpeed, autonomy, year, condition,
                       ubication, availability), engineAmount(engineAmount),
              elevationCapacity(elevationCapacity), use(use) {}

        // Getters y setters para los atributos específicos de Helicopter
        int getEngineAmount() const { return engineAmount; }
        int getElevationCapacity() const { return elevationCapacity; }
        string getUse() const { return use; }

        void setEngineAmount(int newEngineAmount) { engineAmount = newEngineAmount; }
        void setElevationCapacity(int newElevationCapacity) { elevationCapacity = newElevationCapacity; }
        void setUse(string newUse) { use = newUse; }
    };

#endif
