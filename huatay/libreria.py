
#ejercicio 01 "validacion de un entero"
def validar_un_entero(entero):  #se aplica la funcion validar un entero
    if entero.isalnum()==True:  #condicion doble
        validacion="El numero "+str(entero)+" si es entero"  #se guarda un valor en la variable validacion
        return validacion             #retorna la variable validacion
    else:
        return False            #retorna falso si la condicion es falsa
    #fin_def

#ejercicio 2 "validacion de una cadena"
def validar_cadena(msg):    #se aplica la funcion validar cadena:
    if msg.isalpha()==True:# #se aplica una condicional doble
        validacion_cadena="El valor "+msg+" si es una cadena " #se guarda un valor en la variable validacion de cadena
        return validacion_cadena  #retorna el valor de la variable validacion cadena
    else:
        return False     #retorna falso si la condicion es falsa
    #fin_def


#ejercicio 03 "validacion de ataque  y recompensa de un videojuego"
def validar_dano(ataque): #funcion def
    print("INDICAR EL TIPO A QUIEN ATACA MELE o RANGO") #se imprime un comentario inicial
    if  ataque.isdigit()==False: #se valida si  no es un numero condicion doble
        if ataque=="MELE":    #condiciones multiples  para ver que recommpensa se ganara
            rm=35
            recompensa_mele="Su recompensa es de: "+str(rm)
            return recompensa_mele
        elif ataque=="RANGO":
            rr=43
            recompensa_rango="Su recompensa es de: "+str(rr)
            return recompensa_rango
        else:
            comando="el comando ingresado es FALSO"
            return comando
    else:
        return False
#fin_def


#ejercicio 04 "validacion de impresion de numeros de 3 digitos"
def validar_numero_tres_cifras(numero):#funcion def
    #validando si es de tres cifras
    if len(numero)==3:
        #validando si es entero
        if numero.isdigit()==True:
            return True

        else:
            return False
    else:
        return  False
#fin_def


#ejercicio 05 "validacion de una vocal"
def validar_vocal(vocal):
    #validando la longitud
    if len(vocal)==1:
        #validando si es una vaocal ingresada
        if vocal=="a" or  vocal=="e" or vocal=="i" or vocal=="o" or vocal=="u" :
            return True
        else:
            return False
    else:
        return False

    #fin_def

#ejercicio 06 "validacion de DNI"
def validar_dni(DNI):
    #primero validamos la longitud de la cadena
    if len(DNI)==8:
        #valdidamos que los datos ingresados sean puros numero enteros
        if DNI.isdigit()==True:
            return True
        else:
            return False
    else:
        return False

#ejercicio 07 "validar Ruc SUNAT"
def validar_ruc(RUC):
    fragmento=validar_dni("")
    #primero validamos la longitud de la cadena que consta de 11 digitos
    if len(RUC)==11:
        #segundo validamos las condiciones de la cadena
        if RUC[0:2]==10:
            print("la persona es un trabajador  fisico o natural")
            #una ves que validamos  todas las condiciones de la cadena sigue validar el numero de dni
            #para eso creamos una variable a al que llamemos a la funcion validar dni
            if RUC[2:11]==fragmento:
               #por ultimo hacemos la validacion delultimo codigo que siempre debe ser de 8
               if RUC[11]==8:
                   print("el codigo es correcto") #una ves que hicimos la validacion de la cadena lo que haremos finalmente es verificar si es int
                   if RUC.isdigit()==True:
                       return True
                   else:
                       return False
               else:
                return False
            else:
                return False
        elif RUC[0:2]==20:
            print("la persona es una trabajador fisico")
            if RUC[2:11]==fragmento:
                if RUC[11]==8:
                    print("el codigo es correcto")
                    if RUC.isdigit()==True:
                        return True
                    else:
                        return False
            else:
                return False
        elif RUC[0:2]==15:
            print("La persona es una socidad ")
            if RUC[2:11]==fragmento:
                if RUC[11]==8:
                    print("el codigo es correcto")
                    if RUC.isdigit()==True:
                        return True
                    else:
                        return False
            else:
                 return False
        elif RUC[0:2]==16:
            print("se menciona como valido")
            if RUC[2:11]==fragmento:
                if RUC[11]==8:
                    print("el codigo es correcto")
                    if RUC.isdigit()==True:
                        return True
                    else:
                        return False
            else:
                 return False
        elif RUC[0:2]==17:
            print("inscripcion durante 2019 a 2025")
            if RUC[2:11]==fragmento:
                if RUC[11]==8:
                    print("el codigo es correcto")
                    if RUC.isdigit()==True:
                        return True
                    else:
                        return False
            else:
                 return False
        else:

            return False

    else:
        return False



#ejercicio 08 "validar un numero capicua"

def validar_capicua(capicua):
     #primero validamos que sea int
    if capicua.isdigit()==True:
        #segundo para que un numero sea capicua tiene que ser igual que su inversa entonces
        if capicua==capicua[::-1]:
            return True
        else:
            return False
    else:
        return False

    #fin_si
#fin_def


#ejercicio 09 "validar edad"
def validar_edad(edad):
    #primero validar si es entero
    if edad.isdigit()==True:
        if  edad>0 and edad<120:
            return True
        else:
            return False

    else:
        return False
    #fin_si

#fin_def

