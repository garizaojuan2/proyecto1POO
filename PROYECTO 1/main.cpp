#include <iostream>
#include "aircraft.h"
#include "ControlTower.h"
#include "person.h"
#include "worker.h"

using namespace std;

void menu();
void crearObjetos();

void crearObjetos(){

    cout << "**** Crear objetos ****" << endl;
    cout << "1. Trabajador" << endl;
    cout << "2. Avion" << endl;
    cout << "3. Helicoptero" << endl;
    cout << "4. Jet privado" << endl;
    cout << "5. Pasajeros" << endl;
    cout << "6. Puerta de embarque" << endl;
    cout << "****************************" << endl;
    int op;
    cout << "Elija una opcion >";
    cin >> op;
    cout << endl;

    switch (op)
    {
    case 1:
        int id;
        string name;
        string lastName;
        string birthdate;
        string gender;
        string address;
        int phoneNumber;
        string email;
        
        cin >> id;
        cin >> name;
        cin >> lastName;
        cin >> birthdate;
        cin >> gender;
        cin >> address;
        cin >> phoneNumber;
        cin >> email;


        Worker w(name,lastName, birthdate, gender, address, phoneNumber, email)


        break;

    case 2:
        /* code */
        break;

    case 3:
        /* code */
        break;

    case 4:
        /* code */
        break;

    case 5:
        /* code */
        break;

    case 6:
        /* code */
        break;
    
    default:
        break;
    }


}

void menu(){

    cout << "**** Menu de Opciones ****" << endl;
    cout << "1. Crear objetos" << endl;
    cout << "2. Reservar vuelo" << endl;
    cout << "3. Consultar, modificar y ingrsar" << endl;
    cout << "4. Asignacion de vuelos " << endl;
    cout << "5. Asignacion de puertas de embarque " << endl;
    cout << "6. Salir" << endl;
    cout << "****************************" << endl;

    int op;


}

int main(){

    int op;
    do{
        menu();
        cout << "Seleccione una opcción >";
        cin >> op;
        cout << endl;

        switch (op)
        {
        case 1:
            /* code */
            break;

        case 2:
            /* code */
            break;

        case 3:
            /* code */
            break;
        
        case 4:
            /* code */
            break;

        case 5:
            /* code */
            break;

        case 6:
            /* code */
            break;

        default:
            cout << "Opcion invalida. Marque una opcion valida >";
            cin >> op;
            cout << endl; 
            break;
        }

    }while(op != 6);

  
    return 0;

}
