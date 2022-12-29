from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import random
import numpy as np
import seaborn as sns
import squarify

def draw_canvas(fig, title):
    new_window = Toplevel()
    new_window.geometry("+%d+%d" % (250, 10))
    new_window.title(title)

    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, new_window)
    toolbar.update()
    toolbar.pack(side=TOP, fill=X)
    
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH) 
    

def area_chart(title, title_one , title_two, data, x, y, ax_legend, plot_label_one, ylabel, legends):
    
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), sharex=True)
    fig.suptitle(title)
    
    ax0.set(title=title_one)
    ax1.set(title=title_two)

    data.plot.area( x=x, y=y, stacked=False, ax=ax0)
    ax0.set(ylabel="Cases")
    ax0.legend([ax_legend])

    data[[x, plot_label_one ]].plot.area(x=x, stacked=False, ax=ax1)
    
    ax1.set(ylabel=ylabel)
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, legends)
    
    draw_canvas(fig, title)

def pie_chart(title, data, labels):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(data, labels=labels, autopct='%.1f%%',
        wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
        textprops={'size': 'x-large'})
    ax.set_title(title, fontsize=14)

    draw_canvas(fig, title)
    
def colored_bar_chart(df, title, first_label, second_label):
    n = df[first_label].unique().__len__()+1
    all_colors = list(plt.cm.colors.cnames.keys())
    random.seed(100)
    c = random.choices(all_colors, k=n)

    # Plot Bars
    plt.figure(figsize=(16,10), dpi= 80)
    plt.bar(df[first_label], df[second_label], color=c, width=.5)
    for i, val in enumerate(df[second_label].values):
        plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})

    # Decoration
    plt.gca().set_xticklabels(df[first_label], rotation=60, horizontalalignment= 'right')
    plt.title(title, fontsize=22)
    plt.ylabel('Cases')
    # fig = plt
    plt.show()
    # draw_canvas(plt.show(), title)
    
def donut_chart(title, values, labels):
    # colors
    colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F']
    # explosion
    explode = (0.05, 0.05, 0.05, 0.05)
    
    # Pie Chart
    plt.pie(values, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.85, explode=explode)
    
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    
    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)
    
    draw_canvas(fig, title)
    
def scatter_plot(title, x, y):
    colors = np.array(["purple","beige","brown","cyan","magenta"])

    plt.scatter(x, y, c=colors)
    plt.title(title, fontsize=22)
    plt.show()

def horizontal_lollipop(title, df, df_first, df_second, label_one, label_two, xlabel, ylabel, yticks):
    my_range=range(1,len(df.index)+1)
    
    # The horizontal plot is made using the hline function
    plt.hlines(y=my_range, xmin=df_first, xmax=df_second, color='grey', alpha=0.4)
    plt.scatter(df_first, my_range, color='skyblue', alpha=1, label=label_one)
    plt.scatter(df_second, my_range, color='green', alpha=0.4 , label=label_two)
    plt.legend()
    
    # Add title and axis names
    plt.yticks(my_range, yticks)
    plt.title(title, loc='left')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Show the graph
    plt.show()
    
def tree_map(title, size, labels ):
    
    plt.close()
    colors=['#efe598','#172d65','#f9dc5c','#e8ac63','#e76f51','#ef233c','#b7094c', '#c7294c', '#b2494c', '#28094d', '#b7015c'] #color palette
    fig = plt.gcf()
    fig.set_size_inches(12, 7.5)
    sns.set_style(style="whitegrid") # set seaborn plot style
    sizes= size
    label= labels
    squarify.plot(sizes=sizes, label=label, alpha=0.6,color=colors).set(title=title)
    plt.title(title, fontsize=14, fontweight="bold")
    plt.axis('off')
    draw_canvas(fig, title)