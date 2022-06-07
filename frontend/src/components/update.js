import React, { useState, useEffect } from 'react';
import { Button, Form } from 'semantic-ui-react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Update() {
    let navigate = useNavigate();
    const [id, setId] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [country, setCountry] = useState(false);

    useEffect(() => {
        setId(localStorage.getItem('Id'));
        setFirstName(localStorage.getItem('First Name'));
        setLastName(localStorage.getItem('Last Name'));
        setCountry(localStorage.getItem('Country'));
    }, []);

    const updateAPIData = () => {
        axios.put(`http://backend.atu-dissertation.com/users/${id}`, {
            id,
            firstName,
            lastName,
            country
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
                    <label>Country</label>
                    <input placeholder='Country' type="text" data-testid="country" value={country} onChange={(e) => setCountry(e.target.value)}/>
                </Form.Field>
                <Button type='submit' data-testid="update" onClick={updateAPIData}>Update</Button>
            </Form>
        </div>
    )
}
