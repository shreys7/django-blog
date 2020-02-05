import React from 'react'
import CustomNavbar from '../../components/Navbar/Navbar.js'
import CustomCarousel from '../../components/Carousel/Carousel.js'
import BlogCardList from '../../components/BlogCardList/BlogCardList.js'

import './home.css'
export class Home extends React.Component {
    render() {
        return (
            <div>
                <CustomNavbar />
                <CustomCarousel/>
                <BlogCardList/>
            </div>
        )
    }
}