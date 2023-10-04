#include "worker.h"

using namespace std;

// Constructor de la clase Worker
Worker::Worker(int _id, const string& _name, const string& _lastName,
    const string& _birthdate, const string& _gender,
    const string& _address, int _phoneNumber, const string& _email,
    const string& _position, int _yearsOfExperience, int _maxDailyHours)
    : Person(_id, _name, _lastName, _birthdate, _gender, _address, _phoneNumber, _email),
    position(_position), yearsOfExperience(_yearsOfExperience), maxDailyHours(_maxDailyHours) {
}

// Métodos get de Worker
string Worker::getPosition()  { return position; }
int Worker::getYearsOfExperience()  { return yearsOfExperience; }
int Worker::getMaxDailyHours()  { return maxDailyHours; }

// Métodos set de Worker
void Worker::setPosition(const string& _position) { position = _position; }
void Worker::setYearsOfExperience(int _yearsOfExperience) { yearsOfExperience = _yearsOfExperience; }
void Worker::setMaxDailyHours(int _maxDailyHours) { maxDailyHours = _maxDailyHours; }