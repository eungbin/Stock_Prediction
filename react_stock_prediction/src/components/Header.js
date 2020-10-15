import { Button } from '@material-ui/core';
import React from 'react';
import './../css/Header.css';

function App() {
  return (
    <>
        <header>
            <h1>Stock BOT</h1>
            <nav>
                <div className="first-menu menu">
                    <Button>Menu1</Button>
                </div>
                <div className="second-menu menu">
                    <Button>Request Board</Button>
                </div>
                <div className="third-menu menu">
                    <Button>Change Item</Button>
                </div>
            </nav>
        </header>
    </>
  );
}

export default App;
