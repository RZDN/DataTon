from pickle import FALSE
from pandas import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from products import Products



#Consorcios
#url_Consorcio2018 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_CONSORCIO2018.csv"
#url_Consorcio2019 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_CONSORCIO2019.csv"
#url_Consorcio2020 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_CONSORCIO2020.csv"
#url_Consorcio2021 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_CONSORCIO2021.csv"
#url_Consorcio2022 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_CONSORCIO2022.csv"

#Proveedores
url_Proveedores2018 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_PROVEEDORES2018.csv"
url_Proveedores2019 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_PROVEEDORES2019.csv"
url_Proveedores2020 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_PROVEEDORES2020.csv"
url_Proveedores2021 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_PROVEEDORES2021.csv"
url_Proveedores2022 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_PROVEEDORES2022.csv"


#Faltas

url_Penalidades = "https://raw.githubusercontent.com/RZDN/DataTon/main/Penalidades2018.csv"
url_Penalidades2021 = "https://raw.githubusercontent.com/RZDN/DataTon/main/Penalidades2021.csv"

#Sancionados
url_sancionados = "https://raw.githubusercontent.com/RZDN/DataTon/main/Sancionados.csv"

#consorcio2018 = pd.read_csv(url_Consorcio2018,encoding ='utf-8')
#consorcio2019 = pd.read_csv(url_Consorcio2019,encoding ='utf-8')
#consorcio2020 = pd.read_csv(url_Consorcio2020,encoding ='utf-8')
#consorcio2021 = pd.read_csv(url_Consorcio2021,encoding ='utf-8')
#consorcio2022 = pd.read_csv(url_Consorcio2022,encoding ='utf-8')

#Adjudicaciones
url_Adjudicaciones2018 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_ADJUDICACIONES2018.csv"
url_Adjudicaciones2019 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_ADJUDICACIONES2019.csv"
url_Adjudicaciones2020 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_ADJUDICACIONES2020.csv"
url_Adjudicaciones2021 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_ADJUDICACIONES2021.csv"
url_Adjudicaciones2022 = "https://raw.githubusercontent.com/RZDN/DataTon/main/CONOSCE_ADJUDICACIONES2022.csv"

#proveedores
proveedores2018= pd.read_csv(url_Proveedores2018,encoding ='utf-8')
proveedores2019= pd.read_csv(url_Proveedores2019,encoding ='utf-8')
proveedores2020= pd.read_csv(url_Proveedores2020,encoding ='utf-8')
proveedores2021= pd.read_csv(url_Proveedores2021,encoding ='utf-8')
proveedores2022= pd.read_csv(url_Proveedores2022,encoding ='utf-8')


Penalidades2018 = pd.read_csv(url_Penalidades,encoding ='utf-8',)
Penalidades2021 = pd.read_csv(url_Penalidades2021,encoding ='utf-8',)

Sancionados2022 = pd.read_csv(url_sancionados,encoding = 'utf-8') 

#Sancionados
lista_Sancionados2022 = Sancionados2022['RUC'].unique()

#penalidades
lista_penalidades2018 = Penalidades2018['RUC CONTRATISTA'].unique()
lista_penalidades2021 = Penalidades2021['RUC CONTRATISTA'].unique()


#proveedores
lista_proveedores2018 = proveedores2018['RUCPROVEEDOR'].unique()
lista_proveedores2019 = proveedores2019['RUCPROVEEDOR'].unique()
lista_proveedores2020 = proveedores2020['RUCPROVEEDOR'].unique()
lista_proveedores2021 = proveedores2021['RUCPROVEEDOR'].unique()
lista_proveedores2022 = proveedores2022['RUCPROVEEDOR'].unique()


#Data Adjudicaciones
adjudicaciones2018 = pd.read_csv(url_Adjudicaciones2018,encoding ='utf-8')
adjudicaciones2019 = pd.read_csv(url_Adjudicaciones2019,encoding ='utf-8')
adjudicaciones2020 = pd.read_csv(url_Adjudicaciones2020,encoding ='utf-8')
adjudicaciones2021 = pd.read_csv(url_Adjudicaciones2021,encoding ='utf-8')
adjudicaciones2022 = pd.read_csv(url_Adjudicaciones2022,encoding ='utf-8')

#proveedores sancionados 
proveedores_sancionados2022 = []
#2018
for i in lista_Sancionados2022:
  for j in lista_proveedores2018:
    if i == j and j not in proveedores_sancionados2022:
      proveedores_sancionados2022.append(j)

for i in lista_Sancionados2022:
  for j in lista_proveedores2019:
    if i == j and j not in proveedores_sancionados2022:
      proveedores_sancionados2022.append(j)

