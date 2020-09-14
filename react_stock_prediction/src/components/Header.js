import { Button } from '@material-ui/core';
import React from 'react';
import './../css/Header.css';

function App() {
  return (
    <>
        <header>
            <h1>Title</h1>
            <nav>
                <div className="first-menu menu">
                    <Button>Menu1</Button>
                </div>
                <div className="second-menu menu">
                    <Button>Menu2</Button>
                </div>
                <div className="third-menu menu">
                    <Button>Menu3</Button>
                </div>
            </nav>
        </header>
    </>
  );
}

export default App;
