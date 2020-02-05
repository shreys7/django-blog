import React from 'react';
import {Carousel}  from 'react-bootstrap';
import Blog from './blog3.jpg';
import blogdata from '../../data/blogs.json'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import './Carousel.css';

export default class CustomCarousel extends React.Component {
  render(){
    const carouselItems = blogdata["blogs"].map((blog)=>
      <Carousel.Item>
        <img src={Blog} width={2000} height={500}/>
        <Carousel.Caption className='carousel-caption'>
          <div class="carouselLabels">
            {
              blog.labels.map((label)=>
                <div className="carouselLabel">{label}</div>
              )
            }
          </div>
          <h1>{blog.title}</h1>
          <p>{blog.body}</p>
          <p className="carouselBlogInfo">
            <FontAwesomeIcon icon={["far", "calendar-alt"]} className="calenderIcon"/> {blog.author}&nbsp; &nbsp; &nbsp;
            <FontAwesomeIcon icon="user" className="calenderIcon"/> {blog.date}
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    )
    return(
      <Carousel controls={false}>
        {carouselItems}
      </Carousel>
    )
  }
}