for i in lista_Sancionados2022:
  for j in lista_proveedores2020:
    if i == j and j not in proveedores_sancionados2022:
      proveedores_sancionados2022.append(j)

for i in lista_Sancionados2022:
  for j in lista_proveedores2021:
    if i == j and j not in proveedores_sancionados2022:
      proveedores_sancionados2022.append(j)

for i in lista_Sancionados2022:
  for j in lista_proveedores2022:
    if i == j and j not in proveedores_sancionados2022:
      proveedores_sancionados2022.append(j)

#proveedores penalizados
proveedores_penalizados = []
#2018
for i in lista_penalidades2018:
  for j in lista_proveedores2018:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

for i in lista_penalidades2018:
  for j in lista_proveedores2019:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

for i in lista_penalidades2018:
  for j in lista_proveedores2020:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

for i in lista_penalidades2018:
  for j in lista_proveedores2021:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

for i in lista_penalidades2018:
  for j in lista_proveedores2022:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

#2022
for i in lista_penalidades2021:
  for j in lista_proveedores2018:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

for i in lista_penalidades2021:
  for j in lista_proveedores2019:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

for i in lista_penalidades2021:
  for j in lista_proveedores2020:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

for i in lista_penalidades2021:
  for j in lista_proveedores2021:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)

for i in lista_penalidades2021:
  for j in lista_proveedores2022:
    if i == str(j) and j not in proveedores_penalizados:
      proveedores_penalizados.append(j)


lista_final = []

for i in proveedores_sancionados2022:
  if i not in lista_final:
    lista_final.append(i)

for i in proveedores_penalizados:
  if i not in lista_final:
    lista_final.append(i)

data_infraccion = pd.DataFrame() 
for i in lista_final:
  data_infraccion = pd.concat([data_infraccion,proveedores2018[proveedores2018["RUCPROVEEDOR"] == i]])
  data_infraccion = pd.concat([data_infraccion,proveedores2019[proveedores2019["RUCPROVEEDOR"] == i]])
  data_infraccion = pd.concat([data_infraccion,proveedores2020[proveedores2020["RUCPROVEEDOR"] == i]])
  data_infraccion = pd.concat([data_infraccion,proveedores2021[proveedores2021["RUCPROVEEDOR"] == i]])
  data_infraccion = pd.concat([data_infraccion,proveedores2022[proveedores2022["RUCPROVEEDOR"] == i]])

data_infraccion = data_infraccion.drop_duplicates(subset=['RUCPROVEEDOR'])


app = Flask(__name__)
CORS(app)

@app.route('/products')
def getproducts():
    return jsonify({"products": Products})

@app.route('/empresas')
def getEmpresas(): 

  datos = []
  for i in range(len(lista_final)):
    dic = {"RUCPROVEEDOR": data_infraccion.values[i][0],"PROVEEDOR": data_infraccion.values[i][1],"ORIGEN": data_infraccion.values[i][2],"DEPARTAMENTO": data_infraccion.values[i][3],"PROVINCIA": data_infraccion.values[i][4],"DISTRITO": data_infraccion.values[i][5]}
    datos.append(dic)

  return jsonify({"empresas": datos})


@app.route('/empresas/<string:ruc>')
def getEmpresa(ruc):
  prueba =[]
  for i in range(len(Penalidades2018)):
    if ruc == Penalidades2018['RUC CONTRATISTA'][i]:
      dic = {"ID CONTRATO":str(Penalidades2018['ID CONTRATO'][i]),"RUC CONTRATISTA":Penalidades2018['RUC CONTRATISTA'][i],"TIPO PENALIDAD":Penalidades2018['TIPO PENALIDAD'][i],"OBJETO CONTRATO":Penalidades2018['OBJETO CONTRATO'][i],"ENTIDAD CONTRATANTE":Penalidades2018['ENTIDAD CONTRATANTE'][i]}
      prueba.append(dic)

  return jsonify({"empresa": prueba})

@app.route('/empresas/<string:ruc>/penalidades')
def getPenalidadEmpresa(ruc):
  prueba = pd.DataFrame() 

  prueba = prueba.append(Penalidades2018[Penalidades2018["RUC CONTRATISTA"] == ruc])
  prueba = prueba.append(Penalidades2021[Penalidades2021["RUC CONTRATISTA"] == ruc])
  penalidades_proveedor = []
  for i in range(len(prueba)):
    dic = {"ID CONTRATO": prueba.values[i][0],"RUC CONTRATISTA": prueba.values[i][1],"TIPO PENALIDAD": prueba.values[i][2],"OBJETO CONTRATO": prueba.values[i][3],"ENTIDAD CONTRATANTE": prueba.values[i][4],"ECHA PENALIDAD": prueba.values[i][5],"DESCRIPCION/MOTIVO": prueba.values[i][6],"MONTO": prueba.values[i][7]}
    penalidades_proveedor.append(dic)

  return jsonify({"penalidades": penalidades_proveedor})


