import React from 'react';
import BlogCard from '../BlogCard/BlogCard.js'
import { Container, Row, Col } from 'reactstrap';
import './BlogCardList.css'
import blogdata from '../../data/blogs.json'

export default class BlogCardList extends React.Component {
    render(){
        const blogCards  = blogdata["blogs"].map((blog)=><Col><BlogCard blog={blog}/></Col>)
        return (
            <div className="blogCardListWrapper">
                <Container>
                    <Row xs="3">
                        {blogCards}
                    </Row>
                </Container>
            </div>
        )
    }
}

