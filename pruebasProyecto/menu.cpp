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
        op = 7;

        break;

    case 2:
        Airport::getInstance().createAirplane();
        op = 7;
        break;

    case 3:
        Airport::getInstance().createHelicopter();
        op = 7;
        break;

    case 4:
        Airport::getInstance().createPrivateJet();
        op = 7;
        break;

    case 5:
        Airport::getInstance().createPassenger();
        op = 7;
        break;

    case 6:
        Airport::getInstance().createGate();
        op = 7;
        break;
    default:
        cout << "Opcion invalida, digite una nueva opcion: ";
        cin >> op;
        cout << endl;
        break;
    }while(op!=7);
    cout << "Volviendo al menu principal..." << endl;


}
void consultar(){
    cout << "**** Consultar objetos ****" << endl;
    cout << "1. Aviones" << endl;
    cout << "2. Helicopteros" << endl;
    cout << "3. Jets privados" << endl;
    cout << "4. Salir" << endl;
    cout << "****************************" << endl;
    int op;
    cout << "Elija una opcion > ";
    cin >> op;
    cout << endl;
    switch (op)
    {
    case 1:
        Airport::getInstance().printAirplanes();    
        op = 4;
        break;

    case 2:
        Airport::getInstance().printHelicopters();
        op = 4;
        break;

    case 3:
        Airport::getInstance().printPrivateJets();
        op = 4;
        break;
    default:
        cout << "Opcion invalida, digite una nueva opcion: ";
        cin >> op;
        cout << endl;
        break;
    }while(op!=4);
    cout << "Volviendo al menu principal..." << endl;
    cout << "Su objeto ha sido modificado con exito" << endl;

}

void menu(){

    cout << "**** Menu de Opciones ****" << endl;
    cout << "1. Crear objetos" << endl;
    cout << "2. Reservar vuelo" << endl;
    cout << "3. Consultar objetos" << endl;
    cout << "4. Modificar objetos" << endl;
    cout << "5. Asignacion de vuelos " << endl;
    cout << "6. Asignacion de puertas de embarque " << endl;
    cout << "7. Salir" << endl;
    cout << "****************************" << endl;

    int op;


}

int main(){
    string dest;
    string date;
    int num = Airport::getInstance().getPassengersRegisterSize();
    Passenger* _passenger = nullptr;    

    //cout << "Identifícate por favor, llena los siguientes datos para poder reservar el vuelo" << endl;
    //Airport::getInstance().createPassenger();
    //_passenger = Airport::getInstance().getPassenger(num);


    int op;
    do{
        menu();
        cout << "Seleccione una opcion > ";
        cin >> op;
        cout << endl;
        string dest;
        string date;

        switch (op)
        {
        case 1:
            crearObjetos();
            break;

        case 2:
            cout << "Identificate por favor, llena los siguientes datos para poder reservar el vuelo" << endl;
            num = Airport::getInstance().getPassengersRegisterSize();
            Airport::getInstance().createPassenger();
            _passenger  = Airport::getInstance().getPassenger(num); 

            cout << "Digita el destino del vuelo : ";
        
            cin >> dest;
            cout << "Digite la fecha del vuelo (formato: YYYY-MM-DD): ";
            
            cin >> date;

            try {
            if (date.size() != 10 || date[4] != '-' || date[7] != '-') {
                throw invalid_argument("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.");
            }

            for (int i = 0; i < 10; ++i) {
                if (i != 4 && i != 7 && !isdigit(date[i])) {
                    throw invalid_argument("Fecha inválida. Deben ser números.");
                }
            }
        } catch (const invalid_argument& e) {
            cerr << "Error: " << e.what() << endl;
            return false;
        }           
                Airport::getInstance().buyFlight(dest,date, _passenger);
            
            break;

        case 3:
           consultar();
            break;
        
        case 4:
            modificar();
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
