#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:26:46 2019

@author: diviya
"""

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
    
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        print('Hi')
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        print('Hello')
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))
    
if __name__ == '__main__':
    app.run(debug = True)