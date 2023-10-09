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
        Helicopter(string brand, string model, string id, int capacity, int maxSpeed,
                   int autonomy, int year, string condition, string ubication,
                   bool availability, int engineAmount, int elevationCapacity, string use);
        Helicopter();   

        // Getters y setters para los atributos específicos de Helicopter
        int getEngineAmount();
        int getElevationCapacity();
        string getUse();

        void setEngineAmount(int newEngineAmount);
        void setElevationCapacity(int newElevationCapacity);
        void setUse(string newUse);
    };

    

#endif
