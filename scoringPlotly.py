import dash
import plotly.graph_objs as go
import plotly.offline
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash()

#from GZ_ScoringScatterPlt import *
tipo_de_proyectos= ["Edificios residenciales",
                    "Edificios comerciales",
                    "Edificios públicos",
                    "Edificios industriales",
                    "Obras de infraestructura",
                    "Obras de urbanización",
                    "Obras de renovación o rehabilitación",
                    "Obras de mantenimiento",
                    "Obras de mejora o modernización",
                    "Obras de conservación o protección del medio ambiente"
                    ]    

estudios=["Montevideo",
        "ADK",
        "JCMC",
        "RFU",
        "GM",
        "GZ"
        ] 

rango_aa = (20000, 35000)
rango_a = (35001, 42000)
rango_bb = (42001, 47000)
rango_b = (47001, 55000)
rango_cc = (55001, 66000)
rango_c = (66001, 80000)

colores_hex = {
    "AA": "#006600",
    "A": "#00FF00",
    "BB": "#FFFF00",
    "B": "#CCCC00",
    "CC": "#FF0000",
    "C": "#660000",
}
estudios_colores={
        "Montevideo":"#006400",
        "ADK": "#004C40",
        "JCMC": "#1F3A3A",
        "RFU":"#008080",
        "GM": "#00B2B2",
        "GZ": "#66CDAA"
}

proyectos= [{'CO2': 77484, 'M2': 449, 'etiqueta': 'C', 'tipo': 'Obras de renovación o rehabilitación', 'color': '#FB8281', 'estudio': 'GZ'}, {'CO2': 30341, 'M2': 74, 'etiqueta': 'AA', 'tipo': 'Edificios comerciales', 'color': '#00B17B', 'estudio': 'JCMC'}, {'CO2': 20018, 'M2': 6026, 'etiqueta': 'AA', 'tipo': 'Edificios comerciales', 'color': '#00B17B', 'estudio': 'RFU'}, {'CO2': 41804, 'M2': 155, 'etiqueta': 'A', 'tipo': 'Edificios comerciales', 'color': '#002233', 'estudio': 'GZ'}, {'CO2': 66774, 'M2': 2987, 'etiqueta': 'C', 'tipo': 'Obras de infraestructura', 'color': '#FB8281', 'estudio': 'RFU'}, {'CO2': 76818, 'M2': 132, 'etiqueta': 'C', 'tipo': 'Edificios industriales', 'color': '#FB8281', 'estudio': 'JCMC'}, {'CO2': 35624, 'M2': 426, 'etiqueta': 'A', 'tipo': 'Obras de urbanización', 'color': '#002233', 'estudio': 'GM'}, {'CO2': 63651, 'M2': 34, 'etiqueta': 'CC', 'tipo': 'Edificios residenciales', 'color': '#54B5FB', 'estudio': 'Montevideo'}, {'CO2': 27475, 'M2': 287, 'etiqueta': 'AA', 'tipo': 'Obras de conservación o protección del medio ambiente', 'color': '#00B17B', 'estudio': 'GZ'}, {'CO2': 79597, 'M2': 178, 'etiqueta': 'C', 'tipo': 'Edificios comerciales', 'color': '#FB8281', 'estudio': 'RFU'}, {'CO2': 44438, 'M2': 9842, 'etiqueta': 'BB', 'tipo': 'Obras de mejora o modernización', 'color': '#53328B', 'estudio': 'ADK'}, {'CO2': 62906, 'M2': 303, 'etiqueta': 'CC', 'tipo': 'Obras de mejora o modernización', 'color': '#54B5FB', 'estudio': 'JCMC'}, {'CO2': 32740, 'M2': 30, 'etiqueta': 'AA', 'tipo': 'Obras de urbanización', 'color': '#00B17B', 'estudio': 'GM'}, {'CO2': 35865, 'M2': 341, 'etiqueta': 'A', 'tipo': 'Obras de infraestructura', 'color': '#002233', 'estudio': 'GZ'}, {'CO2': 75381, 'M2': 6651, 'etiqueta': 'C', 'tipo': 'Obras de mantenimiento', 'color': '#FB8281', 'estudio': 'Montevideo'}, {'CO2': 33109, 'M2': 413, 'etiqueta': 'AA', 'tipo': 'Edificios públicos', 'color': '#00B17B', 'estudio': 'ADK'}, {'CO2': 48829, 'M2': 319, 'etiqueta': 'B', 'tipo': 'Obras de renovación o rehabilitación', 'color': '#00D47B', 'estudio': 'JCMC'}, {'CO2': 59057, 'M2': 363, 'etiqueta': 'CC',
            'tipo': 'Obras de conservación o protección del medio ambiente', 'color': '#54B5FB', 'estudio': 'RFU'}, {'CO2': 23137, 'M2': 33, 'etiqueta': 'AA', 'tipo': 'Obras de mejora o modernización', 'color': '#00B17B', 'estudio': 'GM'}, {'CO2': 44279, 'M2': 8464, 'etiqueta': 'BB', 'tipo': 'Obras de infraestructura', 'color': '#53328B', 'estudio': 'Montevideo'}]




