#ifndef __WORKER_H
#define __WORKER_H

#include <iostream> 
#include <string>
#include "person.h"

class Worker : public Person {
private:
    string position;
    int yearsOfExperience;
    int maxDailyHours;

public:
    // Constructor de la clase Worker
    Worker(int _id, const string& _name, const string& _lastName,
           const string& _birthdate, const string& _gender,
           const string& _address, int _phoneNumber, const string& _email,
           const string& _position, int _yearsOfExperience, int _maxDailyHours);

    // Métodos get de Worker
    string getPosition();
    int getYearsOfExperience();
    int getMaxDailyHours();

    // Métodos set de Worker
    void setPosition(const string& _position);
    void setYearsOfExperience(int _yearsOfExperience);
    void setMaxDailyHours(int _maxDailyHours);
};

#endif