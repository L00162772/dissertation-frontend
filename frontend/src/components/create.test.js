import React from 'react';
import { shallow } from 'enzyme';
import {render, screen, fireEvent, cleanup} from '@testing-library/react';
import Create from './create';
import {BrowserRouter as Router} from 'react-router-dom';
import axios from 'axios'
jest.mock('axios');

afterEach(cleanup);
afterEach(() => {
    axios.post.mockClear();
  });

  function mockPostDataCall() {
    axios.post.mockResolvedValueOnce({
      data: {
        results: [
          {
            name: {
              first: "name 1"
            }
          },
          {
            name: {
              first: "name 2"
            }
          }
        ]
      }
    });
  }

describe('<Create /> with no props', () => {
  const container = shallow(<Router><Create /></Router>);

  it('should match the snapshot', () => {
    expect(container.html()).toMatchSnapshot();
  });
  
  // See https://testing-library.com/docs/react-testing-library/cheatsheet
  //https://testing-library.com/docs/example-input-event/
  it('should have firstName field', () => {
    render(<Router><Create /></Router>);
    const input = screen.getByTestId('firstName');
    expect(input).toBeInTheDocument()
    expect(input).toHaveAttribute('placeholder',  'First Name')
    expect(input).toHaveAttribute('type',  'text')
  });

  it('should accept changes in firstName field', () => {
    render(<Router><Create /></Router>);
    const input = screen.getByTestId('firstName');
    fireEvent.change(input, {target: {value: 'first name'}})
    expect(input.value).toBe('first name')
  });

  it('should have lastName field', () => {
    render(<Router><Create /></Router>);
    const input = screen.getByTestId('lastName');
    expect(input).toBeInTheDocument()
    expect(input).toHaveAttribute('placeholder',  'Last Name')
    expect(input).toHaveAttribute('type',  'text')
  });

  it('should accept changes in lastName field', () => {
    render(<Router><Create /></Router>);
    const input = screen.getByTestId('lastName')
    fireEvent.change(input, {target: {value: 'last name'}})
    expect(input.value).toBe('last name')
  });

  it('should have country field', () => {
    render(<Router><Create /></Router>);
    const input = screen.getByTestId('country')
    fireEvent.change(input, {target: {value: 'country'}})
    expect(input.value).toBe('country')
  });
 
  it('should have submit button', () => {
    render(<Router><Create /></Router>);
    const button = screen.getByTestId('submit')
    expect(button).toBeInTheDocument()
    expect(button).toHaveAttribute('type',  'submit')
  });

  it('should trigger submit button', () => {
    render(<Router><Create /></Router>);
    const button = screen.getByTestId('submit')

    mockPostDataCall();

    fireEvent.click(button)
  });
});