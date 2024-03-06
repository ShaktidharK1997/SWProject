import React, { useState } from 'react';
import axios from 'axios';


function Login() {
    const [credentials, setCredentials] = useState({ username: '', password: '' });

    const handleInputChange = (event) => {
        setCredentials({
            ...credentials,
            [event.target.name]: event.target.value
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/accounts/login/', credentials);
            // Handle successful login here
        } catch (error) {
            // Handle errors here
        }
    };

    return (
        <div className="login-container">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="username"
                    value={credentials.username}
                    onChange={handleInputChange}
                    placeholder="Email"
                />
                <input
                    type="password"
                    name="password"
                    value={credentials.password}
                    onChange={handleInputChange}
                    placeholder="Password"
                />
                <button type="submit">Login</button>
                {/* Include the Google sign-in button and its logic here */}
            </form>
        </div>
    );
}

export default Login;