@app.route('/empresas/<int:ruc>/sanciones')
def getSancionesEmpresa(ruc):
  sancion_empresa = pd.DataFrame() 
  sancion_empresa = sancion_empresa.append(Sancionados2022[Sancionados2022["RUC"] == ruc])

  
  Sanciones_Proveedor = []
  for i in range(len(sancion_empresa)):
    dic = {"FECHA_CORTE ": sancion_empresa.values[i][0],"RUC": sancion_empresa.values[i][1],"NOMBRE_RAZONODENOMINACIONSOCIAL": sancion_empresa.values[i][2],"FECHA_INICIO": sancion_empresa.values[i][3],"FECHA_FIN": sancion_empresa.values[i][4],"NUMERO_RESOLUCION": sancion_empresa.values[i][5],"ID_MOTIVO_INFRACCION": sancion_empresa.values[i][6],"MOTIVO_DE_INFRACCION": sancion_empresa.values[i][7]}
    Sanciones_Proveedor.append(dic)

  return jsonify({"penalidades": Sanciones_Proveedor})


@app.route('/empresas/<string:ruc>/adjudicaciones')
def getAdjudicacionesEmpresa(ruc):
  data_adjudicaciones = pd.DataFrame()
  data_adjudicaciones = pd.concat([data_adjudicaciones,adjudicaciones2018[adjudicaciones2018["RUC_PROVEEDOR"] == ruc]])
  data_adjudicaciones = pd.concat([data_adjudicaciones,adjudicaciones2019[adjudicaciones2019["RUC_PROVEEDOR"] == ruc]])
  data_adjudicaciones = pd.concat([data_adjudicaciones,adjudicaciones2020[adjudicaciones2020["RUC_PROVEEDOR"] == ruc]])
  data_adjudicaciones = pd.concat([data_adjudicaciones,adjudicaciones2021[adjudicaciones2021["RUC_PROVEEDOR"] == ruc]])
  data_adjudicaciones = pd.concat([data_adjudicaciones,adjudicaciones2022[adjudicaciones2022["RUC_PROVEEDOR"] == ruc]])


  lista_adjudicaciones = []
  for i in range(len(data_adjudicaciones)):
    dic = {"CODIGOENTIDAD": data_adjudicaciones.values[i][0],"ENTIDAD_RUC": data_adjudicaciones.values[i][1],"CODIGOCONVOCATORIA": data_adjudicaciones.values[i][2],"PROCESO": data_adjudicaciones.values[i][3],"N_ITEM": data_adjudicaciones.values[i][4],"DESCRIPCION_ITEM": data_adjudicaciones.values[i][5],"ESTADO_ITEM": data_adjudicaciones.values[i][6],"CANTIDAD_ADJUDICADO_ITEM": data_adjudicaciones.values[i][7],"MONTO_REFERENCIAL_ITEM": data_adjudicaciones.values[i][8],"MONTO_ADJUDICADO_ITEM": data_adjudicaciones.values[i][9],"MONEDA": data_adjudicaciones.values[i][10],"UNIDAD_MEDIDA": data_adjudicaciones.values[i][11],"RUC_PROVEEDOR": data_adjudicaciones.values[i][12],"PROVEEDOR": data_adjudicaciones.values[i][13],"TIPO_PROVEEDOR": data_adjudicaciones.values[i][14],"FECHA_CONVOCATORIA": data_adjudicaciones.values[i][15],"FECHA_BUENAPRO": data_adjudicaciones.values[i][16],"FECHA_CONSENTIMIENTO_BP": data_adjudicaciones.values[i][17]}
    lista_adjudicaciones.append(dic)

  return jsonify({"adjudicaciones": lista_adjudicaciones})

@app.route('/empresas/falsos')
def getFalsasEmpresa():
  falsos = Sancionados2022[Sancionados2022['DE_MOTIVO_INFRACCION'].str.contains('DOCUMENTOS FALSOS')]
  documentacion_falsa = []
  for i in range(len(falsos)):
    dic = {"FECHA_CORTE ": falsos.values[i][0],"RUC": falsos.values[i][1],"NOMBRE_RAZONODENOMINACIONSOCIAL": falsos.values[i][2],"FECHA_INICIO": falsos.values[i][3],"FECHA_FIN": falsos.values[i][4],"NUMERO_RESOLUCION": falsos.values[i][5],"ID_MOTIVO_INFRACCION": falsos.values[i][6],"MOTIVO_DE_INFRACCION": falsos.values[i][7]}
    documentacion_falsa.append(dic)

  return jsonify({"falsos": documentacion_falsa})

if __name__ == '__main__':
    app.run(debug=True, port=4000)