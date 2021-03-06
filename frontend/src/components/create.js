import React, { useState } from 'react';
import { Button, Form } from 'semantic-ui-react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Create() {
    let navigate = useNavigate();
    const [country, setCountry] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');


    const postData = () => {
        axios.post(`http://backend.atu-dissertation.com/users`, {
            id: Date.now(),
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
                    <input type="text" placeholder='First Name' data-testid="firstName" onChange={(e) => setFirstName(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                    <label>Last Name</label>
                    <input type="text" placeholder='Last Name' data-testid="lastName" onChange={(e) => setLastName(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                    <label>Country</label>
                    <input type="text" placeholder='Country' data-testid="country" onChange={(e) => setCountry(e.target.value)}/>
                </Form.Field>                     
                <Button onClick={postData} data-testid="submit" type='submit'>Submit</Button>
            </Form>
        </div>
    )
}
 