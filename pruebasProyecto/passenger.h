#ifndef __PASSENGER_H
#define __PASSENGER_H

#include <iostream>
#include <string>
#include "person.h"

using namespace std;

class Passenger : public Person {
private:
    string nationality;
    int baggageAmount;
    string medicalInformation;

public:
    // Constructor de la clase Passenger que llama al constructor de Person
    Passenger(int _id, const string& _name, const string& _lastName,
               const string& _birthdate, const string& _gender,
               const string& _address, int _phoneNumber, const string& _email,
               const string& _nationality, int _baggageAmount, const string& _medicalInformation);
    
    Passenger();
    // Métodos get de Passenger
    string getNationality();
    int getBaggageAmount();
    string getMedicalInformation();

    // Métodos set de Passenger
    void setNationality(const string& _nationality);
    void setBaggageAmount(int _baggageAmount);
    void setMedicalInformation(const string& _medicalInformation);

    void print() const override;
};

#endif
