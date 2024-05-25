/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejercicio1;

/**
 *
 * @author USUARIO
 */
public class Jugadores {

    private String nombre;
    private String apellidos;

    public Jugadores(String x, String c) {

    }

    public void establecerNombre(String x) {
        nombre = x;
    }

    public void establecerApellido(String c) {
        apellidos = c;
    }

    public String obtenerNobre() {
        return nombre;
    }

    public String obtenerApellidos() {
        return apellidos;
    }
}
