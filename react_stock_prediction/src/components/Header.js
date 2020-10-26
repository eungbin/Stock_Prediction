import { Button } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import './../css/Header.css';

function Header(props) {
    const selectMain = async () => {
        props.onSubmit("Main");
    }

    const selectRequest = async () => {
        props.onSubmit("Request");
    }

    const selectChange = async () => {
        props.onSubmit("Change");
    }

    return (
        <>
            <header>
                <Button>Stock BOT</Button>
                <nav>
                    <div className="first-menu menu">
                        <Button onClick={selectMain}>Menu1</Button>
                    </div>
                    <div className="second-menu menu">
                        <Button onClick={selectRequest}>Request Board</Button>
                    </div>
                    <div className="third-menu menu">
                        <Button onClick={selectChange}>Change Item</Button>
                    </div>
                </nav>
            </header>
        </>
    );
}

export default Header;
