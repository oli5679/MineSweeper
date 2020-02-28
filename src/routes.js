import React from 'react';
import { Route, Switch } from 'react-router-dom';
import App from './components/App';
import Home from './components/Home';
import Play from './components/Play';

const routes = (
  <App>
    <Switch>
      <Route exact path='/' component={Home} />
      <Route path='/play' component={Play} />
    </Switch>
  </App>
)

export { routes };