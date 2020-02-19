import React from 'react'
import { Navbar, NavbarBrand, Nav, NavItem, NavLink } from 'reactstrap'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import './Navbar.css'
export default class CustomNavbar extends React.Component {
    render() {
        return (
            <Navbar className="bg-dark fixed-top NavbarWrapper" dark expand="sm">
                <NavbarBrand className="font-weight-bold" href="/">
                    Blog
                </NavbarBrand>
                <Nav className="ml-auto" navbar>
                    <NavItem className="d-flex align-items-center">
                        <NavLink className="font-weight-bold" href="/">
                            Home
                        </NavLink>
                    </NavItem>
                    <NavItem className="d-flex align-items-center">
                        <NavLink className="font-weight-bold" href="/">
                            Create
                        </NavLink>
                    </NavItem>
                    <NavItem className="d-flex align-items-center">
                        <NavLink className="font-weight-bold" href="/">
                            |
                        </NavLink>
                    </NavItem>
                    <NavItem className="d-flex align-items-center">
                        <NavLink className="" href="/">
                            <div><FontAwesomeIcon icon="search" /></div>
                        </NavLink>
                    </NavItem>
                    <NavItem className="d-flex align-items-center">
                        <NavLink className="" href="/">
                            <FontAwesomeIcon icon="user-circle" />
                        </NavLink>
                    </NavItem>
                </Nav>
            </Navbar>
        )
    }
}