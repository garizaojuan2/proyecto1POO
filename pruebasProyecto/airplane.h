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
        Airplane(string brand, string model,string id, int capacity, int maxSpeed,
                 int autonomy, int year, string condition, string ubication,
                 bool availability, int maxAltitude, int engineAmount, string category);
        Airplane();

        // Getters y setters para los atributos específicos de Airplane
        int getMaxAltitude();
        int getEngineAmount() ;
        string getCategory();

        void setMaxAltitude(int newMaxAltitude);
        void setEngineAmount(int newEngineAmount);
        void setCategory(string newCategory);
    };


#endif
