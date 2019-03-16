#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:04:05 2019

@author: diviya
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('result.html', result = dict)
    
if __name__ == '__main__':
    app.run(debug = True)