#ejercicio 10 "validar codigo de alumno de UNPRG"
def validar_codigo_unprg(codigo):
    #primero validamos la longitud de la cadena
    if len(codigo)==7:
        #validacion de los dos primero digitos
        if codigo[0:2]==19:
            #validamos la ultima parte de la cadena
            if codigo[7].isdigit()==True:
                #validamos que una parte de la cadena sea numeros
                if codigo[0:7].isdigit()==True:
                    return True
                else:
                    return False
                #fin_si
            else:
                return False
            #fin_si
        else:
            return False
        #fin_si
    else:
        return False
    #fin_si

#fin_def

#ejercicio 11 "validacion de  una fuerza realizada"
def validar_fuerza(masa,aceleracion):
    #primero validamos el numero ingresado que sea un real
    fuerza=int(masa)*int(aceleracion)
    fuerza_cero="La fuerza realizada es cero ya que la aceleracion es igual a 0"
    if masa.isdigit()==True:
        if aceleracion.isdigit()==True:
            if fuerza==0:
                return fuerza_cero
            elif fuerza>0:
                return fuerza
            else:
                return -1*fuerza

        else:
            return False
    else:
        return False
    #fin_si
#fin_def

#ejercicio 12 "validar un interruptor"
def validar_interruptor(comando):
    #validar que sea un str:
    on="prendido"
    oof="apagado"
    if comando.isalpha()==True:
        #una ves que validamos que sea un str colocamos las condiciones
        if comando.upper()=="ON":
            return  on
        elif comando.upper()=="OOF":
            return oof
        else:
            return False
    else:
        return False


    #fin_si

#ejercicio 13 "lanzamiento de un balon de basket"
def validar_lanzamiento(distancia):
    #validamos primeramente la longitud de la cadena
    if len(distancia[0])>0 and len(distancia[0])<=3:
        #validamos que sea alfanumerico

        if distancia.isalnum()==True:

            if len(distancia)==2:
                #validamos que tenga el signo al final
                if distancia[1]=="m":
                    if int(distancia[0])>=6:
                        print("fue anotacion de 3")
                    else:
                        print("FUE anotacion de 2")
                else:
                    return False
            elif len(distancia)==3:
                if distancia[2]=="m":
                    if int(distancia[0])>=6:
                        print("fue anotacion 3")
                    else:
                        print("fue anotacion de 2")
                else:
                    return False
            else:
                 return False
        else:
            return False
    else:
        return False

#ejercicio 14 "numero telefonico de peru ejemplo "+51973396201" "
def validar_numero_peru(telefono):
    #validamos la longitud de la cadena
    if len(telefono)==12:
        #validamos el valor  inicial
        if telefono[0]=="+":
            #validamos los dos siguientes digitos
            if telefono[1:3]==51:
                if telefono[1:].isdigit()==True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


#ejercicio 15 "validar un factorial"

def validar_factorial(cifras,factorial):
    cif=1
    #validamos la longitud de cualquier factorial  y a la vez estamos validando de que no sea un numero negativo
    if cifras+1==len(factorial):
        #validamos el ingreso de factoriales
        if factorial[cifras+1]=="!":
            #validamos que sean numeros
            if factorial[0:cifras+1].isdigit()==True:
                #una vez que validamos esttablecemos condiciones
                #si es facotrial d euno o cero retorna automaticamente un 1 si no se hara el calculo respectivoy retornara la variable factor
                if factorial=="1!" or factorial=="0!":
                    return 1
                else:
                    for i in range(2,factorial[0:cifras+1]):
                        cif*=i
                        return cif
            else:
                return False
        else:
            return False
    else:
        return False
    #FIN_SI

#fin_def

#ejercicio 16 "validar el comando de un videojuego"
def valida_salto(hop):
    pos=1
    letra=""
    numero=""
    direccion=""
    if len(hop)==13:
        for iteam in  hop.split(" "):
            if pos==1:
                iteam=letra
                if letra.isdigit()==False:
                    return True
                else:
                    return False
            if pos==2:
                iteam=numero
                if numero.isalpha()==False:
                    return True
                else:
                    return False
            if pos==3:
                iteam=direccion
                if direccion.isdigit()==False:
                    return True
                else:
                    return False
    else:
        return False


#ejercicio 17 "validar la hora ingresada ejemplo 03:34 am"
def validar_hora(horario):
    pico_del_dia="12:00 m"
    #validamos la longitud
    if len(horario)==8:
        #validamos la estructura de la cadena
        if horario[0:2].isdigit()==True:
            if horario[2]==":":
                if horario[3:5].isdigit()==True:
                    if horario[5]==" ":
                        if horario[6:]=="am":
                            return True
                        elif horario[6:]=="pm":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif len(horario)==7:
        return pico_del_dia
    else:
        return False



#ejercicio 18 "validar un numero mayo de 2 cifras en donde si es mayor retorna el numero mayor"
def validar_mayor(num1,num2):
    #validamos la longitud
    if  len(num1)==2 and len(num2):
        #validamos si la cadena esta compuesta de digitos
        if num1.isdigit()==True and num2.isdigit()==True:
            #validamos que sea mayor
            if num1>num2:
                return num1
            else:
                return False
        else:
            return False
    else:
        return False


#ejercicio 19 "validar un numero menor de 2 cifras en donde si es menor retorna el menor"
def validar_menor(numero1,numero2):
    #validamos la longitud
    if len(numero1)==2 and len(numero2):
        #VALIDAMOS QUE LA CADENA ESTE COMPUESTA DE NUMEROS
        if numero1.isdigit()==True and numero2.isdigit()==True:
            #validamos que sea menor
            if numero1<numero2:
                return numero1
            else:
                return False
        else:
            return False
    else:
        return False

#ejercicio 20 ""



