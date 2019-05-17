import './App.css'

// Styles
import 'bootstrap/dist/css/bootstrap.css';

import React, {Component} from 'react';
import Calculator from './components/Calculator/Calculator';
import Form from './components/Form/Form';
import FullForm from './components/FullForm/FullForm';
import LifeCycle from './components/LifeCycle/LifeCycle';

class App extends Component {
  render() {
    return  <div className="App">
              <div className="App-heading App-flex">
                <h2>Welcome to <span className="App-react">React</span></h2>
              </div>
              <Calculator />
              <Form />
              <hr/>
              <FullForm />
              <LifeCycle />
              <div className="App-instructions App-flex">
                <img className="App-logo" src={require('./react.svg')}/>
                <p>Edit <code>src/App.js</code> and save to hot reload your changes.</p>
              </div>
            </div>
  }
}

export default App
