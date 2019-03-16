#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:23:04 2019

@author: diviya
"""

from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def cookie_index():
   return render_template('cookie_index.html')

@app.route('/setcookie', methods = ['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        
        return resp
    
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'
       
if __name__ == '__main__':
   app.run(debug = True)