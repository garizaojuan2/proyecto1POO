#include <iostream>
#include "aircraft.h"
#include "ControlTower.h"
#include "person.h"
#include "worker.h"
#include "airport.h"

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
    cout << "7. Salir" << endl;
    cout << "****************************" << endl;
    int op;
    cout << "Elija una opcion > ";
    cin >> op;
    cout << endl;

    switch (op)
    {
    case 1:
        Airport::getInstance().createWorker();    

        break;

    case 2:
        Airport::getInstance().createAirplane();
        break;

    case 3:
        Airport::getInstance().createHelicopter();
        break;

    case 4:
        Airport::getInstance().createPrivateJet();
        break;

    case 5:
        Airport::getInstance().createPassenger();
        break;

    case 6:
        Airport::getInstance().createGate();
        break;
    default:
        cout << "Opcion invalida, digite una nueva opcion: ";
        cin >> op;
        cout << endl;
        break;
    }while(op!=7);


}

void menu(){

    cout << "**** Menu de Opciones ****" << endl;
    cout << "1. Crear objetos" << endl;
    cout << "2. Reservar vuelo" << endl;
    cout << "3. Ingresar, consultar y modificar " << endl;
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
        cout << "Seleccione una opcion > ";
        cin >> op;
        cout << endl;

        switch (op)
        {
        case 1:
            crearObjetos();
            break;

        case 2:
            cout << "Identificate por favor, llena los siguientes datos para poder reservar el vuelo" << endl;
            Airport::getInstance().createPassenger();
            
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
