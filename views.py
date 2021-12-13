from flask import render_template, Response, send_from_directory, request, jsonify
from bokeh.embed import components
from bokeh.io import curdoc
import os
import holoviews as hv
hv.extension("bokeh")
from app import app
from data import nwis_set, nwis_set_iv, dyn_figures


@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        id = '15008000'
        ds = nwis_set_iv(id)
        fig = dyn_figures(ds)
        renderer = hv.renderer('bokeh')
        hvplot = renderer.get_plot(fig)
        curdoc().add_root(hvplot.state)
        call_nwis = components(hvplot.state)
        return jsonify(call_nwis)
    return render_template('data.html')


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
    id = '15008000'
    ds = nwis_set_iv(id)
    fig = dyn_figures(ds)
    renderer = hv.renderer('bokeh')
    hvplot = renderer.get_plot(fig)
    curdoc().add_root(hvplot.state)
    script, div = components(hvplot.state)
    return render_template('kootenai.html', script=script, div=div)


@app.route('/alsek')
def alsek():
    id = '15129120'
    ds = nwis_set(id)
    fig = dyn_figures(ds)
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
    fig = dyn_figures(ds)
    renderer = hv.renderer('bokeh')
    hvplot = renderer.get_plot(fig)
    curdoc().add_root(hvplot.state)
    script, div = components(hvplot.state)
    return render_template('salmon.html', script=script, div=div)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path), 'favicon.ico', mimetype='image/vnd.microsoft.icon')