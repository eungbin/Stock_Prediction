import React from 'react';
import './App.css';
import Main from './components/Main';
import Header from './components/Header';

function App() {
  return (
    <div className="mapWrapper">
      <div className="App-Header">
        <Header />
      </div>
      <div className="App-Body">
        <Main />
      </div>
    </div>
  );
}

export default App;
