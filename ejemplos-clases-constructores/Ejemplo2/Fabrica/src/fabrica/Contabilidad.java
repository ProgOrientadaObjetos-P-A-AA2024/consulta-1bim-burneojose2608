/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fabrica;

/**
 *
 * @author USUARIO
 */
public class Contabilidad {

    private int sueldo;
    private int horas;

    public Contabilidad(int c, int b) {
    }

    public void estableceSueldo(int c) {
        sueldo = c;
    }

    public void establacerHoras(int b) {
        horas = b;
    }

    public int obtenerSueldo() {
        return sueldo;
    }

    public int obtenerHoras() {
        return horas;
    }
}
