import React from 'react';
import './App.css';
import {Home} from './pages/Home/home.js';

// Font awesome icons
import { library } from '@fortawesome/fontawesome-svg-core';
import {faSearch, faUserCircle, faUser} from '@fortawesome/free-solid-svg-icons';
import {faCommentAlt as farCommentAlt, faCalendarAlt as farCalenderAlt} from '@fortawesome/free-regular-svg-icons';
library.add(faSearch, faUserCircle, faUser, farCommentAlt, farCalenderAlt)


class App extends React.Component {
  render(){
    return <Home/>
  }
}

export default App;
