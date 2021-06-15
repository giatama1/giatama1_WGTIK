/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package segitiga;

import java.util.Scanner;
/**
 *
 * @author asus
 */
public class Segitiga {
    private double a,b,c;
    private boolean hasil;
    boolean hasilCek;
    Scanner keyboard = new Scanner(System.in);

    public double getA() {
        return a;
    }

    public double getB() {
        return b;
    }

    public double getC() {
        return c;
    }

    public void setA(int a) {
        this.a = a;
    }

    public void setB(int b) {
        this.b = b;
    }

    public void setC(int c) {
        this.c = c;
    }
    
    public boolean cekBilanganTidakDptSegitiga(){
        if(getA()>getB() && getA()>getB() ){
            if(getA()>=getB()+getC()){
                hasil = true;
            }
        }else if(getB()>getA() && getB()>getC()){
            if(getB()>=getA()+getC()){
                hasil = true;
            }
        }else if(getC()>getA() && getC()>getB()){
            if(getC()>=getA()+getB()){
                hasil = true;
            }
        }
        return hasil;
    }
    public boolean cekBilanganTerbesarKuadrat(){
        double kuadratBilTerbesar;
        double kuadratBilTerkecil;
        
        if(Math.round(getA())>Math.round(getB()) && Math.round(getA())>Math.round(getC()) ){
            kuadratBilTerbesar = Math.round(getA())^2;
            kuadratBilTerkecil = Math.round(getB())^2+Math.round(getC())^2;
            if(kuadratBilTerbesar == kuadratBilTerkecil){
                hasilCek = true;
            }
        }else if(Math.round(getB())>Math.round(getA()) && Math.round(getB())>Math.round(getC())){
            kuadratBilTerbesar = Math.round(getB())^2;
            kuadratBilTerkecil = Math.round(getA())^2+Math.round(getC())^2;
            if(kuadratBilTerbesar == kuadratBilTerkecil){
                hasilCek = true;
            }
        }else if(Math.round(getC())>Math.round(getA()) && Math.round(getC())>Math.round(getB())){
            kuadratBilTerbesar = Math.round(getC())^2;
            kuadratBilTerkecil = Math.round(getA())^2+Math.round(getB())^2;
            if(kuadratBilTerbesar == kuadratBilTerkecil){
                hasilCek = true;
            }
        }
        return hasilCek;
    }
    public void segitigaBebas(double a, double b, double c){
        if(a>b && a>c ){
            if(a<b+c){
                System.out.println("Segitiga Bebas");
            }
        }else if(b>a && b>c){
            if(b<a+c){
                System.out.println("Segitiga Bebas");
            }
        }else if(c>a && c>b){
            if(c<a+b){
                System.out.println("Segitiga Bebas");
            }
        }
    }
    public void cekJenisSegitiga(double a, double b, double c){
        if((a==b || b==c || a==c) && (a!=b || b!=c || a!=c)){
            System.out.println("Segitiga Sama Kaki");
        }else if(a==b && b==c){
            System.out.println("Segitiga Sama Sisi");
        }else if(a<0 || a==0 && b<0 || b==0 && c<0 || c==0){
            System.out.println("Segitiga tidak dapat dibangun");
        }else if(cekBilanganTidakDptSegitiga()==true){
            System.out.println("Segitiga tidak dapat dibangun");
        }else if(cekBilanganTerbesarKuadrat()== true){
            System.out.println("Segitiga Siku-Siku");
        }else{
            segitigaBebas(Math.round(a),Math.round(b), Math.round(c));
        }
    }
    public void JenisSegitiga(){
        System.out.println("-----JENIS SEGITIGA-----");
        System.out.println("");
        System.out.println("#Masukkan nilai A# ");
        a = keyboard.nextDouble();
        System.out.println("#Masukkan nilai B# ");
        b = keyboard.nextDouble();
        System.out.println("#Masukkan nilai C# ");
        c = keyboard.nextDouble();
        System.out.println("");
        System.out.println("# HASIL # ");
        cekJenisSegitiga(Math.round(a),Math.round(b),Math.round(c));
    }
    public static void main(String[] args) {
        Segitiga s = new Segitiga();
        s.JenisSegitiga();
    }
    
}