# Crea las listas desplegables
estudio_dropdown = dcc.Dropdown(
    id='estudio-dropdown',
    options=[{'label': estudio, 'value': estudio} for estudio in estudios],
    value=None,
    clearable=True,
    placeholder='Seleccione un Estudio',
    style={'width': '250px','font-family': 'Arial, sans-serif','text-align': 'center'}
)

tipo_dropdown = dcc.Dropdown(
    id='tipo-dropdown',
    options=[{'label': tipo, 'value': tipo} for tipo in tipo_de_proyectos],
    value=None,
    clearable=True,
    placeholder='Seleccione un Tipo de Proyecto', 
    style={'width': '250px','font-family': 'Arial, sans-serif','text-align': 'center'}
)


# Crea el layout de la aplicación
app.layout = html.Div([
                #html.Div([html.Img(src='C:\Python\GZ\GoZeroLOGO.png', style={'width': '100px', 'height': '100px'})], style={'position': 'absolute', 'top': 0, 'left': 0}),
                html.H1('GO ZERO - Scoring', style={'font-size': '40px', 'font-family': 'Arial, sans-serif','text-align': 'center','color':'#122E50'}),
                html.Div(style={'display': 'flex', 'justifyContent': 'center'},
                children=[
                    html.H3('Estudios', style={'vertical-align': 'middle','margin': '4px 10px 1px 10px','font-size': '20px', 'font-family': 'Arial, sans-serif','color':'#122E50'}),
                    estudio_dropdown,
                    html.H3('Tipo de Proyecto', style={'vertical-align': 'middle','margin': '4px 10px 1px 10px','font-size': '20px', 'font-family': 'Arial, sans-serif','color':'#122E50'}),
                    tipo_dropdown
            ]),
            dcc.Graph(id='GO ZERO - Scoring')])


@app.callback(
    Output('GO ZERO - Scoring', 'figure'),
    [Input('estudio-dropdown', 'value'),
     Input('tipo-dropdown', 'value')])


