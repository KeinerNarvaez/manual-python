
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


print(pagototal(15,500000));