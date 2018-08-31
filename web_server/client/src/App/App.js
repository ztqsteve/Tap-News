import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.min.js';

import React, { Component } from 'react';
import logo from './logo.png';
import './App.css';

import NewsPanel from '../NewsPanel/NewsPanel'
class App extends Component {
  render() {
    return (
      <div className="App">
        <img src={logo} className="App-logo" alt="logo" />
        <div className="container">
          <NewsPanel />
        </div>
      </div>
    );
  }
}

export default App;