#funcion de actualizacion del grafico
def update_figure(estudio_dropdown, tipo_dropdown):

    filtered_proyectos = proyectos

    if estudio_dropdown != None:
        filtered_proyectos = [p for p in proyectos if p['estudio'] == estudio_dropdown]
    if tipo_dropdown != None:
        filtered_proyectos = [p for p in filtered_proyectos if p['tipo'] == tipo_dropdown]

    tamanos = [50 if proyecto["M2"] < 200 else 50 for proyecto in filtered_proyectos]
    colores = [estudios_colores[proyecto["estudio"]] for proyecto in filtered_proyectos]

    #shapes
    tickvals= [rango_aa[0], rango_a[0], rango_bb[0], rango_b[0], rango_cc[0], rango_c[0]]
    tickvals= [27500, 38500, 44500, 51000, 60500, 73000]
    ticktext= ["<b>AA</b>","<b>A</b>","<b>BB</b>","<b>B</b>","<b>CC</b>","<b>C</b>"]

    shapes = [
        go.layout.Shape(
            type='rect',
            x0=rango[0],
            x1=rango[1],
            y0=0,
            y1=500,
            xref='x2',
            yref='y',
            fillcolor=colores_hex[etiqueta],
            opacity=0.2,
            line=dict(color='rgba(0,0,0,0)')
        ) for etiqueta, rango in zip(colores_hex, [rango_aa, rango_a, rango_bb, rango_b, rango_cc, rango_c])]

    #detalle de anotaciones
    text = [
        f"CO2: <b>{proyecto['CO2']}</b> kg/m2<br>"
        f"M2: <b>{proyecto['M2']}</b> m2<br>"
        f"CLASE: <b>{proyecto['etiqueta']}</b> <br>"
        f"TIPO: <b>{proyecto['tipo']}</b> <br>"
        f"ESTUDIO: <b>{proyecto['estudio']}</b> "
        for proyecto in filtered_proyectos]

    #actualizar data del grafico
    data = [
        go.Scatter(
            x = [p["CO2"] for p in filtered_proyectos],
            y = [p["M2"] for p in filtered_proyectos],
            xaxis="x",
            mode="markers",
            text= text,
            marker=go.scatter.Marker(
                size=tamanos,  # Tamaño de los puntos en el gráfico
                color=colores,  # Color de los puntos en el gráfico
                opacity=1,  # Opacidad de los puntos en el gráfico
            )
        )   
    ]

    # Actualiza el layout del gráfico
    layout = go.Layout(
        #title=dict(text='<b>GO ZERO - Scoring</b>', font=dict(size=30, family='Arial, sans-serif')),  # Título del gráfico
        xaxis=go.layout.XAxis(title=dict(text='<b>CO2 (kg/m2)</b>',font=dict(family='Arial, sans-serif', size=18, color='#7f7f7f')),range=[20000, 80000],visible=True,side='bottom'),
        yaxis=go.layout.YAxis(title=dict(text='<b>M2 (m2)</b>', font=dict(family='Arial, sans-serif', size=18, color='#7f7f7f')),range=[0,500],visible=True),  # Título del eje Y    
        xaxis2=go.layout.XAxis(
        title=dict(text='<b>Clases</b>', font=dict(family='Arial, sans-serif', size=18, color='#7f7f7f')),  # Título del eje secundario
        overlaying='x',  # Especifica que el eje secundario se superpone al eje principal
        range=[20000, 80000],  #Rango de valores del eje secundario
        visible=True,
        tickvals=tickvals,  # Valores de los ticks del eje secundario
        ticktext=ticktext,  # Texto de los ticks del eje secundario
        showgrid=False,  #No muestra la grilla en el eje secundario
        side='top',
        ),
        shapes=shapes  
        )
    return go.Figure(data=data, layout=layout)

#fig = go.Figure(data=data, layout=layout)


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

    
#plotly.offline.plot(app, filename='app.html')

#plotly.offline.write_html(app, filename='GZ_Scoring.html')
#plotly.offline.plot(app.layout, filename='nombre_archivo.html')
#plotly.offline.plot(app, filename='GZ_Scoring.html', include_plotlyjs=False)
#app.write_html(file='GZ_Scoring.html')
#app.write_html(file='GZ_Scoring.html')
#plotly.offline.plot(app, filename='GZ_Scoring.html')
#plotly.offline.plot(app, filename='GZ_Scoring.html')
#app._generate_scripts_html(app, filename='GZ_Scoring.html')