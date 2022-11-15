import json

d = open("jsonFeriaFinal.json", encoding="utf8")
data = json.load(d)
IngenieriaSistemasCount = 0
adminCount = 0
ComunicaCount = 0
economiaCount = 0
negoCount = 0
derechoCount = 0
industrialCount = 0
civilCount = 0
contaCount = 0
arquiCount = 0
psicoCount = 0
markeCount = 0
listaEmpresas = []
i = data["EntradaZoom"]
listaCodigos = []
for  ingreso1 in i.values():
    for ingreso2 in ingreso1.values():
        for ingreso3 in ingreso2.values():
            for ingreso4 in ingreso3.values():
                for ingreso5 in ingreso4.values():  
                        e = ingreso5['empresaV']
                        fecha = ingreso5["fecha"]
                        if e not in listaEmpresas and fecha[0:5] == "02/11":
                            listaEmpresas.append(e)
print(listaEmpresas)
for E in listaEmpresas:
    i = data["EntradaZoom"][E]["02"]["11"]
    listaCodigos = []
    total = 0
    IngenieriaSistemasCount = 0
    adminCount = 0
    ComunicaCount = 0
    economiaCount = 0
    negoCount = 0
    derechoCount = 0
    industrialCount = 0
    civilCount = 0
    contaCount = 0
    arquiCount = 0
    psicoCount = 0
    markeCount = 0
    for  ingreso1 in i.values():
        for ingreso2 in ingreso1.values():
            id = ingreso2['idV']
            if id not in listaCodigos:
                listaCodigos.append(id)
                if ingreso2["carreraV"] == "INGENIERÍA DE SISTEMAS":
                    IngenieriaSistemasCount += 1
                elif ingreso2["carreraV"] == "ADMINISTRACIÓN":
                    adminCount += 1
                elif ingreso2["carreraV"] == "ECONOMÍA":
                    economiaCount += 1
                elif ingreso2["carreraV"] == "NEGOCIOS INTERNACIONALES":
                    negoCount += 1
                elif ingreso2["carreraV"] == "DERECHO":
                    derechoCount += 1
                elif ingreso2["carreraV"] == "INGENIERÍA INDUSTRIAL":
                    industrialCount += 1
                elif ingreso2["carreraV"] == "INGENIERÍA CIVIL":
                    civilCount += 1
                elif ingreso2["carreraV"] == "CONTABILIDAD":
                    contaCount += 1
                elif ingreso2["carreraV"] == "COMUNICACIÓN":
                    ComunicaCount += 1
                elif ingreso2["carreraV"] == "ARQUITECTURA":
                    arquiCount += 1
                elif ingreso2["carreraV"] == "PSICOLOGÍA":
                    psicoCount += 1
                elif ingreso2["carreraV"] == "MARKETING":
                    markeCount += 1

    

            #print(ingreso2)
    total = IngenieriaSistemasCount + adminCount + ComunicaCount + economiaCount + negoCount + derechoCount + industrialCount + civilCount + contaCount + arquiCount + psicoCount + markeCount
    #print(listaCodigos)
    print("Conteo de ingresos Zoom empresa: " + E)
    print("Ingresos totales: " + str(total))
    print("Ingresos de Ingeniería de Sistemas: " + str(IngenieriaSistemasCount))
    print("Ingresos de Administración: " + str(adminCount))
    print("Ingresos de Economía: " + str(economiaCount))
    print("Ingresos de Negocios Internacionales: " + str(negoCount))
    print("Ingresos de Derecho: " + str(derechoCount))
    print("Ingresos de Ingeniería Industrial: " + str(industrialCount))
    print("Ingresos de Ingeniería Civil: " + str(civilCount))
    print("Ingresos de Contabilidad: " + str(contaCount))
    print("Ingresos de Comunicación: " + str(ComunicaCount))
    print("Ingresos de Arquitectura: " + str(arquiCount))
    print("Ingresos de Psicología: " + str(psicoCount))
    print("Ingresos de Marketing: " + str(markeCount))
    print(" ")
    