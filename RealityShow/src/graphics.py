import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

def onebarplot(fig, x, y, color):
    x=x,
    y=y,
    fig.update_traces(
        marker_color=color,
        textposition='outside',
        hoverinfo='text',
        texttemplate='{text:.3s}'
)


    fig.update_layout(
        uniformtext_minsize=12,
        margin=dict(l=0, r=0, t=5, b=5),
        plot_bgcolor='rgba(255,255,255,0.5)',
    legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01),
    xaxis = {'type': 'category'}
)

    fig.update_xaxes(title_text = ' ')

    fig.show()


def twobarplot(fig, x, y, y1, nome_y, nome_y1):

    fig.add_trace(go.Bar(x=x, y=y,
                              marker_line_width=2, name = nome_y,
                             marker_color='#bdc4bc',
                             text = y,
                             textangle = 0,
                         texttemplate='%{text:.3s}',
                             textposition='outside'))

    fig.add_trace(go.Bar(x=x, y=y1, marker_line_width=2, name = nome_y1,
                             marker_color='#0D6E6E',
                             text = y1,
                             textangle = 0,
                         texttemplate='%{text:.3s}',
                             textposition='outside'),
                   secondary_y=False,
                  row=1, col=1)


    fig.update_layout(
      margin=dict(l=5, r=0, t=5, b=0),
      plot_bgcolor='rgba(255,255,255,0.5)',
      legend=dict(orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=0.9),
      xaxis = { 'type': 'category'}
    )

    fig.update_traces(hoverinfo='text')
    fig.update_yaxes(visible = False)


    fig.show()


def barlineplot(fig, x, y, y1, y2, nome_y, nome_y1, nome_y2):

    fig.add_trace(go.Bar(x=x, y=y,
                              marker_line_width=2, name = nome_y,
                             marker_color='#bdc4bc',
                             text = y,
                             textangle = 0,
                             textposition='outside'))

    fig.add_trace(go.Bar(x=x, y=y1, marker_line_width=2, name = nome_y1,
                             marker_color='#0D6E6E',
                             text = y1,
                             textangle = 0,
                             textposition='outside'),
                   secondary_y=False,
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=x, y=y2, marker_line_width=1, line=dict(color='rgb(157, 209, 238)'),
                                 name=nome_y2,
                                 mode="lines+text",
                                 text = y2,
                                 textposition='top left',
                                 texttemplate='%{y:.3s}',
                                 textfont=dict(color='#E58606',
                                            family = 'Arial Black', size = 12)), secondary_y=True, row=1, col=1)

    fig.update_layout(
      margin=dict(l=5, r=0, t=5, b=0),
      plot_bgcolor='rgba(255,255,255,0.5)',
      legend=dict(orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=0.9),
      xaxis = { 'type': 'category'}
    )

    fig.update_traces(hoverinfo='text')


    fig.update_yaxes(visible = False)


    fig.show()

def onebarlineplot(fig, x, y, y1, nome_y, nome_y1):

    fig.add_trace(go.Bar(x=x, y=y,
                              marker_line_width=2, name = nome_y,
                             marker_color='#b4c4b7',
                             text = y,
                             textangle = 0,
                             textposition='outside'))


    fig.add_trace(go.Scatter(x=x, y=y1, marker_line_width=1, line=dict(color='rgb(157, 209, 238)'),
                                 name=nome_y1,
                                 mode="lines+text",
                                 text = y1,
                                 textposition='top left',
                                 texttemplate='%{y:.3s}',
                                 textfont=dict(color='#E58606',
                                            family = 'Arial Black', size = 12)), secondary_y=True, row=1, col=1)

    fig.update_layout(
      margin=dict(l=5, r=0, t=5, b=0),
      plot_bgcolor='rgba(255,255,255,0.5)',
      legend=dict(orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=0.9),
      xaxis = { 'type': 'category'}
    )

    fig.update_traces(hoverinfo='text')


    fig.update_yaxes(visible = False)


    fig.show()