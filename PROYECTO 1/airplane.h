#ifndef __AIRPLANE_H
#define __AIRPLANE_H

#include <string>
#include <iostream>
#include "aircraft.h"

using namespace std;

    class Airplane : public Aircraft {
    private:
        int maxAltitude;
        int engineAmount;
        string category;

    public:
        // Constructor
        Airplane(string brand, string model, int capacity, int maxSpeed,
                 int autonomy, int year, string condition, string ubication,
                 bool availability, int maxAltitude, int engineAmount, string category)
            : Aircraft(brand, model, capacity, maxSpeed, autonomy, year, condition,
                       ubication, availability), maxAltitude(maxAltitude),
              engineAmount(engineAmount), category(category) {}

        // Getters y setters para los atributos específicos de Airplane
        int getMaxAltitude() const { return maxAltitude; }
        int getEngineAmount() const { return engineAmount; }
        string getCategory() const { return category; }

        void setMaxAltitude(int newMaxAltitude) { maxAltitude = newMaxAltitude; }
        void setEngineAmount(int newEngineAmount) { engineAmount = newEngineAmount; }
        void setCategory(string newCategory) { category = newCategory; }
    };


#endif
