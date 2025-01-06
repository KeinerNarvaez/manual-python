def salario(dias,valordia):
    return dias*valordia
def salud(dias,valordia): 
    pago_salud=salario(dias,valordia)*0.12
    return pago_salud

def pension(dias,valordia):
    pago_pension=salario(dias,valordia)*0.16
    return pago_pension   

def deducible(dias,valordia):
    pago_deducible = pension(dias,valordia)+ salud(dias,valordia);
    return pago_deducible

def arl (dias,valordia):
    pago_arl = salario(dias,valordia)*0.052
    return pago_arl
def pagototal(dias,valordia):
    pago_total = salario(dias,valordia)-deducible(dias,valordia);
    return pago_total
def subtrans(dias,valordia):
    salarioMin= 1600000;
    salariotrans=salario(dias,valordia);
    subtransporte=0
    if salariotrans<=2*salarioMin:
        subtransporte=114000
    else: 
        subtransporte=0;
    return subtransporte
def retencion(dias,valordia):
    if salario(dias,valordia)>7800000:
        retencion_total=0.02
    if (salario(dias,valordia)>10400000):
        retencion_total=0.04
    if (salario(dias,valordia)>15600000):
        retencion_total=0.08
    else:
        retencion_total="No tiene retencion";
    return retencion_total



nomina=[
{
'id':'1',
'nombres':'keiner andres',
'apellidos':'cano narvaez',
'cargo':'programador',
'valorDia':100000,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'2',
'nombres':'alfredo olimpica',
'apellidos':'santa rosa',
'cargo':'coserje',
'valorDia':50000,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'3',
'nombres':'jhampier',
'apellidos':'santos ortiz',
'cargo':'programador',
'valorDia':100000,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'4',
'nombres':'monica natalia',
'apellidos':'lozada castañeda',
'cargo':'conserje',
'valorDia':500000,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'5',
'nombres':'carlos francisco',
'apellidos':'andrade bermeo',
'cargo':'hornero',
'valorDia':43333,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'6',
'nombres':'nestor david',
'apellidos':'lozano castañeda',
'cargo':'programador',
'valorDia':43333,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'7',
'nombres':'angel',
'apellidos':'farid',
'cargo':'hornero',
'valorDia':43333,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'8',
'nombres':'jose santiago',
'apellidos':'ballen',
'cargo':'repartidor',
'valorDia':43333,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'9',
'nombres':'zully vanesa',
'apellidos':'camacho',
'cargo':'enfermera',
'valorDia':43333,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
},
{
'id':'10',
'nombres':'sandra milena',
'apellidos':'navaez rodriguez',
'cargo':'docente',
'valorDia':43333,'diasTrabajados':30,'salario':0,
'subtransporte':0,'salud':0,'pension':0,'arl':0,'retencion':0,'total_pagar':0,
}]

for empleado in nomina:
    valor_dia = empleado['valorDia']
    dias_trabajados = empleado['diasTrabajados']
    empleado['salario'] = salario(dias_trabajados, valor_dia)
    empleado['subtransporte'] = subtrans(dias_trabajados, valor_dia)
    empleado['salud'] = salud(dias_trabajados, valor_dia)
    empleado['pension'] = pension(dias_trabajados, valor_dia)
    empleado['arl'] = arl(dias_trabajados, valor_dia)
    empleado['total_pagar'] = pagototal(dias_trabajados, valor_dia)
    empleado['retencion'] = retencion(dias_trabajados, valor_dia)

# Imprimir la nómina
for empleado in nomina:
    print(empleado)
