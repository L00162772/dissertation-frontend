import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Table, Button } from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';

export default function Read() {
    let navigate = useNavigate();

    const [APIData, setAPIData] = useState([]);
    useEffect(() => {
        axios.get(`http://backend.atu-dissertation.com/users`)
            .then((response) => {
                console.log(response.data)
                console.log(response.data.Items)
                setAPIData(response.data.Items);
            })
    }, []);

    const setData = (data) => {
        let { id, firstName, lastName, country } = data;
        localStorage.setItem('Id', id);
        localStorage.setItem('First Name', firstName);
        localStorage.setItem('Last Name', lastName);
        localStorage.setItem('Country', country)
        navigate('/update')
    }

    const getData = () => {
        axios.get(`http://backend.atu-dissertation.com/users`)
            .then((getData) => {
                console.log("here 2")
                console.log(getData)
                console.log(getData.data)
                setAPIData(getData.data.Items);
            })
    }

    const onDelete = (id) => {
        axios.delete(`http://backend.atu-dissertation.com/users/${id}`)
        .then(() => {
            getData();
            navigate("/read", { replace: true });
        })
    }

    return (
        <div>
            <Table celled>
                <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell>ID</Table.HeaderCell>
                        <Table.HeaderCell>First Name</Table.HeaderCell>
                        <Table.HeaderCell>Last Name</Table.HeaderCell>
                        <Table.HeaderCell>Country</Table.HeaderCell>
                        <Table.HeaderCell>Update</Table.HeaderCell>
                        <Table.HeaderCell>Delete</Table.HeaderCell>
                    </Table.Row>
                </Table.Header>

                <Table.Body>
                    {APIData.length && APIData.map((data) => {
                        return (
                            <Table.Row key={data.id}>
                                <Table.Cell>{data.id}</Table.Cell>
                                <Table.Cell>{data.firstName}</Table.Cell>
                                <Table.Cell>{data.lastName}</Table.Cell>
                                <Table.Cell>{data.country}</Table.Cell>
                                    <Table.Cell> 
                                        <Button onClick={() => setData(data)}>Update</Button>
                                    </Table.Cell>
                                <Table.Cell>
                                    <Button onClick={() => onDelete(data.id)}>Delete</Button>
                                </Table.Cell>
                            </Table.Row>
                        )
                    })}
                </Table.Body>
            </Table>
        </div>
    )
}
