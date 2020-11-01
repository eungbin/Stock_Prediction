import { Button } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import './../css/Header.css';

function Header(props) {
    useEffect(() =>  {
        setLoginState({
            loginStat: props.loginStat,
        })
      }, [props]);
    const [loginState, setLoginState] = useState({
        loginStat: props.loginStat,
    })
    const selectMain = async () => {
        props.onSubmit("Main", props.loginStat);
    }

    const selectRequest = async () => {
        props.onSubmit("Request", props.loginStat);
    }

    const selectChange = async () => {
        props.onSubmit("Change", props.loginStat);
    }

    const selectLogin = async () => {
        props.onSubmit("Login", props.loginStat);
    }

    const selectRegister = async () => {
        props.onSubmit("Register", props.loginStat);
    }

    const selectLogout = async() => {
        sessionStorage.setItem("loginStat", false);
        sessionStorage.setItem("id", null);
        sessionStorage.setItem("pw", null);
        props.onSubmit("Main", false);
        alert("로그아웃 되었습니다.");
        // window.location.reload(true);
    }
    if(loginState.loginStat == "true") {
        return (
            <>
                <header>
                    <Button onClick={selectMain}>Stock BOT</Button>
                    <nav>
                        <div className="sixth-menu menu">
                            <p>{props.id} 님</p>
                        </div>
                        {/* <div className="first-menu menu">
                            <Button onClick={selectLogin}>Login</Button>
                        </div>
                        <div className="second-menu menu">
                            <Button onClick={selectRegister}>Register</Button>
                        </div> */}
                        <div className="third-menu menu">
                            <Button onClick={selectLogout}>Logout</Button>
                        </div>
                        <div className="fourth-menu menu">
                            <Button onClick={selectRequest}>Request Board</Button>
                        </div>
                        <div className="fifth-menu menu">
                            <Button onClick={selectChange}>Change Item</Button>
                        </div>
                    </nav>
                </header>
            </>
        );
    } else {
        return (
            <>
                <header>
                    <Button onClick={selectMain}>Stock BOT</Button>
                    <nav>
                        <div className="first-menu menu">
                            <Button onClick={selectLogin}>Login</Button>
                        </div>
                        <div className="second-menu menu">
                            <Button onClick={selectRegister}>Register</Button>
                        </div>
                        {/* <div className="third-menu menu">
                            <Button onClick={selectLogout}>Logout</Button>
                        </div> */}
                        <div className="fourth-menu menu">
                            <Button onClick={selectRequest}>Request Board</Button>
                        </div>
                        <div className="fifth-menu menu">
                            <Button onClick={selectChange}>Change Item</Button>
                        </div>
                    </nav>
                </header>
            </>
        );
    }
}

export default Header;
