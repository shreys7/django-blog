import React from 'react';
import './BlogCard.css'
import Blog from './blog3.jpg'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

export default class BlogCard extends React.Component {
    render(){
        let blog = this.props.blog
        return(
            <div className="cardWrapper">
                <img src={Blog} className="image"/>
                <div className="cardBody">
                    <p className="blogInfo">
                        {blog.author} |&nbsp;
                        {blog.date} |&nbsp;
                         <FontAwesomeIcon icon={["far", "comment-alt"]} className="commentIcon"/> {blog.noOfComments}
                    </p>
                    <p className="blogTitle">{blog.title}</p>
                    <p className="blogBody">{blog.body}</p>
                    <div className="cardLabels">{blog.labels.map((label)=><div className="cardLabel">{label}</div>)}</div>
                </div>
            </div>
        )
    }
}

