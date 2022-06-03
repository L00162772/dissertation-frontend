import React, { useState, useEffect } from 'react';
import { Button, Form } from 'semantic-ui-react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Update() {
    let navigate = useNavigate();
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phoneNumber, setPhoneNumber] = useState(false);

    useEffect(() => {
        setFirstName(localStorage.getItem('First Name'));
        setLastName(localStorage.getItem('Last Name'));
        setPhoneNumber(localStorage.getItem('Phone Number'));
    }, []);

    const updateAPIData = () => {
        axios.put(`https://backend.atu-dissertation.com/users/${phoneNumber}`, {
            firstName,
            lastName,
            phoneNumber
        }).then(() => {
            navigate('/read')
        })
    }
    return (
        <div>
            <Form className="create-form">
                <Form.Field>
                    <label>First Name</label>
                    <input placeholder='First Name' type="text" data-testid="firstName" value={firstName} onChange={(e) => setFirstName(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                    <label>Last Name</label>
                    <input placeholder='Last Name' type="text" data-testid="lastName" value={lastName} onChange={(e) => setLastName(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                    <label>Phone Number</label>
                    <input placeholder='Phone Number' type="text" data-testid="phoneNumber" value={lastName} onChange={(e) => setPhoneNumber(e.target.value)}/>
                </Form.Field>
                <Button type='submit' data-testid="update" onClick={updateAPIData}>Update</Button>
            </Form>
        </div>
    )
}
