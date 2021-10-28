from flask import render_template, Response
from bokeh.embed import components
from bokeh.io import curdoc
import holoviews as hv
import data
hv.extension("bokeh")
from app import app
from data import create_figure, nwis_set


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/alaska')
def alaska():
    return render_template('alaska.html')

@app.route('/washington')
def washington():
    return render_template('index.html')

@app.route('/id_mt')
@app.route('/kootenai')
def id_mt():
    return render_template('kootenai.html')

@app.route('/alsek')
def alsek():
    id = '15129120'
    ds = nwis_set(id)
    fig = create_figure(ds, '00060')
    renderer = hv.renderer('bokeh')
    hvplot = renderer.get_plot(fig)
    curdoc().add_root(hvplot.state)
    script, div = components(hvplot.state)
    return render_template('alsek.html', script=script, div=div)

@app.route('/unuk')
def unuk():
    return render_template('unuk.html')

@app.route('/stikine')
def stikine():
    return render_template('stikine.html')

@app.route('/taku')
def taku():
    return render_template('taku.html')

@app.route('/salmon')
def salmon():
    id = '15008000'
    ds = nwis_set(id)
    fig = create_figure(ds, '00060')
    renderer = hv.renderer('bokeh')
    hvplot = renderer.get_plot(fig)
    curdoc().add_root(hvplot.state)
    script, div = components(hvplot.state)
    return render_template('salmon.html', script=script, div=div)

