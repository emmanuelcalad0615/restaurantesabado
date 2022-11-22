from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos
from web.models import Empleados
# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def PlatosVista(request):

    #Rutina consulta de platos
    platosConsultados=Platos.objects.all()
    print(platosConsultados)


    #Esta vista va a utilizar un formulario de django
    #DEBO CREAR ENTONCES UN OBJETO DE LA CLASE FormularioPlatos()
    formulario=FormularioPlatos()

    #CREAMOS UN DICCIONARIO PARA ENVIAR EL FORMULARIO AL HTML(TEMPLATE)
    data={
        'formulario':formulario,
        'bandera':False,
        'platos':platosConsultados
    }
    #Recibimos los datos del formulario

    if request.method=="POST":
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
           
            #construir un diccionario de envío de datos hacía la db
            platoNuevo=Platos(
                nombre=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                imagen=datosLimpios["fotografia"],
                precio=datosLimpios["precio"],
                tipo=datosLimpios["tipo"]
            )
            #Intentaré llevar mis datos a la BD
            try:
                platoNuevo.save()
                data["bandera"]=True
                print("Exito guardando...")
            except Exception as error:
                print("Ups", error)    
        


    return render(request,'menuplatos.html',data)

def EmpleadosVista(request):
    #Rutina para consulta de empleados
    empleadosConsultados=Empleados.objects.all()
    print(empleadosConsultados)



    formulario2=FormularioEmpleados

    data={
        'formulario2':formulario2,
        'bandera':False, 
        'empleados':empleadosConsultados
        
        
    }
    #Recibimos los datos del formulario
    if request.method=="POST":
        datosFormulario2=FormularioEmpleados(request.POST)
        if datosFormulario2.is_valid():
            datosLimpios=datosFormulario2.cleaned_data
            print(datosLimpios)
            empleadosNuevo=Empleados(
                nombre_emp=datosLimpios["nombre"],
                foto=datosLimpios["foto"],
                cargo=datosLimpios["cargo"],
                salario=datosLimpios["salario"],
                contacto=datosLimpios["contacto"]
            )
            try:
                empleadosNuevo.save()
                data["bandera"]=True
                print("Exito guardando")
            except Exception as error:
                print("ups", error)    



#

    return render(request,'empleados.html', data)

