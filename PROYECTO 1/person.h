#ifndef __PERSON_H
#define __PERSON_H

#include <iostream>
#include <string>

using namespace std;


class Person {
private:
    int id;
    string name;
    string lastName;
    string birthdate;
    string gender;
    string address;
    int phoneNumber;
    string email;

public:
    // Constructor
    Person(int _id, const string& _name, const string& _lastName,
           const string& _birthdate, const string& _gender,
           const string& _address, int _phoneNumber, const string& _email);
    person();

    // Métodos get privados
    int getId();
    string getName();
    string getLastName();
    string getBirthdate();
    string getGender();
    string getAddress();
    int getPhoneNumber();
    string getEmail();

    // Métodos set privados
    void setId(int _id);
    void setName(const string& _name);
    void setLastName(const string& _lastName);
    void setBirthdate(const string& _birthdate);
    void setGender(const string& _gender);
    void setAddress(const string& _address);
    void setPhoneNumber(int _phoneNumber);
    void setEmail(const string& _email);

};

#endif