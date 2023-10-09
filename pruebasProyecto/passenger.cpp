#include "passenger.h"

using namespace std;

// Constructor de la clase Passenger que llama al constructor de Person
Passenger::Passenger(int _id, const string& _name, const string& _lastName,
    const string& _birthdate, const string& _gender,
    const string& _address, int _phoneNumber, const string& _email,
    const string& _nationality, int _baggageAmount, const string& _medicalInformation)
    : Person(_id, _name, _lastName, _birthdate, _gender, _address, _phoneNumber, _email),
   nationality(_nationality), baggageAmount(_baggageAmount), medicalInformation(_medicalInformation) {
}
Passenger::Passenger(){}
// Métodos get de Passenger
string Passenger::getNationality()  { return nationality; }
int Passenger::getBaggageAmount()  { return baggageAmount; }
string Passenger::getMedicalInformation()  { return medicalInformation; }

// Métodos set de Passenger
void Passenger::setNationality(const string& _nationality) { nationality = _nationality; }
void Passenger::setBaggageAmount(int _baggageAmount) { baggageAmount = _baggageAmount; }
void Passenger::setMedicalInformation(const string& _medicalInformation) { medicalInformation = _medicalInformation; }