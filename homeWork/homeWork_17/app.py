from flask import Flask
from flask import render_template
import plotly.express as px
import plotly
import json



app = Flask(__name__)

@app.route("/")
def index1():    
    df = px.data.tips()
    fig = px.box(df, x="day", y="total_bill", color="smoker")
    fig.update_traces(quartilemethod="exclusive")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index1.jinja.html', graphJSON=graphJSON)

@app.route("/index2/")
def index2():
    df = px.data.tips()
    fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group",
             facet_row="time", facet_col="day",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "time": ["Lunch", "Dinner"]})
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index2.jinja.html', graphJSON=graphJSON)

@app.route("/index3/")
def index3():
    df = px.data.gapminder()
    fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index3.jinja.html', graphJSON=graphJSON)