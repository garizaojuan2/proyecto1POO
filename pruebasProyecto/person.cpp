#include "person.h"

using namespace std;

Person::Person(int _id, const string& _name, const string& _lastName,
    const string& _birthdate, const string& _gender,
    const string& _address, int _phoneNumber, const string& _email) 
    : id(_id), name(_name), lastName(_lastName), birthdate(_birthdate),
    gender(_gender), address(_address), phoneNumber(_phoneNumber), email(_email) {
}
Person::Person(){}

// Métodos get privados
int Person::getId(){ return id; }
string Person::getName(){ return name; }
string Person::getLastName(){ return lastName; }
string Person::getBirthdate()  { return birthdate; }
string Person::getGender(){ return gender; }
string Person::getAddress(){ return address; }
int Person::getPhoneNumber(){ return phoneNumber; }
string Person::getEmail(){ return email; }    

// Métodos set privados
void Person::setId(int _id) { id = _id; }
void Person::setName(const string& _name) { name = _name; }
void Person::setLastName(const string& _lastName) { lastName = _lastName; }
void Person::setBirthdate(const string& _birthdate) { birthdate = _birthdate; }
void Person::setGender(const string& _gender) { gender = _gender; }
void Person::setAddress(const string& _address) { address = _address; }
void Person::setPhoneNumber(int _phoneNumber) { phoneNumber = _phoneNumber; }
void Person::setEmail(const string& _email) { email = _email; }
