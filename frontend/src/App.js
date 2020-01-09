import React from 'react';
import './App.css';
import {Home} from './pages/Home/home.js';

// Font awesome icons
import { library } from '@fortawesome/fontawesome-svg-core';
import {faSearch, faUserCircle} from '@fortawesome/free-solid-svg-icons';
library.add(faSearch, faUserCircle)


class App extends React.Component {
  render(){
    return <Home/>
  }
}

export default App;
